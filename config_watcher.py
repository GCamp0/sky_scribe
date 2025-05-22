#watches json for changes and restarts the scheduler process
import time #for the test per time
import subprocess
from watchdog.observers import Observer #watchdog to monitor file changes
from watchdog.events import FileSystemEventHandler

#start the scheduler process
scheduler_process = subprocess.Popen(["python3", "scheduler.py"])

# Function to restart the scheduler process on config change
class ConfigChangeHandler(FileSystemEventHandler):
    def on_modified(self, event):
        print("File changed:", event.src_path)
        global scheduler_process
        scheduler_process.terminate()
        scheduler_process = subprocess.Popen(["python3", "scheduler.py"])

#normal scheduler process
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
