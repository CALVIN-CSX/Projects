#my first project
from file_handler import FileHandler
from watchdog.observers import Observer
import time
import json
with open("mapping.json","r") as f:
    config=json.load(f)
source_folder = config["watch_folder"]
mapping = config["mappings"]
if __name__=="__main__":
   handler =FileHandler(mapping)
   observer=Observer()
   observer.schedule(handler,source_folder,recursive=False)
   observer.start()
   try:
      while True:
          time.sleep(1)
   except KeyboardInterrupt:
       observer.stop()
       print("Observer Stopped")
   observer.join()


