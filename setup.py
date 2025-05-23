from setuptools import setup
import certifi
import shutil
import os

# Ensure cert directory exists
if not os.path.exists('cert'):
    os.mkdir('cert')

# Copy cert bundle
shutil.copy(certifi.where(), 'cert/cacert.pem')

APP = ['app.py']

DATA_FILES = [
    'config.json',
    'sky_logo.png',
    'sky_scribe.icns',
    ('cert', [certifi.where()]) 
]

OPTIONS = {
    'argv_emulation': False,
    'iconfile': 'sky_scribe.icns',
    'resources': ['cert'],
    'packages': [
        'requests', 'schedule', 'watchdog', 'PIL', 'ollama', 'httpx'
    ],
    'includes': [
        'quote_engine', 'weather_api', 'main',
        'config_editor', 'scheduler', 'config_watcher'
    ],
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
