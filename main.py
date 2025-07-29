from watcher import Watcher
import os

if __name__ == "__main__":
    # Example: monitor the Downloads folder
    folder = os.path.join(os.path.expanduser("~"), "Downloads")
    cleaner = Watcher(folder)
    cleaner.run()
