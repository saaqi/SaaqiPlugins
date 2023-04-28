# Saaqi Plugins for Sublime Text

A Sublime Text plugin that combines multiple useful features for web developers. This plugin does not have a unique feature it just combines many small useful features all in one plugin. I created this plugin for my own use and I have decided to launch this for the every one to use.

## Features

* Minify CSS and JavaScript files automatically on save. You can disable the autosave feature on save.
* Open terminal from Sublime Text by pressing CTRL+SHIFT+C. You can choose to open the terminal from the current subfolders or always from the parent or the project.
* Launch Browser-Sync from your current project folder. You can also launch multiple instances of Browser-Sync if you are working on multiple * projects simultaneously.
* AutoPrefix your CSS file.
* Provides many small and useful HTML, CSS, JavaScript, and jQuery snippets.


## Requirements

* Node.js ( for [Clean CSS](https://www.npmjs.com/package/clean-css-cli), [Terser](https://www.npmjs.com/package/tersers), [Browser-Sync](https://www.npmjs.com/package/browser-sync) & [AutoPrefixer-Cli](https://github.com/ai/autoprefixer-cli)
* Terser, Clean-CSS-CLI, AutoPrefixer-Cli & Browser-Sync **installed globally**

**Install Node.js on your system if it is not installed already. Then install.**

<pre><code>npm install clean-css-cli -g</code></pre>
<pre><code>npm install terser -g</code></pre>
<pre><code>npm install browser-sync -g</code></pre>
<pre><code>npm install autoprefixer-cli -g</code></pre>


## Installation

### Saaqi Plugins is not available on Package Control. To install, follow these steps:

1. To install Saaqi Plugins manually, follow these steps:
2. Download the latest release from the GitHub repository.
2. Unzip the downloaded file and rename the folder to "SaaqiPlugins".
4. Move the folder to your Sublime Text packages directory. You can find this directory by clicking on Preferences > Browse Packages in Sublime Text.
5. Restart Sublime Text.


## Usage

### Minifying CSS and JavaScript files
By befault CSS and JavaScript files are minified automatically on save.

If you do not want the plugin th create a minified version every time your save your files, follow these steps:

1. Open the settings file by clicking on Preferences > Package Settings > Saaqi Plugins > Settings - User.
2. In the settings file, set "auto_build_one_save": false. like this.
<pre><code>{
    "auto_build_one_save": false,
}</code></pre>
3. Save the settings file.
4. Now everytime you need to minify yor css or JavaScript file go to Tools > Build.
5. It will automatically create a new file with .min file extension. For example style.css will have a new file called syle.min.css

### Opening the terminal

To open the terminal from Sublime Text, press CTRL+SHIFT+C. By default, the terminal will open from the current active folders. If you want to open the terminal from the root of your Proect folder, follow these steps:

1. Open the settings file by clicking on Preferences > Package Settings > Saaqi Plugins > Settings - User.
2. In the settings file, set "prefer_active_view_dir": false. like this.
<pre><code>{
    "prefer_active_view_dir": false,
}</pre></code>
3. Save the settings file.
4. Now everytime you open the Terminal it will from the root folder of your current project.

### Launching Browser-Sync

To launch Browser-Sync from your current project folder, follow these steps:

1. Open the Command Palette by pressing CTRL+SHIFT+P.
2. Type in "Saaqi: Start Browser-Sync Here" and press Enter.
3. Or simply Right on the opened file from the main screen on the Side-Bar and click "Start Browser-Sync Here".

**Please make sure that you start browser sync from root of your projects folders.**

If you are working on multiple prjects you can launch multiple instances of Browser-Sync, repeat the above steps for each project you want to launch.

### Auto Prefixing your CSS files

To AutoPrefix your CSS file, follow these steps:

1. Open the Command Palette by pressing CTRL+SHIFT+P.
2. Type in "Saaqi: AutoPrefix CSS" and press Enter.

**It will overwrite your currently opened CSS file.**

### Snippets

Saaqi Plugins provides many useful HTML, CSS, JavaScript, and jQuery snippets. To use these snippets, open a file and type in the snippet shortcut. Press Tab to expand the snippet.

To check all the available snippets for your current file.

1. Open the Command Palette by pressing CTRL+SHIFT+P.
2. Type in "Snippet: " and you will see a list fo all the available snippets. 

### License
Saaqi Plugins is released under the MIT License.
