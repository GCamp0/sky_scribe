# watches json for changes and restarts the scheduler process
import time  # for the test per time
import subprocess
import sys  # for sys.executable to replace hardcoded python3
from watchdog.observers import Observer  # watchdog to monitor file changes
from watchdog.events import FileSystemEventHandler

# start the scheduler process
scheduler_process = subprocess.Popen([sys.executable, "scheduler.py"])

# Function to restart the scheduler process on config change
class ConfigChangeHandler(FileSystemEventHandler):
    def on_modified(self, event):
        # only respond to actual config.json edits
        if event.src_path.endswith("config.json"):
            print("🔄 config.json changed. Restarting scheduler.")
            global scheduler_process
            scheduler_process.terminate()
            scheduler_process.wait()
            scheduler_process = subprocess.Popen([sys.executable, "scheduler.py"])

# normal scheduler process
handler = ConfigChangeHandler()
observer = Observer()
observer.schedule(handler, path=".", recursive=False)
observer.start()

# Main loop to keep the script running with a keyboard interrupt
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
    scheduler_process.terminate()
    observer.join()
