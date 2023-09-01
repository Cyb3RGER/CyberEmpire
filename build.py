import os
import shutil
import subprocess
import PyInstaller.__main__

subprocess.check_call([f'{os.path.realpath("ui/build_ui.bat")}'], cwd=f'{os.path.realpath("ui")}')

PyInstaller.__main__.run([
    'main.py',
    '-n',
    'CyberEmpire',
    # '--onefile',
    '-y',
    '--clean',
    '--windowed',
    '--add-data', 'README.md;.',
    '--add-data', 'data;data',
])

# shutil.copytree('data', 'dist/data')
