from tkinter import *
from tkinter import ttk
import os
from pygame import mixer
import fnmatch

# Create an instance of Tkinter frame
win = Tk()

# Define the geometry
win.geometry("750x350")
win.configure(bg="pink")
win.title("Music Player")


# Create Buttons in the frame
rootpath=r"C:\Users\3053tu\OneDrive\Desktop\songs"
pattern="*.mp3"
mixer.init()

Label(win, text="Music Player", font="Consolas 25",bg="black",fg="white").pack(side=TOP)


#functions for making btn working-----

# for play-----

def select():
    song=list_box.get(ACTIVE)
    song=r"C:\Users\3053tu\OneDrive\Desktop\songs\Believer.mp3"

    mixer.music.load(song)
    mixer.music.play()


#for pause------

def Pause():
    mixer.music.pause() 


 #for resume--------

def Resume():
    mixer.music.unpause() 



#buttons----

play_button = ttk.Button(win,text="Play", command=select)
play_button.place(x=225, y=330)

pause_btn = ttk.Button(win, text="Pause" ,command=Pause)
pause_btn.place(x=325, y=330)

resume_button = ttk.Button(win, text="Resume",command=Resume )
resume_button.place(x=425, y=330)
 


#Create a llist_box--------

list_box = Listbox(win,fg="black",width=100,font=("poppins",15))
list_box.pack(padx=15, pady=15) 

for root, dirs, files in os.walk(rootpath):
    for filename in fnmatch.filter(files,pattern):
       list_box.insert('end',filename)

win.mainloop()