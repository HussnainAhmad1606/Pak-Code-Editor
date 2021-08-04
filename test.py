from tkinter import *
import tkinter
from tkinter.messagebox import showinfo
from PIL import Image, ImageTk
from tkinter import ttk
from tkinter.filedialog import asksaveasfilename, askopenfilename, askdirectory

import os
import webbrowser
# Functions Start Here


# Checking the extension of the file and show type of the file accordingly
def checkFileType(file):
	if file.lower() == "py":
		type = "Python"

	elif file.lower() == "html":
		type = "HTML"

	elif file.lower() == "css":
		type = "CSS"

	elif file.lower() == "js":
		type = "JavaScript"

	elif file.lower() in ["cp", "cpp"]:
		type = "C++"

	elif file.lower() == "cs":
		type = "C#"

	elif file.lower() == "c":
		type = "C"

	elif file.lower() == "txt":
		type = "Plain Text"

	elif file.lower() == "java":
		type = "Java"

	elif file.lower() == "json":
		type = "JSON"

	elif file.lower() == "ts":
		type = "TypeScript"

	fileType.set(type)
	statusBar.update()

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
		# codingArea.delete(1.0, END)
		# codingArea.insert(1.0, f.read())
		tab.delete(1.0, END)
		tab.insert(1.0, f.read())
		f.close()
	fileName = os.path.basename(file)
	fileExtension = fileName.split(".")[1]
	checkFileType(fileExtension)


	


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
	tabName = my_notebook.select()
	print(tabName)
	if tabName:
		textWidget = my_notebook.nametowidget(tabName)
		text = textWidget.get(1.0, END)
	if file == None:
		file = asksaveasfilename(initialfile='Untitled.txt', defaultextension=".txt", filetypes=[("All Files", "*.*"),("Text Documents", "*.txt")])
		if file == "":
			file = None

		else:
			# Save as a new file
			f = open(file, "w")
			f.write(text)
			f.close()

			root.title(os.path.basename(file) + " - Notepad")
	else:
		# Save the file
		print(text)
		f = open(file, "w")
		f.write(text)
		f.close()
		my_notebook.config(text=file)

	# Writing the file type on status bar
	fileName = os.path.basename(file)
	fileExtension = fileName.split(".")[1]
	print(fileExtension)


	checkFileType(fileExtension)


def saveAsFile():
	global file
	file = asksaveasfilename(initialfile='Untitled.txt', defaultextension=".txt", filetypes=[("All Files", "*.*"),("Text Documents", "*.txt")])

	# Save the file
	f = open(file, "w")
	f.write(codingArea.get(1.0, END))
	f.close()

def removeLine(event):
	lineNumber = tab.index(INSERT)
	print(lineNumber.split(".")[1])
	if lineNumber.split(".")[1] == 0:
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

# Add line number upon clicking ENTER
def addLine(event):
	final_index = str(lineNumbers.index(END))
	num_of_lines = final_index.split(".")[0]
	line_numbers_string = "\n".join(str(no + 1) for no in range(int(num_of_lines)))
	width = len(str(num_of_lines))
	lineNumbers.configure(state='normal', width=width)
	lineNumbers.delete(1.0, END)
	lineNumbers.insert(1.0, line_numbers_string)
	lineNumbers.configure(state='disabled')

# Increase font by 2 points
def increaseFont():
	global fontSize
	fontSize += 2
	# codingArea.configure(font=("Cascadia Code", fontSize))
	# lineNumbers.configure(font=("Cascadia Code", fontSize))
	tab.configure(font=("Cascadia Code", fontSize))
	lineNumbers.configure(font=("Cascadia Code", fontSize))


# Decrease font by 2 points
def decreaseFont():
	global fontSize
	fontSize -= 2
	# codingArea.configure(font=("Cascadia Code", fontSize))
	# lineNumbers.configure(font=("Cascadia Code", fontSize))
	lineNumbers.configure(font=("Cascadia Code", fontSize))
	tab.configure(font=("Cascadia Code", fontSize))

