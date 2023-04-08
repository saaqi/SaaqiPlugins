import os.path 
import pipes
import re
import subprocess
import tempfile
import sublime
import sublime_plugin
from functools import partial


def cwd_for_window(window):

    active_view = window.active_view()
    active_file = active_view.file_name() if active_view else None
    if settings().get('prefer_active_view_dir') == True:
        return active_view_dir(active_file) or open_folder(window, active_file) or home_dir()
    else:
        return open_folder(window, active_file) or active_view_dir(active_file) or home_dir()

def open_folder(window, active_file_name):
    folders = window.folders()
    if len(folders) == 1:
        return folders[0]

    if not active_file_name:
        return folders[0] if len(folders) else None

    for folder in folders:
        if active_file_name.startswith(folder):
            return folder

def active_view_dir(active_file_name):
    if active_file_name:
        return os.path.dirname(active_file_name)

def home_dir():
    return os.path.expanduser("~")


def abbreviate_user(path):
    """
    Return a path with the ~ dir abbreviated (i.e. the inverse of expanduser)
    """
    home = home_dir()
    if path.startswith(home):
        return "~" + path[len(home):]
    else:
        return path

def settings():
    return sublime.load_settings('SaaqiPlugins.sublime-settings')


def run_cmd(cwd, cmd, wait, input_str=None):
    shell = isinstance(cmd, str)
    if wait:
        proc = subprocess.Popen(cmd, cwd=cwd,
                                     shell=shell,
                                     stdout=subprocess.PIPE,
                                     stderr=subprocess.PIPE,
                                     stdin=(subprocess.PIPE if input_str else None))
        encoded_input = None if input_str == None else input_str.encode('utf8')
        output, error = proc.communicate(encoded_input)
        return_code = proc.poll()
        if return_code:
            show_in_output_panel("`%s` exited with a status code of %s\n\n%s"
                                 % (cmd, return_code, error))
            return (False, None)
        else:
            return (True, output.decode('utf8'))
    else:
        subprocess.Popen(cmd, cwd=cwd, shell=shell)
        return (False, None)


class ReplaceWithTextCommand(sublime_plugin.TextCommand):
    """
    Replace the text in the specified region with the specified text
    """
    def run(self, edit, region_start=None, region_end=None, text=None):
        if region_start and region_end:
            self.view.replace(edit, sublime.Region(region_start, region_end), text)
        else:
            self.view.insert(edit, 0, text)

class SubprocessInCwdCommand(sublime_plugin.WindowCommand):
    """
    Launch a subprocess using the window's working directory
    """
    def run(self, cmd=None, wait=False):
        cwd = cwd_for_window(self.window)
        run_cmd(cwd, cmd, wait)









# Build on Save
class AutoBuildOnSave(sublime_plugin.EventListener):
    def on_post_save(self, view):
        global_settings = sublime.load_settings('SaaqiPlugins.sublime-settings')

        # See if we should build. A project level auto_build_one_save setting
        # takes precedence. To be backward compatible, we assume the global
        # auto_build_one_save to be true if not defined.
        should_build = view.settings().get('auto_build_one_save', global_settings.get('auto_build_one_save', True))

        # Load filename filter. Again, a project level setting takes precedence.
        choose_filenames = view.settings().get('choose_filenames', global_settings.get('choose_filenames', '.*'))

        if not should_build:
            return

        if not re.search(choose_filenames, view.file_name()):
            return

        view.window().run_command('build')
