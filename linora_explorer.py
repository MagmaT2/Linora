import os
import tkinter as tk
from tkinter import filedialog

class LinoraExplorer:
    def __init__(self, root):
        self.root = root
        self.root.title("Linora Explorer")
        self.current_path = tk.StringVar(value=os.getcwd())
        
        self.label = tk.Label(root, textvariable=self.current_path)
        self.label.pack()
        
        self.listbox = tk.Listbox(root)
        self.listbox.pack(fill=tk.BOTH, expand=True)
        
        self.load_directory(self.current_path.get())
        
        self.button = tk.Button(root, text="Open Directory", command=self.open_directory)
        self.button.pack()
    
    def load_directory(self, path):
        self.listbox.delete(0, tk.END)
        for item in os.listdir(path):
            self.listbox.insert(tk.END, item)
    
    def open_directory(self):
        new_path = filedialog.askdirectory()
        if new_path:
            self.current_path.set(new_path)
            self.load_directory(new_path)

if __name__ == "__main__":
    root = tk.Tk()
    app = LinoraExplorer(root)
    root.mainloop()