# Reset font back to 20 points
def resetFont():
	global fontSize
	fontSize  = 20
	# codingArea.configure(font=("Cascadia Code", fontSize))
	# lineNumbers.configure(font=("Cascadia Code", fontSize))
	tab.configure(font=("Cascadia Code", fontSize))
	lineNumbers.configure(font=("Cascadia Code", fontSize))


# Settings window function
def settings():
	settings = Tk()
	settings.title("Settings - Pak Code Editor")
	settings.geometry("400x400")
	settings.mainloop()



def darkModeOn():
	darkColor = "#2b2a2a"
	secondary = "#292626"
	font = "white"
	
	root.config(bg=darkColor)
	fileMenu.config(fg=font, bg=secondary)	
	editMenu.config(fg=font, bg=secondary)	
	preferMenu.config(fg=font, bg=secondary)	
	themeMenu.config(fg=font, bg=secondary)	
	aboutMenu.config(fg=font, bg=secondary)		
	fontMenu.config(fg=font, bg=secondary)
	sideBarFrame.config(bg=secondary)

	statusBar.config(bg="#1b1b1b")
	linesCols.config(bg=darkColor, fg=font)
	FileTypeStatus.config(bg=darkColor, fg=font)
	
	folders.config(bg=secondary, fg=font)
	tab.config(bg=darkColor, fg=font)
	tab.config(insertbackground="white")



	

def darkModeOff():
	darkColor = "white"
	secondary = "white"
	font = "black"

	root.config(bg=darkColor)
	fileMenu.config(fg=font, bg=secondary)	
	editMenu.config(fg=font, bg=secondary)	
	preferMenu.config(fg=font, bg=secondary)	
	themeMenu.config(fg=font, bg=secondary)	
	aboutMenu.config(fg=font, bg=secondary)		
	fontMenu.config(fg=font, bg=secondary)
	sideBarFrame.config(bg=secondary)
	statusBar.config(bg=secondary)
	folders.config(bg=secondary, fg=font)
	tab.config(bg=darkColor, fg=font)
	tab.config(insertbackground="black")
	linesCols.config(bg=darkColor, fg=font)
	FileTypeStatus.config(bg=darkColor, fg=font)


