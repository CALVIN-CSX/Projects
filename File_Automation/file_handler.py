import os
import shutil
import time
from watchdog.events import FileSystemEventHandler

class FileHandler(FileSystemEventHandler):
    def __init__(self, mapping):
        self.mapping = mapping  # Store mapping passed from main.py

    def process_file(self, file_path):
        filename = os.path.basename(file_path)
        extension = os.path.splitext(filename)[1].lower()

        # Ignore temp/incomplete downloads
        if filename.endswith(('.crdownload', '.part', '.tmp')):
            return

        destination_folder = self.mapping.get(extension)
        if not destination_folder:
            destination_folder = self.mapping.get("default")

        destination_path = os.path.join(destination_folder, filename)

        print("Event triggered for:", file_path)
        print("Filename:", filename)
        print("Extension:", extension)
        print("Destination folder:", destination_folder)

        while True:
            if os.path.exists(file_path):
                try:
                    shutil.move(file_path, destination_path)
                    print(f"Moved {file_path} to {destination_path}")
                    return
                except PermissionError:
                    time.sleep(1)
                except Exception as e:
                    print(f"Failed to move {file_path}: {e}")
                    return
            else:
                time.sleep(1)

    def on_created(self, event):
        if not event.is_directory:
            self.process_file(event.src_path)

    def on_moved(self, event):
        if not event.is_directory:
            self.process_file(event.dest_path)
