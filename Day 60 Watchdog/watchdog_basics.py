from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time


class MyHandler(FileSystemEventHandler):

    def on_modified(self, event):
        print(f"Modified: {event.src_path}")

    def on_created(self, event):
        print(f"Created: {event.src_path}")

    def on_deleted(self, event):
        print(f"Deleted: {event.src_path}")


path = "."

event_handler = MyHandler()

observer = Observer()

observer.schedule(
    event_handler,
    path,
    recursive=True
)

observer.start()

print("Watching folder...")

try:

    while True:
        time.sleep(1)

except KeyboardInterrupt:

    observer.stop()

observer.join()