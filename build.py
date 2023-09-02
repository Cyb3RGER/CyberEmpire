import os
import subprocess
import PyInstaller.__main__
import zipfile


def zipdir(path, zipf: zipfile.ZipFile, rel: str = ''):
    for root, dir, files in os.walk(path):
        for f in files:
            zipf.write(os.path.join(root, f), os.path.relpath(os.path.join(root, f), os.path.join(path, rel)))


subprocess.check_call([f'{os.path.realpath("ui/build_ui.bat")}'], cwd=f'{os.path.realpath("ui")}')

PyInstaller.__main__.run([
    'CyberEmpire.spec',
    # '-n',
    # 'CyberEmpire',
    # '--add-data', 'README.md;.',
    # '--add-data', 'LICENSE;.',
    # '--add-data', 'data;data',
    # '--windowed',
    '--clean',
    '-y',
])

with zipfile.ZipFile('dist/CyberEmpire.zip', 'w', zipfile.ZIP_DEFLATED) as zipf:
    zipdir('dist/CyberEmpire', zipf)
