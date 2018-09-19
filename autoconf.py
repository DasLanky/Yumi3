# Python3
from shutil import copyfile
import os

I3_WORKSPACE_DIR = os.path.expanduser('~/.i3/')
COMPTON_CFG_DIR = os.path.expanduser('~/.config/')
I3_CFG_DIR = os.path.expanduser('~/.config/i3/')
VIS_CFG_DIR = os.path.expanduser('~/.config/vis/')
TERM_CFG_DIR = os.path.expanduser('~/.config/terminator/')
WALLPAPER_DIR = os.path.expanduser('~/Pictures/')

if not os.path.exists(I3_WORKSPACE_DIR):
    print('Creating new directory ' + I3_WORKSPACE_DIR)
    os.mkdir(I3_WORKSPACE_DIR)

if not os.path.exists(COMPTON_CFG_DIR):
    print('Creating new directory ' + COMPTON_CFG_DIR)
    os.mkdir(COMPTON_CFG_DIR)

if not os.path.exists(I3_CFG_DIR):
    print('Creating new directory ' + I3_CFG_DIR)
    os.mkdir(I3_CFG_DIR)

if not os.path.exists(TERM_CFG_DIR):
    print('Creating new directory' + TERM_CFG_DIR)
    os.mkdir(TERM_CFG_DIR)

# i3 config
print('Copying i3 config to ' + I3_CFG_DIR + 'config')
copyfile(os.path.abspath('./.config/i3/config'), I3_CFG_DIR + 'config')

# workspaces
print('Copying workspaces to ' + I3_WORKSPACE_DIR)
for name in os.listdir(I3_WORKSPACE_DIR):
    print('Copying workspace: ' + name)
    copyfile(os.path.abspath('./.i3/' + name), I3_WORKSPACE_DIR + name)

# Compton config
print('Copying compton config to ' + COMPTON_CFG_DIR + 'compton.conf')
copyfile(os.path.abspath('./.config/compton.conf'), COMPTON_CFG_DIR + 'compton.conf')

# Visualizer config
print('Copying cli-visualizer config to ' + VIS_CFG_DIR + 'config')
copyfile(os.path.abspath('./.config/vis/config'), VIS_CFG_DIR + 'config')

# Terminator config
print('Copying terminator config to ' + TERM_CFG_DIR + 'config')
copyfile(os.path.abspath('./.config/terminator/config'), TERM_CFG_DIR + 'config')

# Wallpaper config
print('Copying wallpaper to ' + WALLPAPER_DIR + 'wallpaper.png')
copyfile(os.path.abspath('./wallpaper.png'), WALLPAPER_DIR + 'wallpaper.png')

print('Done.')
