from tkinter import *
import os
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"

IMAGE = "/data/logo.png"
dir_path = os.path.dirname(os.path.abspath(__file__)) # get the path of the current file

window = Tk() # create a window

# password generator



# save password




# UI setup
def create_window():
    """
    create a window, set a title, set the size, and set the padding
    """
    window.title("Password Manager") # set the title of the window
    window.config(padx=20, pady=20)  # set the padding of the window
def create_canvas():
    """
    create a canvas
    """
    global canvas
    img = PhotoImage(file=dir_path + IMAGE) # create an image

    canvas = Canvas(width=200, height=200, highlightthickness=0) # create a canvas
    canvas.img = img # assign the image to a variable
    canvas.create_image(100, 100, image=img) # place the image
    canvas.grid(column=1, row=1)  # place the canvas

create_window() # call the function to create the window
create_canvas() # call the function to create the canvas
window.mainloop() # continuously run the program