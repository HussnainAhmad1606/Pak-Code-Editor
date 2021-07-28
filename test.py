from tkinter import *
from tkinter.messagebox import showinfo
from PIL import Image, ImageTk
from tkinter.filedialog import asksaveasfilename, askopenfilename, askdirectory

import os
import webbrowser
# Functions Start Here

# Visit website function
def openWebsite():
	website = "https://hussnainahmad.com"
	webbrowser.open(website)


# Contribution function
def contribution():
	contribute_page = "https://github.com/HussnainAhmad1606/Pak-Code-Editor"
	webbrowser.open(contribute_page)


# About function
def about():
	showinfo("Pak Code Editor", "A Code editor made for Pakistani Developers by a Pakistani Developer")

def submitFeedback():
	webbrowser.open("https://hussnainahmad.com")

def submitBugReport():
	webbrowser.open("https://hussnainahmad.com")


# copy function
def copy():
	codingArea.event_generate("<<Copy>>")

def cut():
	codingArea.event_generate("<<Cut>>")

def paste():
	codingArea.event_generate("<<Paste>>")

def undo():
	codingArea.event_generate("<<Undo>>")
	print("Undo")

# Create new file function
def newFile():
	global file
	root.title("Untitled - Pak Code Editor")
	codingArea.delete(1.0, END)
	file = None

def openFile():
	global file
	file = askopenfilename(defaultextension=".txt", filetypes=[("All Files", "*.*"),("Python Files", "*.py")])
	if file == "":
		file = None
	else:
		root.title(os.path.basename(file) + " - Pak Code Editor")
		f = open(file, "r")
		codingArea.delete(1.0, END)
		codingArea.insert(1.0, f.read())
		f.close()


def openFolder():
	folder = askdirectory()
	root.title(os.path.basename(folder) + " - Pak Code Editor")
	foldersInFolder = os.listdir(folder)
	print(foldersInFolder)
	folderStr = ""
	for singleFolder in foldersInFolder:
		Label(sideBarFrame, text=singleFolder, font=("Berlin Sans FB", 20)).pack()
		folderStr = folderStr + singleFolder + "\n"
	print(folderStr)
	# folders["text"] = folderStr

def saveFile():
	global file
	if file == None:
		file = asksaveasfilename(initialfile='Untitled.txt', defaultextension=".txt", filetypes=[("All Files", "*.*"),("Text Documents", "*.txt")])
		if file == "":
			file = None

		else:
			# Save as a new file
			f = open(file, "w")
			f.write(codingArea.get(1.0, END))
			f.close()

			root.title(os.path.basename(file) + " - Notepad")
	else:
		# Save the file
		f = open(file, "w")
		f.write(codingArea.get(1.0, END))
		f.close()


def removeLine(event):
	if codingArea.get(1.0, END) == "":
		print("IF")
		lineNumbers.delete(1.0, END)
		lineNumbers.insert("1.0", 1)
		lineNumbers.configure(state='disabled')
	else:
		print("ELSE")
		final_index_string = float(lineNumbers.index(END))-2.0
		final_index = str(final_index_string)
		print(final_index)
		num_of_lines = final_index.split(".")[0]
		line_numbers_string = "\n".join(str(no + 1) for no in range(int(num_of_lines)))
		width = len(str(num_of_lines))
		lineNumbers.configure(state='normal', width=width)
		lineNumbers.delete(1.0, END)
		lineNumbers.insert(1.0, line_numbers_string)
		lineNumbers.configure(state='disabled')

def addLine(event):
	final_index = str(lineNumbers.index(END))
	num_of_lines = final_index.split(".")[0]
	line_numbers_string = "\n".join(str(no + 1) for no in range(int(num_of_lines)))
	width = len(str(num_of_lines))
	lineNumbers.configure(state='normal', width=width)
	lineNumbers.delete(1.0, END)
	lineNumbers.insert(1.0, line_numbers_string)
	lineNumbers.configure(state='disabled')


