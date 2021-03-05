from tkinter import *
from tkinter import messagebox
from pygame import mixer

def reset_all():
    song1['bg'] = 'white'
    song2['bg'] = 'white'
    song3['bg'] = 'white'
    song4['bg'] = 'white'
    song5['bg'] = 'white'
    song6['bg'] = 'white'
    song7['bg'] = 'white'
    song8['bg'] = 'white'
    song9['bg'] = 'white'

def stop_error():
    messagebox.showwarning("Song Not Started" , "Please choose a song first!")

def stop_play():
    mixer.music.pause()
    global resume_play
    stop['text'] = 'Resume'
    stop['command'] = resume_play

def resume_play():
    mixer.music.unpause()
    global stop_play
    stop['text'] = 'Pause'
    stop['command'] = stop_play

def pause_reset():
    stop['command'] = stop_play
    stop['text'] = 'Pause'

def play_1():
    mixer.init()
    mixer.music.load("Beatbox Lighter - Kwon.mp3")
    mixer.music.play()
    reset_all()
    intro.config(text = "Now playing - Beatbox Lighter!")
    song1['bg'] = 'light blue'
    pause_reset()
    player.update()
#playing Danger Snow
def play_2():
    mixer.init()
    mixer.music.load("Danger Snow - Dan Henig.mp3")
    mixer.music.play()
    reset_all()
    intro.config(text = "Now playing - Danger Snow!")
    song2['bg'] = 'light blue'
    pause_reset()
    player.update()
#playing Electro Fight
def play_3():
    mixer.init()
    mixer.music.load("Electro Fight - Kwon.mp3")
    mixer.music.play()
    reset_all()
    intro.config(text = "Now playing - Electro Fight!")
    song3['bg'] = 'light blue'
    pause_reset()
    player.update()
#playing Find Me Here
def play_4():
    mixer.init()
    mixer.music.load("Find Me Here - Patrick Patrikios.mp3")
    mixer.music.play()
    reset_all()
    intro.config(text = "Now playing - Find Me Here!")
    song4['bg'] = 'light blue'
    pause_reset()
    player.update()
#playing Higher Octane
def play_5():
    mixer.init()
    mixer.music.load("Higher Octane - Vans in Japan.mp3")
    mixer.music.play()
    reset_all()
    intro.config(text = "Now playing - High Octane!")
    song5['bg'] = 'light blue'
    pause_reset()
    player.update()
#playing No Starlight Dey Beat
def play_6():
    mixer.init()
    mixer.music.load("No Starlight Dey Beat - Nana Kwabena.mp3")
    mixer.music.play()
    reset_all()
    intro.config(text = "Now playing - No Starlight!")
    song6['bg'] = 'light blue'
    pause_reset()
    player.update()
#playing Project
def play_7():
    mixer.init()
    mixer.music.load("Project - Patrick Patrikios.mp3")
    mixer.music.play()
    reset_all()
    intro.config(text = "Now playing - Project!")
    song7['bg'] = 'light blue'
    pause_reset()
    player.update()
#playing Street Rhapsody
def play_8():
    mixer.init()
    mixer.music.load("Street Rhapsody - DJ Freedem.mp3")
    mixer.music.play()
    intro.config(text = "Now playing - Street Rhapsody!")
    song8['bg'] = 'light blue'
    pause_reset()
    player.update()
#playing Today's Plan
def play_9():
    mixer.init()
    mixer.music.load("Today's Plan - DJ Freedem.mp3")
    mixer.music.play()
    reset_all()
    intro.config(text = "Now playing - Today's Plan!")
    song9['bg'] = 'light blue'
    pause_reset()
    player.update()
player = Tk()
player.geometry("500x400")
player.title("Your Music Player!")
intro = Label(player, text = "V Music - Your Music Player!" , fg = "black" , font = ("Arial",20) , anchor = E)
song1 = Button(player, text = "Beatbox Lighter" , fg = "black" , font = ("Arial" , 12), width = 12 , command = play_1 , activebackground = "light blue")
song2 = Button(player, text = "Danger Snow" , fg = "black" , font = ("Arial" , 12), width = 12, command = play_2 , activebackground = "light blue")
song3 = Button(player, text = "Electro Fight" , fg = "black" , font = ("Arial" , 12), width = 12 , command = play_3 , activebackground = "light blue")
song4 = Button(player, text = "Find Me Here" , fg = "black" , font = ("Arial" , 12), width = 12 , command = play_4 , activebackground = "light blue")
song5 = Button(player, text = "Higher Octane" , fg = "black" , font = ("Arial" , 12), width = 12 , command = play_5 , activebackground = "light blue")
song6 = Button(player, text = "No Starlight " , fg = "black" , font = ("Arial" , 12), width = 12 , command = play_6 , activebackground = "light blue")
song7 = Button(player, text = "Project" , fg = "black" , font = ("Arial" , 12), width = 12 , command = play_7 , activebackground = "light blue")
song8 = Button(player, text = "Street Rhapsody" , fg = "black" , font = ("Arial" , 12 ), width = 12 , command = play_8 , activebackground = "light blue")
song9 = Button(player, text = "Today's plan" , fg = "black" , font = ("Arial" , 12), width = 12 , command = play_9 , activebackground = "light blue")
stop = Button(player, text = "Pause" , font = ("Arial" , 12), width = 12, command = stop_error , activebackground = "light green" , anchor = CENTER)
intro.pack()
song1.pack()
song2.pack()
song3.pack()
song4.pack()
song5.pack()
song6.pack()
song7.pack()
song8.pack()
song9.pack()
stop.pack()
song1.place(x = 25, y = 65)
song2.place(x = 200, y = 65)
song3.place(x = 375, y = 65)
song4.place(x = 25, y = 130)
song5.place(x = 200, y = 130)
song6.place(x = 375, y = 130)
song7.place(x = 25, y = 195)
song8.place(x = 200, y = 195)
song9.place(x = 375, y = 195)
intro.place(x = 50, y = 10)
stop.place(y = 300 , x = 200)
player.mainloop()
