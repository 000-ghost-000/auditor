from tkinter import *
from tkinter.filedialog import *

def new_file():
    global name
    name = "Untitled"
    text_area.delete(0.0, END)

def save_file(file_name=None):  # Optional argument for file name
    text_content = text_area.get(0.0, END)  # Get text from text area
    if file_name is None:
        file_name = name
    with open(file_name, "w") as f:
        f.write(text_content)

def save_as_file():
    f = asksaveasfile(mode='w', defaultextension=".md")
    if f:  # Check if user selected a file
        text_content = text_area.get(0.0, END)
        f.write(text_content)
        f.close()

def open_file():
    f = askopenfile(mode='r')
    if f:  # Check if user selected a file
        text_content = f.read()
        text_area.delete(0.0, END)
        text_area.insert(0.0, text_content)
        f.close()

root = Tk()
root.title("Aditor")

text_area = Text(root)  # Create the text area widget
text_area.pack()  # Add the text area to the window

menubar = Menu(root)
filemenu = Menu(menubar)

filemenu.add_command(label="New", command=new_file)
filemenu.add_command(label="Open", command=open_file)
filemenu.add_command(label="Save", command=save_file)  # Can optionally pass name
filemenu.add_command(label="Save As", command=save_as_file)
filemenu.add_separator()
filemenu.add_command(label="Quit", command=root.quit)

menubar.add_cascade(label="File", menu=filemenu)
root.config(menu=menubar)

root.mainloop()
