# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[('README.md', '.'), ('data', 'data'), ('LICENSE','.'), ('custom_decks/format.md','custom_decks')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
to_dynamic_link = {"PySide6", "shiboken6"}
to_include = []
for bundle in a.pure:
    name, path, _ = bundle
    if name in to_dynamic_link:
        py_file = path.split("site-packages")[-1][1:]
        print("Dynamic linking", name, path, "->", py_file)
        a.datas.append((py_file, path, "DATA"))
    else:
        to_include.append(bundle)

pyz = PYZ(to_include, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='CyberEmpire',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='CyberEmpire',
)
