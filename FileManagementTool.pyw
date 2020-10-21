import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfilename
import os, shutil

class UI:
    def __init__(self, master, width, height):
        self.master = master 
        self.width = width
        self.height = height
        self.s = ttk.Style()
        self.s.theme_use('clam')

        master.title("United Systems File Management Tool v0.0.1")
        master.geometry('%dx%d+250+250' %(width, height))

        #self.trun = os.getcwd()[20:]
        self.trun = os.getcwd()
        self.currentDirectory = ttk.Label(text="Current Directory: ").place(x=20, y=20)
        self.text = tk.StringVar()
        self.text.set(self.trun)
        self.directoryText = ttk.Label(textvariable=self.text, foreground='dark slate gray').place(x=120, y=20)

        #Interface Buttons
        self.fileButton = ttk.Button(text="Rename Files", width=15).place(x=20, y=60)
        self.moveupButton = ttk.Button(text="Move Files Up", width=15).place(x=20, y=90)
        self.backupButton = ttk.Button(text='Backup Files', width=15, command=lambda:self.backupFiles()).place(x=20, y=120)
        self.compressButton = ttk.Button(text='Zip Files', width=15, command=lambda:self.compressFiles()).place(x=20, y=150)

        self.directoryButton = ttk.Button(text="Change Directory...", width=18, command=lambda:self.changeDirectory()).place(x=130, y=60)

        self.console = tk.Text(height=9, width=59, background='gray', foreground='ghost white', insertborderwidth=7, undo=True, bd=3)
        self.console.place(x=10, y=340)

        self.console.insert(1.0, "United Systems File Management Tool [version 0.0.1]")
        self.console.insert(2.0, "\n")
        self.console.insert(2.0, "(c) 2020 United Systems and Software, Inc.")
        self.console.insert(3.0, "\n")

    def renameFiles(self, event=None):
        return

    def moveupFiles(self, event=None):
        return

    def backupFiles(self, event=None):
        filename = tk.filedialog.askopenfilename(title="Choose File to Backup")
        shutil.copy(filename, os.getcwd())

    def compressFiles(self, event=None):
        filename = tk.filedialog.askopenfilename(title="Choose File to Compress")
        #shutil.make_archive('compressed', 'zip', os.getcwd())
        shutil.make_archive('compressed', 'zip', filename)

    def changeDirectory(self, event=None):
        self.filename = filedialog.askdirectory()
        #print(self.filename)
        self.text = self.filename

if __name__ == '__main__':
    root = Tk()
    interface = UI(root, 500, 500)
    root.mainloop()