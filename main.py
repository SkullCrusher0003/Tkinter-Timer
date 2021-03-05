#Importing libraries
import time
from tkinter import *
from pygame import mixer

def timer():
    clock.destroy()
    mixer.init()
    mixer.music.load("")
    mixer.music.play()
    options = Tk()
    options.geometry("400x150")
    options.title("Options")
    def stop_timer():
        heading.config(text = "Timer Stopped!")
        mixer.music.pause()
    def snooze_5():
        heading.config(text = "Snoozed!")
        mixer.music.pause()
        time.sleep(300)
        mixer.music.unpause()
    heading = Label(options, text = "Your time is up!", fg = "red", font = ("Helvetica", 20, "bold"), anchor = CENTER)
    stop = Button(options, text = "Stop", font = 50, width = 16, activebackground = "light green", command = stop_timer).place(x = 45, y = 50)
    snooze = Button(options, text = "Snooze", font = 50, width = 16, activebackground = "light green", command = snooze_5).place(x = 225, y = 50)
    heading.pack()
    options.mainloop()
def convert_timing():
    reaction = int(hour.get() * 3600 + minute.get() * 60 + second.get())
    if reaction == 0:
        warn = Label(clock, text = "Please enter some time", fg = "red" , bg = "black" , font = ("Arial",20,"bold")).place(x = 225, y = 250)
    else:
        remind.config(text = "Time Left")
        while True:
            for i in range(reaction):
                mins,secs = divmod(reaction,60)
                hours = 0
                if mins > 60:
                    hours,mins = divmod(mins,60)
                time.sleep(1)
                Intro.config(text = f"{hours}:{mins}:{secs}")
                clock.update()
                reaction -= 1
                if reaction == 0:
                    timer()

clock = Tk()
clock.title("Timer")
clock.geometry("400x300")

Intro = Label(clock, text = "Enter the duration", fg = "blue", font = ("Arial",23,"bold"), anchor = CENTER)
remind = Label(clock, text = "Hrs         Min        Sec", font = ("Arial", 28), anchor = CENTER)

hour = IntVar()
minute = IntVar()
second = IntVar()
hour.set("00")
minute.set("00")
second.set("00")

hours = Entry(clock, bg = "Light Blue", font = 20, textvariable = hour, width = 12).place(x = 5, y = 100)
minutes = Entry(clock, bg = "Light Blue", font = 20, textvariable = minute, width = 12).place(x = 145, y = 100)
seconds = Entry(clock, bg = "Light Blue", font = 20, textvariable = second, width = 12).place(x = 285, y = 100)
enter = Button(clock, text = "Set Timer", width = 15, font = 50, command = convert_timing, activebackground = "light pink")

Intro.pack()
remind.pack()
enter.pack()
enter.place(x = 140, y = 200)
clock.mainloop()
