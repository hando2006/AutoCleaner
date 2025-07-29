import time
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from cleaner import categorize_and_move

class Watcher:
    def __init__(self, folder_to_watch, log_func=None):
        self.folder_to_watch = folder_to_watch
        self.observer = Observer()
        self.log_func = log_func

    def run(self):
        event_handler = Handler(self.folder_to_watch, self.log_func)
        self.observer.schedule(event_handler, self.folder_to_watch, recursive=False)
        self.observer.start()
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            self.stop()

    def stop(self):
        self.observer.stop()
        self.observer.join()

class Handler(FileSystemEventHandler):
    def __init__(self, base_dir, log_func):
        self.base_dir = base_dir
        self.log = log_func

    def on_created(self, event):
        if not event.is_directory:
            time.sleep(1)  # Wait for file to finish copying
            categorize_and_move(event.src_path, self.base_dir)
            if self.log:
                filename = os.path.basename(event.src_path)
                self.log(f"📁 Moved: {filename}")
