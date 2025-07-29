import os
import time
import threading
import tkinter as tk
from tkinter import filedialog
from watcher import Watcher

class AutoCleanerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("J.A.R.V.I.S AutoCleaner")
        self.root.geometry("600x400")
        self.root.configure(bg="#0f0f0f")
        self.observer = None
        self.folder = ""
        self.is_watching = False

        self.build_ui()

    def build_ui(self):
        tk.Label(self.root, text="AutoCleaner – J.A.R.V.I.S v4", font=("Segoe UI", 20),
                 fg="#00ffcc", bg="#0f0f0f").pack(pady=20)

        self.path_label = tk.Label(self.root, text="No folder selected", fg="#7dffbd", bg="#0f0f0f")
        self.path_label.pack(pady=5)

        tk.Button(self.root, text="Select Folder", command=self.select_folder,
                  bg="#111", fg="#00ffcc", activebackground="#00ffcc", activeforeground="#000",
                  relief=tk.FLAT).pack(pady=5)

        self.start_btn = tk.Button(self.root, text="Start Monitoring", command=self.start_monitoring,
                                   bg="#00ffcc", fg="#000", relief=tk.FLAT)
        self.start_btn.pack(pady=5)

        tk.Button(self.root, text="Stop Monitoring", command=self.stop_monitoring,
                  bg="#111", fg="#ff5c5c", activebackground="#ff5c5c", relief=tk.FLAT).pack(pady=5)

        self.log_box = tk.Text(self.root, height=10, width=70, bg="#121212", fg="#00ffcc", wrap=tk.WORD)
        self.log_box.pack(pady=10)

    def select_folder(self):
        folder = filedialog.askdirectory()
        if folder:
            self.folder = folder
            self.path_label.config(text=f"Selected: {self.folder}")

    def log(self, message):
        self.log_box.insert(tk.END, message + "\n")
        self.log_box.see(tk.END)

    def start_monitoring(self):
        if self.folder and not self.is_watching:
            self.is_watching = True
            self.log("🔍 Started watching: " + self.folder)

            def run_observer():
                self.watcher = Watcher(self.folder, self.log)
                self.watcher.run()

            self.thread = threading.Thread(target=run_observer, daemon=True)
            self.thread.start()

    def stop_monitoring(self):
        if self.is_watching:
            self.watcher.stop()
            self.is_watching = False
            self.log("🛑 Stopped watching.")

# Run GUI
if __name__ == "__main__":
    root = tk.Tk()
    app = AutoCleanerGUI(root)
    root.mainloop()
