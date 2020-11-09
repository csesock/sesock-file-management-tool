import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import filedialog, messagebox
from tkinter.filedialog import askopenfilename
import os, shutil
from os import rename, listdir

master = tk.Tk()
master.title("United Systems File Management Tool v0.0.2")
left_edge = master.winfo_screenwidth()/3
top_edge = master.winfo_screenheight()/3
master.geometry('%dx%d+250+250' %(500, 560))
master.resizable(False, False)

BUTTON_WIDTH = 18

master.bind('<Control-c>', lambda event: console.delete(1.0, "end"))
master.bind('<F1>', lambda event: aboutDialog())

try:
    dirp = os.path.dirname(__file__)
    photo = PhotoImage(file="assets\\IconSmall.png")
    master.iconphoto(False, photo)
except:
    pass

full_directory = os.getcwd()
text = tk.StringVar()
text.set(full_directory[-50:])

currentDirectory = ttk.Label(text="Current Directory: ").place(x=40, y=20)
directoryText = ttk.Label(textvariable=text, foreground='dark slate gray').place(x=140, y=20)

#Interface buttons
#Column 1
fileButton = ttk.Button(text="Rename Files", width=BUTTON_WIDTH, command=lambda:renameFiles()).place(x=40, y=60)
moveupButton = ttk.Button(text="Move Files Up", width=BUTTON_WIDTH, command=lambda:moveupFiles()).place(x=40, y=90)
backupButton = ttk.Button(text='Backup Files', width=BUTTON_WIDTH, command=lambda:backupFiles()).place(x=40, y=120)
compressButton = ttk.Button(text='Zip Files', width=BUTTON_WIDTH, command=lambda:compressFiles()).place(x=40, y=150)
listfilesButton = ttk.Button(text='List Files', width=BUTTON_WIDTH, command=lambda:listFiles()).place(x=40, y=180)
#Column 2
test1button = ttk.Button(text="Test 1", width=BUTTON_WIDTH).place(x=183, y=60)
test2button = ttk.Button(text="Test 1", width=BUTTON_WIDTH).place(x=183, y=90)
test3button = ttk.Button(text="Test 1", width=BUTTON_WIDTH).place(x=183, y=120)
test4button = ttk.Button(text="Test 1", width=BUTTON_WIDTH).place(x=183, y=150)
test5button = ttk.Button(text="Test 1", width=BUTTON_WIDTH).place(x=183, y=180)
#Column 3
directoryButton = ttk.Button(text="Change Directory...", width=BUTTON_WIDTH, command=lambda:changeDirectory()).place(x=326, y=60)
settingsButton = ttk.Button(text="Settings", width=BUTTON_WIDTH).place(x=326, y=90)


console = tk.Text(height=14, width=59, background='black', foreground='lawn green', insertborderwidth=7, undo=True, bd=3)
console.place(x=10, y=300)

console.insert(1.0, "United Systems File Management Tool [version 0.0.2]")
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
filemenu.add_command(label="Exit", accelerator='Alt+F4', command=lambda:master.destroy())
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
#windowmenu.add_command(label="Full Screen", accelerator="F11", command=lambda:fullscreenWindow())
windowmenu.add_separator()
#windowmenu.add_command(label="Reset Window", accelerator="F10", command=lambda:resetWindow())
menubar.add_cascade(label="Window", menu=windowmenu)

helpmenu = tk.Menu(menubar, tearoff=0)
helpmenu.add_command(label="About This Tool", accelerator='F1', command=lambda:aboutDialog())
#helpmenu.add_command(label="Purge Log Files", command=lambda:Logging.deleteLog(int(logDeleteOldInput.get())))
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
    filename = filedialog.askdirectory()
    for root, dirs, files in os.walk(filename, topdown=False):
        for file in files:
            try:
                shutil.move(os.path.join(root, file), filename)
            except OSError:
                pass

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

def listFiles(event=None):
    files = os.listdir(full_directory)
    console.delete(1.0, 'end')
    counter = 1.0
    for file in files:
        console.insert(counter, file+'\n')
        counter+=1.0

def changeDirectory(event=None):
    console.delete(1.0, 'end')
    console.insert(1.0, "Changing directory...\n")
    
    filename = filedialog.askdirectory()
    if filename == None or filename == False:
        console.insert(2.0, "Operation cancelled\n")
        return 
    global full_directory
    full_directory = filename 
    text.set(filename)

    console.insert(2.0, "Directory successfully changed\n")

def changeTheme(theme):
    s = ttk.Style()
    s.theme_use(theme)

def aboutDialog():
    dialog = """ Author: Chris Sesock \n Version: 0.0.2 \n Commit: 077788d6166f5d69c9b660454aa264dd62956fb6 \n Date: 2020-11-06:12:00:00 \n Python: 3.8.3 \n OS: Windows_NT x64 10.0.10363
             """
    messagebox.showinfo("About", dialog)

if __name__ == '__main__':
    master.config(menu=menubar)
    master.mainloop()