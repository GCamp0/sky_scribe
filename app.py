import os
import sys

if getattr(sys, 'frozen', False):
    base_path = os.path.dirname(sys.executable)
    cert_path = os.path.abspath(os.path.join(base_path, '..', 'Resources', 'cert', 'cacert.pem'))
    os.environ["SSL_CERT_FILE"] = cert_path

import subprocess
import time
from config_editor import launch_gui


def start_scheduler():
    return subprocess.Popen([sys.executable, "scheduler.py"])

def start_watcher():
    return subprocess.Popen([sys.executable, "config_watcher.py"])

def main():
    scheduler_process = start_scheduler()
    watcher_process = start_watcher()

    try:
        launch_gui()
    finally:
        scheduler_process.terminate()
        watcher_process.terminate()

if __name__ == "__main__":
    main()
