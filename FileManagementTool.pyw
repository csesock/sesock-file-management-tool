import tkinter as tk
from tkinter import ttk
from tkinter import *
import os

class UI:
    def __init__(self, master, width, height):
        self.master = master 
        self.width = width
        self.height = height 

        master.title("United Systems File Management Tool v0.0.1")
        master.geometry('%dx%d+250+250' %(width, height))

        self.currentDirectory = ttk.Label(text="Current Directory: ").place(x=20, y=20)
        self.text = tk.StringVar()
        self.text.set(os.getcwd())
        self.directoryText = ttk.Label(textvariable=self.text, foreground='dark slate gray').place(x=120, y=20)

        self.fileButton = ttk.Button(text="Rename Files", width=15).place(x=20, y=60)
        self.moveupButton = ttk.Button(text="Move Files Up", width=15).place(x=20, y=90)
        self.backupButton = ttk.Button(text='Backup Files', width=15).place(x=20, y=120)

        self.console = tk.Text(height=9, width=59, background='gray', foreground='ghost white', insertborderwidth=7, undo=True, bd=3)
        self.console.place(x=10, y=340)

        self.console.insert(1.0, "United Systems File Management Tool [version 0.0.1]")
        self.console.insert(2.0, "\n")
        self.console.insert(2.0, "(c) 2020 United Systems and Software, Inc.")
        self.console.insert(3.0, "\n")

        

root = Tk()
interface = UI(root, 500, 500)
root.mainloop()