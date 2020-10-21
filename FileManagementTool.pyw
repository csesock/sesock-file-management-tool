import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfilename
import os, shutil
from os import rename, listdir

master = tk.Tk()
master.title("United Systems File Management Tool v0.0.1")
master.geometry('%dx%d+250+250' %(500, 500))

trun = os.getcwd()[20:]
#trun = os.getcwd()
urrentDirectory = ttk.Label(text="Current Directory: ").place(x=20, y=20)
text = tk.StringVar()
text.set(trun)
directoryText = ttk.Label(textvariable=text, foreground='dark slate gray').place(x=120, y=20)

#Interface Buttons
fileButton = ttk.Button(text="Rename Files", width=15, command=lambda:renameFiles()).place(x=20, y=60)
moveupButton = ttk.Button(text="Move Files Up", width=15).place(x=20, y=90)
backupButton = ttk.Button(text='Backup Files', width=15, command=lambda:backupFiles()).place(x=20, y=120)
compressButton = ttk.Button(text='Zip Files', width=15, command=lambda:compressFiles()).place(x=20, y=150)

directoryButton = ttk.Button(text="Change Directory...", width=18, command=lambda:changeDirectory()).place(x=130, y=60)

console = tk.Text(height=9, width=59, background='black', foreground='lawn green', insertborderwidth=7, undo=True, bd=3)
console.place(x=10, y=340)

console.insert(1.0, "United Systems File Management Tool [version 0.0.1]")
console.insert(2.0, "\n")
console.insert(2.0, "(c) 2020 United Systems and Software, Inc.")
console.insert(3.0, "\n")

#menu
menubar = tk.Menu(master)

filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="Open...", accelerator='Ctrl+O')
filemenu.add_command(label="Save", accelerator='Ctrl+S')
filemenu.add_command(label="Save As...", accelerator='Ctrl+Alt+S')
filemenu.add_separator()
filemenu.add_command(label="Exit", accelerator='Alt+F4')
menubar.add_cascade(label="File", menu=filemenu)

editmenu = tk.Menu(menubar, tearoff=0)
editmenu.add_command(label="Clear Console", accelerator="Ctrl+C", command=lambda:console.delete(1.0, 'end'))

submenu = Menu(editmenu)

submenu.add_command(label="clam", command=lambda:changeTheme('clam'))
submenu.add_command(label="winnative", command=lambda:changeTheme('winnative'))
submenu.add_command(label="alt", command=lambda:changeTheme('alt'))
submenu.add_command(label="xpnative", command=lambda:changeTheme('xpnative'))
submenu.add_command(label="default", command=lambda:changeTheme('default'))
submenu.add_command(label="classic", command=lambda:changeTheme('classic'))
submenu.add_command(label="vista", command=lambda:changeTheme('vista'))

editmenu.add_cascade(label="Theme", menu=submenu)
menubar.add_cascade(label="Edit", menu=editmenu)

windowmenu = tk.Menu(menubar, tearoff=0)
windowmenu.add_command(label="Full Screen", accelerator="F11", command=lambda:fullscreenWindow())
windowmenu.add_separator()
windowmenu.add_command(label="Reset Window", accelerator="F10", command=lambda:resetWindow())
menubar.add_cascade(label="Window", menu=windowmenu)

helpmenu = tk.Menu(menubar, tearoff=0)
helpmenu.add_command(label="About This Tool", accelerator='F1', command=lambda:aboutDialog())
helpmenu.add_command(label="Purge Log Files", command=lambda:Logging.deleteLog(int(logDeleteOldInput.get())))
menubar.add_cascade(label="Help", menu=helpmenu)


def renameFiles(event=None):
    console.delete(1.0, 'end')
    console.insert(1.0, 'Opening File Rename dialog...\n')

    directory = filedialog.askdirectory()
    to_be_named = os.listdir(path = directory)

    for i in range(0, len(to_be_named)):
        os.rename(to_be_named[i], str(i + 1))

    console.insert(2.0, "Files successfully renamed")

def moveupFiles(event=None):
    return

def backupFiles(event=None):
    console.delete(1.0, 'end')
    console.insert(1.0, "Opening Backup File dialog...\n")

    filename = tk.filedialog.askopenfilename(title="Choose File to Backup")
    shutil.copy(filename, os.getcwd())

    console.insert(2.0, "Files successfully backed up")

def compressFiles(event=None):
    filename = tk.filedialog.askopenfilename(title="Choose File to Compress")
    #shutil.make_archive('compressed', 'zip', os.getcwd())
    shutil.make_archive('compressed', 'zip', filename)

def changeDirectory(event=None):
    console.delete(1.0, 'end')
    console.insert(1.0, "Changing directory...\n")
    
    filename = filedialog.askdirectory()[20:]
    text.set(filename)

    console.insert(2.0, "Directory successfully changed\n")


def changeTheme(theme):
    s = ttk.Style()
    s.theme_use(theme)

if __name__ == '__main__':
    master.config(menu=menubar)
    master.mainloop()