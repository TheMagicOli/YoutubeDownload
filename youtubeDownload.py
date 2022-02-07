#Youtube dlp does the heavy lifting for us in terms of download, we just provide a GUI version of this
from yt_dlp import YoutubeDL
import sys
import time
#Tkinter graphical libraries
from tkinter import *
import tkinter as tk
from tkinter import simpledialog
import tkinter.messagebox as msgbox
def downloadURL(textbox): #Pass string Youtube URL
    continueDownload = True
    if continueDownload == True:
        try:
           ydl_opts = {'format': 'bestaudio', "audio-format": "m4a"} #Specifiy "best" output
           with YoutubeDL(ydl_opts) as ydl:
                ydl.download([textbox])
        except Exception as e:
            msgbox.showerror("Error!", "Error downloading from youtube: " + str(e))
            continueDownload = False
    if continueDownload:
        msgbox.showinfo("Done!", "Saved video in current working directory")
def downloadPress():
    url = urlGiven.get(1.0, "end-1c")
    downloadURL(url)
def onClosing():
        window.destroy()
        sys.exit()
def characterLimit(entryText):
    if len(entryText.get()) > 0:
        entryText.set(entry_text.get()[-1])
def aboutPage():
    win2 = Tk()
    win2.geometry('300x100')
    win2.title("About Me")
    win2.resizable(False, False)
    titleText = tk.Label(win2,
            text="Youtube to MP3 - by TheMagicOli",
        )
    moduleText = tk.Label(win2,
            text="Modules: yt-dlp, tkinter, sys, os",
        )
    licenseText = tk.Label(win2,
            text="MIT License 2.0. Read license.md for more info",
        )
    moduleText.place(x=0,y=20)
    licenseText.place(x=0,y=40)
    titleText.place(x=0,y=0)
def makeWindow():
    window = Tk()
    
    window.geometry('500x300')
    window.title("Youtube to MP3 - v1.0")
    window.resizable(False, False)
    menubar = Menu(window)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Download", command=downloadPress)
    about = Menu(menubar, tearoff=0)
    about.add_command(label="About", command=aboutPage)
    menubar.add_cascade(label="Action",menu=filemenu)
    menubar.add_cascade(label="Info",menu=about)
    filemenu.add_command(label="Quit", command=onClosing)
    window.config(menu=menubar)
    #Buttons and widgets
    global urlGiven
    titleText = tk.Label(window,
            text=" Youtube to MP3",
        )
    titleText.config(font=("Arial",20))
    urlGiven = tk.Text(window,
        width = 50,
        height = 3,
        relief=RIDGE,
        borderwidth = 3,
    )
    downloadSongB = Button(window,
        text = "Download",
        command = downloadPress,
        width = 15,
        height = 5,
    )
    window.protocol("WM_DELETE_WINDOW", window.destroy)
    #urlGiven.trace("w", lambda *args: characterLimit(urlGiven))
    urlGiven.place(x=50,y=100)
    titleText.place(x=160,y=30)
    urlGiven.insert(INSERT, "Put in a valid Youtube URL....")
    downloadSongB.place(x=170,y=155)
    window.mainloop()
#Not the best practice (terrible type conversion for a cheap fix
# for main not working while called, fix later
if "__main__" == __name__:
    makeWindow()