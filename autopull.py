# Python3
from shutil import copyfile
import os

I3_WORKSPACE_DIR = os.path.expanduser('~/.i3/')
COMPTON_CFG_DIR = os.path.expanduser('~/.config/')
I3_CFG_DIR = os.path.expanduser('~/.config/i3/')
VIS_CFG_DIR = os.path.expanduser('~/.config/vis/')
TERM_CFG_DIR = os.path.expanduser('~/.config/terminator/')

if not os.path.exists(I3_WORKSPACE_DIR):
    print('Directory non-existant: ' + I3_WORKSPACE_DIR)

if not os.path.exists(COMPTON_CFG_DIR):
    print('Directory non-existant: ' + COMPTON_CFG_DIR)

if not os.path.exists(I3_CFG_DIR):
    print('Directory non-existant: ' + I3_CFG_DIR)

if not os.path.exists(VIS_CFG_DIR):
    print('Directory non-existant: ' + VIS_CFG_DIR)

if not os.path.exists(TERM_CFG_DIR):
    print('Directory non-existant: ' + TERM_CFG_DIR)

# i3 config
print('Copying i3 config from ' + I3_CFG_DIR + ' to ./config/i3/config')
copyfile(I3_CFG_DIR + 'config', os.path.abspath('./.config/i3/config'))

# workspaces
print('Copying workspaces from ' + I3_WORKSPACE_DIR + ' to ./.i3/')
for name in os.listdir(I3_WORKSPACE_DIR):
    print('Copying workspace: ' + name)
    copyfile(I3_WORKSPACE_DIR + name, os.path.abspath('./.i3/' + name))

# Compton config
print('Copying compton config from ' + COMPTON_CFG_DIR + ' to ./.config/compton.conf')
copyfile(COMPTON_CFG_DIR + 'compton.conf', os.path.abspath('./.config/compton.conf'))

# Visualizer config
print('Copying cli-visualizer config from ' + VIS_CFG_DIR + ' to ./.config/vis/config')
copyfile(VIS_CFG_DIR + 'config', os.path.abspath('./.config/vis/config'))

# Terminator config
print('Copying terminator config from ' + TERM_CFG_DIR + ' to ./.config/terminator/config')
copyfile(TERM_CFG_DIR + 'config', os.path.abspath('./.config/terminator/config'))

print('Done.')