if __name__ == "__main__":
	root = Tk()
	file = None
	# Title of the software
	root.title("Pak Text Editor")

	# Software Icon
	root.wm_iconbitmap("code.ico")

	# By default, software open in maximum window
	root.state('zoomed')

	# If want to full screen the software
	# root.attributes("-fullscreen", True)

	"""
	Menu Starts Here
	"""

	# Main Menu
	mainMenu = Menu(root)

	# File Menu
	fileMenu = Menu(mainMenu, tearoff=0)
	fileMenu.add_command(label="New File", command=newFile)
	fileMenu.add_command(label="Open File", command=openFile)
	fileMenu.add_separator()
	fileMenu.add_command(label="Open Folder", command=openFolder)
	fileMenu.add_separator()
	fileMenu.add_command(label="Save", command=saveFile)
	fileMenu.add_separator()
	fileMenu.add_command(label="Exit", command=root.destroy)

	mainMenu.add_cascade(label="File", menu=fileMenu)
	root.config(menu=mainMenu)

	# Edit Menu
	editMenu = Menu(mainMenu, tearoff=0)
	editMenu.add_command(label="Undo", command=undo)
	editMenu.add_command(label="Redo", command=newFile)
	editMenu.add_separator()
	editMenu.add_command(label="Cut", command=cut)
	editMenu.add_command(label="Copy", command=copy)
	editMenu.add_command(label="Paste", command=paste)

	mainMenu.add_cascade(label="Edit", menu=editMenu)
	root.config(menu=mainMenu)

	# Preferences Menu
	preferMenu = Menu(mainMenu, tearoff=0)
	preferMenu.add_command(label="Settings", command=newFile)
	preferMenu.add_separator()
	preferMenu.add_command(label="Theme...", command=newFile)

	# Font menu within preferences menu
	fontMenu = Menu(preferMenu, tearoff=0)
	fontMenu.add_command(label="Smaller", command=newFile)
	fontMenu.add_command(label="Larger", command=newFile)
	fontMenu.add_separator()
	fontMenu.add_command(label="Reset", command=newFile)


	preferMenu.add_cascade(label="Font", menu=fontMenu)
	mainMenu.add_cascade(label="Preferences", menu=preferMenu)
	root.config(menu=mainMenu)



	# Edit Menu
	editMenu = Menu(mainMenu, tearoff=0)
	editMenu.add_command(label="Visit Website", command=openWebsite)
	editMenu.add_command(label="Contribute", command=contribution)
	editMenu.add_separator()
	editMenu.add_command(label="Purchase License", command=newFile)
	editMenu.add_command(label="Enter License", command=newFile)
	editMenu.add_separator()
	editMenu.add_command(label="Submit a Feedback", command=submitFeedback)
	editMenu.add_command(label="Submit a Bug Report", command=submitBugReport)
	editMenu.add_separator()
	editMenu.add_command(label="About Pak Text", command=about)

	mainMenu.add_cascade(label="Help", menu=editMenu)
	root.config(menu=mainMenu)

	"""
	Menu Ends Here
	"""


	# Side bar where files of the project will be shown
	sideBarFrame = Canvas(root)
	sideBarFrame.pack(fill=BOTH, side=LEFT)
	folders = Label(sideBarFrame, text="Folders", font=("Berlin Sans FB", 20))
	folders.pack()

	# Coding area scroll bar
	codingScroll = Scrollbar(root)
	codingScroll.pack(fill=BOTH, side=RIGHT)

	# Line Numbers to show
	lineNumbers = Text(root, width=5, font=("Cascadia Code", 20), bg="#476072", fg="white", yscrollcommand=codingScroll.set)
	lineNumbers.pack(side=LEFT, fill=BOTH)
	lineNumbers.insert("1.0", "1")

	lineNumbers['state'] = 'disabled'




	# Text Area where code will be written
	codingArea = Text(root, font=("Cascadia Code", 20), bg="#548CA8", fg="white", cursor="xterm white white", yscrollcommand=codingScroll.set)
	codingArea.pack(expand=True, fill=BOTH)
	codingArea.config(insertbackground="white")

	codingScroll.config(command= codingArea.yview)






	root.bind("<Return>", addLine)
	root.bind("<BackSpace>", removeLine)
	root.mainloop()
