# VSCode Nautilus Extension
#
# Place me in ~/.local/share/nautilus-python/extensions/,
# ensure you have python-nautilus package, restart Nautilus, and enjoy :)
#
# This script is released to the public domain.

from gi.repository import Nautilus, GObject
from subprocess import call
import os

# path to vscode
VSCODE = 'code'
VSCODIUM = 'codium' # adding codium path

# what name do you want to see in the context menu?
VSCODENAME = 'Code'
VSCODIUMNAME = 'Codium' # adding codium name

# always create new window?
NEWWINDOW = False


class VSCodeExtension(GObject.GObject, Nautilus.MenuProvider):

    def launch_vscode(self, menu, files):
        safepaths = ''
        args = ''

        for file in files:
            filepath = file.get_location().get_path()
            safepaths += '"' + filepath + '" '

            # If one of the files we are trying to open is a folder
            # create a new instance of vscode
            if os.path.isdir(filepath) and os.path.exists(filepath):
                args = '--new-window '

        if NEWWINDOW:
            args = '--new-window '

        call(VSCODE + ' ' + args + safepaths + '&', shell=True)

    # adding codium function
    def launch_vscodium(self, menu, files):
        safepaths = ''
        args = ''

        for file in files:
            filepath = file.get_location().get_path()
            safepaths += '"' + filepath + '" '

            # If one of the files we are trying to open is a folder
            # create a new instance of vscode
            if os.path.isdir(filepath) and os.path.exists(filepath):
                args = '--new-window '

        if NEWWINDOW:
            args = '--new-window '

        call(VSCODIUM + ' ' + args + safepaths + '&', shell=True)

    def get_file_items(self, *args):
        files = args[-1]
        item1 = Nautilus.MenuItem(
            name='VSCodeOpen',
            label='Open in ' + VSCODENAME,
            tip='Opens the selected files with VSCode'
        )
        item1.connect('activate', self.launch_vscode, files)

        # add codium context menu
        item2 = Nautilus.MenuItem(
            name='VSCodiumOpen',
            label='Open in ' + VSCODIUMNAME,
            tip='Opens the selected files with VSCodium'
        )
        item2.connect('activate', self.launch_vscodium, files)

        return [item1, item2]

    def get_background_items(self, *args):
        file_ = args[-1]
        item1 = Nautilus.MenuItem(
            name='VSCodeOpenBackground',
            label='Open in ' + VSCODENAME,
            tip='Opens the current directory in VSCode'
        )
        item1.connect('activate', self.launch_vscode, [file_])

        # add codium context menu
        item2 = Nautilus.MenuItem(
            name='VSCodiumOpenBackground',
            label='Open in ' + VSCODIUMNAME,
            tip='Opens the current directory in VSCodium'
        )
        item2.connect('activate', self.launch_vscodium, [file_])

        return [item1, item2]
