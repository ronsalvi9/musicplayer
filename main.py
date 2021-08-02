import tkinter as tk
import fnmatch
import os
from pygame import mixer

canvas = tk.Tk()
canvas.title("Music Player")
canvas.geometry("900x600")
canvas.config(background="#ebebeb")

rootpath = "music"
pattern = "*.mp3"

mixer.init()

prev_img = tk.PhotoImage(file="prev.png")
stop_img = tk.PhotoImage(file="stop.png")
play_img = tk.PhotoImage(file="play.png")
pause_img = tk.PhotoImage(file="pause.png")
next_img = tk.PhotoImage(file="next.png")


def select():
    label.config(text=listBox.get("anchor"))
    mixer.music.load(rootpath+"/"+listBox.get("anchor"))
    mixer.music.play()


def stop():
    mixer.music.stop()
    listBox.select_clear("active")


def play_next():
    next_song = listBox.curselection()
    next_song = next_song[0]+1
    next_song_name = listBox.get(next_song)
    label.config(text=next_song_name)

    mixer.music.load(rootpath+"/"+next_song_name)
    mixer.music.play()

    listBox.select_clear(0, "end")
    listBox.activate(next_song)
    listBox.select_set(next_song)


def play_prev():
    next_song = listBox.curselection()
    next_song = next_song[0]-1
    next_song_name = listBox.get(next_song)
    label.config(text=next_song_name)

    mixer.music.load(rootpath+"/"+next_song_name)
    mixer.music.play()

    listBox.select_clear(0, "end")
    listBox.activate(next_song)
    listBox.select_set(next_song)


def pause_song():
    if pauseButton["text"] == "Pause":
        mixer.music.pause()
        pauseButton['text'] = "Play"
    else:
        mixer.music.unpause()
        pauseButton["text"] = "Pause"


listBox = tk.Listbox(canvas, foreground="cyan", background="black",
                     width=100, font=('poppins', 14))
listBox.pack(padx=15, pady=15)

label = tk.Label(canvas, text="", background="#ebebeb",
                 foreground="black", font=("poppins", 20))
label.pack(pady=15)

top = tk.Frame(canvas, bg="#ebebeb")
top.pack(padx=10, pady=5, anchor='center')

prevButton = tk.Button(canvas, text="Prev",
                       image=prev_img, bg='black', borderwidth=0, command=play_prev)
prevButton.config(bg="systemTransparent")
prevButton.pack(pady=15, in_=top, side='left')

stopButton = tk.Button(canvas, text="Stop",
                       image=stop_img, bg='black', borderwidth=0, command=stop)
stopButton.pack(pady=15, in_=top, side='left')


playButton = tk.Button(canvas, text="Prev",
                       image=play_img, bg='black', borderwidth=0, command=select)
playButton.pack(pady=15, in_=top, side='left')

pauseButton = tk.Button(canvas, text="Stop",
                        image=pause_img, bg='black', borderwidth=0, command=pause_song)
pauseButton.pack(pady=15, in_=top, side='left')


nextButton = tk.Button(canvas, text="Stop",
                       image=next_img, bg='black', borderwidth=0, command=play_next)
nextButton.pack(pady=15, in_=top, side='left')


for root, dirs, files in os.walk(rootpath):
    for filename in fnmatch.filter(files, pattern):
        listBox.insert('end', filename)

canvas.mainloop()
