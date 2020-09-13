##### IMPORTS ####

import random, os, time
import mutagen
from mutagen.mp3 import MP3
import tkinter as tk
from tkinter import filedialog, Text

##### FRONT END AND BACK END ####

root = tk.Tk()
dires = []
paths = dires

def randSong():
	global paths
	random_path = (random.choice(paths))
	files = os.listdir(random_path)
	d = random.choice(files)
	selectedsong = (random_path + "\\" + d)
	print("//////////////////////////////////////////")
	print(random_path)
	print(files)
	print(selectedsong)
	print("//////////////////////////////////////////")
	os.startfile(selectedsong)

def looprandsong():
	global paths
	random_path = (random.choice(paths))
	files = os.listdir(random_path)
	d = random.choice(files)
	selectedsong = (random_path + "\\" + d)
	audio_info = MP3(selectedsong).info
	selectedsongtime = int(audio_info.length)
	print("//////////////////////////////////////////")
	print(random_path)
	print(files)
	print(str(selectedsongtime) + " seconds in duration")
	print(selectedsong)
	print("//////////////////////////////////////////")
	os.startfile(selectedsong)
	time.sleep(selectedsongtime)
	looprandsong()

def addFolder():

	for widget in frame.winfo_children():
		widget.destroy()

	filename = filedialog.askdirectory()
	dires.append(filename)
	print(filename)
	for dire in dires:
		label = tk.Label(frame, text=dire, bg="gray").pack()


canvas = tk.Canvas(root, height=400, width=400, bg="#263D42")
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

openFile = tk.Button(root, text="Open File", padx=10, pady=5, fg="white", bg="#263D42", command=addFolder)
openFile.pack()

randomSong = tk.Button(root, text="Random Song", padx=10, pady=5, fg="white", bg="#263D42", command=randSong)
randomSong.pack()

root.mainloop()

