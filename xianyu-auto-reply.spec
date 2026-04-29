# -*- mode: python ; coding: utf-8 -*-
"""
闲鱼管理系统 PyInstaller 打包配置文件

用于将 Python 项目打包为独立可执行文件
"""

import os
import sys
from PyInstaller.utils.hooks import collect_data_files, collect_submodules

block_cipher = None

# 收集所有需要的数据文件
datas = [
    ('static', 'static'),
    ('utils', 'utils'),
    ('global_config.yml', '.'),
]

# 如果存在 .env.example 文件，也包含进去
if os.path.exists('.env.example'):
    datas.append(('.env.example', '.'))

# 收集隐式导入的模块
hiddenimports = [
    # FastAPI 相关
    'uvicorn',
    'uvicorn.logging',
    'uvicorn.loops',
    'uvicorn.loops.auto',
    'uvicorn.protocols',
    'uvicorn.protocols.http',
    'uvicorn.protocols.http.auto',
    'uvicorn.protocols.websockets',
    'uvicorn.protocols.websockets.auto',
    'uvicorn.lifespan',
    'uvicorn.lifespan.on',
    
    # Pydantic
    'pydantic',
    'pydantic_core',
    
    # 数据库
    'sqlite3',
    
    # 网络请求
    'aiohttp',
    'httpx',
    'requests',
    'websockets',
    
    # 配置文件
    'yaml',
    'dotenv',
    
    # 日志
    'loguru',
    
    # 加密
    'jwt',
    'passlib',
    'passlib.handlers',
    'passlib.handlers.bcrypt',
    'cryptography',
    
    # 图像处理
    'PIL',
    'qrcode',
    
    # 浏览器自动化
    'playwright',
    
    # AI
    'openai',
    
    # 其他
    'execjs',
    'blackboxprotobuf',
    'psutil',
    'multipart',
    'dateutil',
    'pandas',
    'openpyxl',
    'email_validator',
]

# 收集所有子模块
for module in ['aiohttp', 'httpx', 'websockets', 'pydantic']:
    try:
        hiddenimports.extend(collect_submodules(module))
    except:
        pass

a = Analysis(
    ['Start.py'],
    pathex=[],
    binaries=[],
    datas=datas,
    hiddenimports=hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[
        'tkinter',
        'matplotlib',
        'numpy.f2py',
        'IPython',
        'jupyter',
    ],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='xianyu-auto-reply',
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
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='xianyu-auto-reply',
)