def position(event):
	print("Running")
	pos = tab.index(tkinter.INSERT).split(".")

	lines = f"Line: {pos[0]}, Column: {pos[1]}"
	statusBarVar.set(lines)
	statusBar.update()

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
	fileMenu.add_separator()
	fileMenu.add_command(label="Open File", command=openFile)
	fileMenu.add_command(label="Open Folder", command=openFolder)
	fileMenu.add_separator()
	fileMenu.add_command(label="Save", command=saveFile)
	fileMenu.add_command(label="Save As..", command=saveAsFile)
	fileMenu.add_separator()
	fileMenu.add_command(label="Close File", command=saveFile)
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
	editMenu.add_separator()
	editMenu.add_command(label="Find", command=newFile)
	editMenu.add_command(label="Replace", command=newFile)
	mainMenu.add_cascade(label="Edit", menu=editMenu)
	root.config(menu=mainMenu)

	# Preferences Menu
	preferMenu = Menu(mainMenu, tearoff=0)
	preferMenu.add_command(label="Settings", command=settings)
	
	preferMenu.add_separator()
	preferMenu.add_command(label="Theme...", command=newFile)

	# Font menu within preferences menu
	fontMenu = Menu(preferMenu, tearoff=0)
	fontMenu.add_command(label="Smaller", command=decreaseFont)
	fontMenu.add_command(label="Larger", command=increaseFont)
	fontMenu.add_separator()
	fontMenu.add_command(label="Reset", command=resetFont)
	# Theme Menu
	themeMenu = Menu(preferMenu, tearoff=0)
	themeMenu.add_command(label="On", command=darkModeOn)
	themeMenu.add_command(label="Off", command=darkModeOff)

	preferMenu.add_cascade(label="Font", menu=fontMenu)
	preferMenu.add_cascade(label="Dark Mode", menu=themeMenu)
	mainMenu.add_cascade(label="Preferences", menu=preferMenu)
	root.config(menu=mainMenu)

	
	# Edit Menu
	aboutMenu = Menu(mainMenu, tearoff=0)
	aboutMenu.add_command(label="Visit Website", command=openWebsite)
	aboutMenu.add_command(label="Contribute", command=contribution)
	aboutMenu.add_separator()
	aboutMenu.add_command(label="Purchase License", command=newFile)
	aboutMenu.add_command(label="Enter License", command=newFile)
	aboutMenu.add_separator()
	aboutMenu.add_command(label="Submit a Feedback", command=submitFeedback)
	aboutMenu.add_command(label="Submit a Bug Report", command=submitBugReport)
	aboutMenu.add_separator()
	aboutMenu.add_command(label="About Pak Text", command=about)

	mainMenu.add_cascade(label="Help", menu=aboutMenu)
	root.config(menu=mainMenu)

	"""
	Menu Ends Here
	"""

	# Status bar
	statusBarVar = StringVar()
	statusBarVar.set("Line: 1, Column: 0")
	fileType = StringVar()
	fileType.set("")
	statusBar =  Frame(root)
	linesCols = Label(statusBar, bg="white", textvariable=statusBarVar)
	linesCols.pack(side=RIGHT, padx=20)
	FileTypeStatus = Label(statusBar, bg="white", textvariable=fileType)
	FileTypeStatus.pack(side=RIGHT, padx=20)
	statusBar.pack(side=BOTTOM, anchor=W, fill=X)

	fileNumber = 1
	# Side bar where files of the project will be shown
	sideBarFrame = Frame(root)
	sideBarFrame.pack(fill=BOTH, side=LEFT)
	folders = Label(sideBarFrame, text="Folders", font=("Berlin Sans FB", 20))
	folders.pack()

	# Line Numbers to show
	fontSize = 20

	lineNumbers = Text(root, width=1, font=("Cascadia Code", fontSize), bg="#476072", fg="white")
	lineNumbers.pack(side=LEFT, fill=BOTH, pady=20)
	lineNumbers.insert("1.0", "1")

	lineNumbers['state'] = 'disabled'

	codingScrollBar = Scrollbar(root)
	codingScrollBar.pack(fill=Y, side=RIGHT)

	my_notebook = ttk.Notebook(root)
	my_notebook.pack()
	tab = Text(my_notebook, font=("Cascadia Code", fontSize), width=400, height=400, yscrollcommand=codingScrollBar.set)
	tab.pack(fill=BOTH, side=LEFT)
	my_notebook.add(tab, text=f"Untitled{fileNumber}")
	fileNumber += 1

	def multiple_yview(*args):
		lineNumbers.yview(*args)
		# codingArea.yview(*args)
		tab.yview(*args)


	# codingScrollBar.config(command=tab.yview)
	codingScrollBar.config(command=multiple_yview)

	

	

	
	# Coding area scroll bar
	# codingScroll = Scrollbar(root)
	# codingScroll.pack(fill=BOTH, side=RIGHT)
	


	



	# Text Area where code will be written
	
	codingArea = Text(root, font=("Cascadia Code", fontSize), bg="#548CA8", fg="white", cursor="xterm white white")
	codingArea.pack(expand=True, fill=BOTH)
	codingArea.config(insertbackground="white")

	scrollbar = Scrollbar(codingArea, orient=VERTICAL, cursor="arrow", command=multiple_yview)
	scrollbar.pack(fill=Y, side=RIGHT)

	# codingScroll.config(command= codingArea.yview)

	
	root.bind("<Return>", addLine)
	root.bind("<BackSpace>", removeLine)
	root.bind("<KeyRelease>", position)
	root.mainloop()
