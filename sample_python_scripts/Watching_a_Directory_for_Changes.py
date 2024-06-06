import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class Watcher(FileSystemEventHandler):
    def on_modified(self, event):
        print(f'{event.src_path} has been modified')

path = '.'
observer = Observer()
observer.schedule(Watcher(), path, recursive=False)
observer.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()

observer.join()
