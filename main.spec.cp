# -*- mode: python ; coding: utf-8 -*-
exename = "AutoStarRail v1.0.1"

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[('D:\\work_console\\AutoStarRail\\.venv\\Lib\\site-packages\\vgamepad\\win\\vigem\\client\\x64\\ViGEmClient.dll','.\\vgamepad\\win\\vigem\\client\\x64')],
    datas=[],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name=exename,
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='icon\\jizi.ico'
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name=exename,
)
