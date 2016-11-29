# -*- mode: python -*-

basedir = '../..'

import sys, os

assert os.path.exists(SPECPATH + '/' + basedir + '/src/petronia/' + script_name + '.py'), "Could not find script {0}".format(script_name)
assert isinstance(exe_name, str), "exe_name is not a string"
assert isinstance(use_cli, bool), "use_cli is not a boolean"

ARCH = sys.version.lower().find(' 64 bit ') > 0 and 'x64' or 'x86'
# dist = exe_name + '-' + ARCH
dist = exe_name

block_cipher = None

scripts = [basedir + '/src/petronia/' + script_name + '.py']
data_files = [
    (basedir + '/README.md', '.'),
    (basedir + '/CHANGES.md', '.'),
    (basedir + '/LICENSE', '.'),
    (basedir + '/docs', 'docs'),
    (basedir + '/src/no_chrome_config.py', 'example-configs'),
    (basedir + '/src/simple_config.py', 'example-configs'),
    (basedir + '/src/user_test_config.py', 'example-configs'),
    (basedir + '/src/user_test_config.json', 'example-configs'),
    (basedir + '/src/user_test_config.yaml', 'example-configs'),
    (basedir + '/src/no_border_config.yaml', 'example-configs'),
    (basedir + '/src/border_config.yaml', 'example-configs'),
]

extra_imports = [
    'petronia.arch.funcs_any_win',
    'petronia.arch.funcs_win7',
    'petronia.arch.funcs_win8',
    'petronia.arch.funcs_win10',
    'petronia.arch.funcs_winVista',
    'petronia.arch.funcs_winXP',
    'petronia.arch.funcs_x64_win',
    'petronia.arch.funcs_x86_win',
    'petronia.shell.view.portal_chrome',
]

a = Analysis(scripts,
             pathex=[],
             binaries=None,
             datas=data_files,
             hiddenimports=extra_imports,
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name=dist,
          debug=False,
          strip=False,
          upx=True,
          console=use_cli )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name=dist)
