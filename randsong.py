##### IMPORTS ####

import random, os, time
import mutagen
from mutagen.mp3 import MP3
import tkinter as tk
from tkinter import filedialog, Text, messagebox

##### FRONT END AND BACK END ####

root = tk.Tk()
dires = []

def randSong():
	global dires
	if dires == []:
		tk.messagebox.showerror(title="Error", message="click open file and select a folder")
	else:
		random_path = (random.choice(dires))
		files = os.listdir(random_path)
		d = random.choice(files)
		selectedsong = (random_path + "\\" + d)
		print(random_path)
		print(selectedsong)
		print("//////////////////////////////////////////")
		os.startfile(selectedsong)

def looprandsong():	# not current being used in program
	global dires
	random_path = (random.choice(dires))
	files = os.listdir(random_path)
	d = random.choice(files)
	selectedsong = (random_path + "\\" + d)
	audio_info = MP3(selectedsong).info
	selectedsongtime = int(audio_info.length)
	print(random_path)
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

	if len(dires) < 1:
		dires.remove()

	for dire in dires:
		label = tk.Label(frame, text=dire, bg="gray").pack()

def clearFolders():
	global dires
	if dires == []:
		tk.messagebox.showerror(title="Error", message="folder list is already empty")
	dires = []
	for widget in frame.winfo_children():
		widget.destroy()


canvas = tk.Canvas(root, height=400, width=400, bg="#263D42").pack()

frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

openFile = tk.Button(root, text="Open File",  fg="white", bg="#263D42", command=addFolder).pack()
randomSong = tk.Button(root, text="Random Song",  fg="white", bg="#263D42", command=randSong).pack()
randomDire = tk.Button(root, text="Clear Files",  fg="white", bg="#263D42", command=clearFolders).pack()

root.mainloop()
