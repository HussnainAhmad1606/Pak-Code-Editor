from tkinter import *

# Functions Start Here

# Create new file function
def newFile():
	pass


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
	fileMenu.add_command(label="Open File", command=newFile)
	fileMenu.add_separator()
	fileMenu.add_command(label="Save", command=newFile)
	fileMenu.add_separator()
	fileMenu.add_command(label="Exit", command=root.destroy)

	mainMenu.add_cascade(label="File", menu=fileMenu)
	root.config(menu=mainMenu)

	# Edit Menu
	editMenu = Menu(mainMenu, tearoff=0)
	editMenu.add_command(label="Undo", command=newFile)
	editMenu.add_command(label="Redo", command=newFile)
	editMenu.add_separator()
	editMenu.add_command(label="Cut", command=newFile)
	editMenu.add_command(label="Copy", command=newFile)
	editMenu.add_command(label="Paste", command=newFile)


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
	editMenu.add_command(label="Visit Website", command=newFile)
	editMenu.add_command(label="Contribute", command=newFile)
	editMenu.add_separator()
	editMenu.add_command(label="Purchase License", command=newFile)
	editMenu.add_command(label="Enter License", command=newFile)
	editMenu.add_separator()
	editMenu.add_command(label="About Pak Text", command=newFile)

	mainMenu.add_cascade(label="Help", menu=editMenu)
	root.config(menu=mainMenu)

	"""
	Menu Ends Here
	"""

	# Side bar where files of the project will be shown
	sideBarFrame = Frame(root, padx=40)
	sideBarFrame.pack(fill=BOTH, side=LEFT)

	label = Label(sideBarFrame, text="Folders", font=("Berlin Sans FB", 30))
	label.pack()

	# Line Numbers to show
	lineNumbers = Text(root, width=5, bg="blue", font=("Cascadia Code", 20))
	lineNumbers.pack(side=LEFT, fill=BOTH)
	lineNumbers.insert("1.0", "1")

	lineNumbers['state'] = 'disabled'
	
	# Text Area where code will be written
	codingArea = Text(root, font=("Cascadia Code", 20))
	codingArea.pack(expand=True, fill=BOTH)

	root.bind("<Return>", addLine)
	root.bind("<BackSpace>", removeLine)
	root.mainloop()