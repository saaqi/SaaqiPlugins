import sublime
import sublime_plugin
import re

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
