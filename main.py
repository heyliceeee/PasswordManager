from tkinter import *
import os
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"

IMAGE = "/data/logo.png"
dir_path = os.path.dirname(os.path.abspath(__file__)) # get the path of the current file

def generate_password():
    """
    generate a random password
    """
    pass
def add():
    """
    save a new credential to the file
    """
    with open(dir_path + "/data/credentials.txt", "a") as file:
        file.write(f"{input_website.get()} | {input_email_username.get()} | {input_password.get()}\n")

    # clear the text box
    input_website.delete(0, END)
    input_password.delete(0, END)

# UI setup
def create_window():
    """
    create a window, set a title, set the size, and set the padding
    """
    window.title("Password Manager") # set the title of the window
    window.config(padx=50, pady=50)  # set the padding of the window
def create_labels():
    """
    create the labels, set the text, and place them on the screen
    """
    website_label = Label(text="Website ") # create a label
    website_label.grid(column=0, row=1) # place the label on the screen

    email_username_label = Label(text="Email/Username ") # create a label
    email_username_label.grid(column=0, row=2) # place the label on the screen

    password_label = Label(text="Password ") # create a label
    password_label.grid(column=0, row=3) # place the label on the screen
def create_canvas():
    """
    create a canvas
    """
    global canvas
    img = PhotoImage(file=dir_path + IMAGE) # create an image

    canvas = Canvas(width=200, height=200, highlightthickness=0) # create a canvas
    canvas.img = img # assign the image to a variable
    canvas.create_image(100, 100, image=img) # place the image
    canvas.grid(column=1, row=0)  # place the canvas
def create_btns():
    """
    create the buttons, set the text, and place them on the window
    """
    generate_password_btn = Button(text="Generate Password", command=generate_password, highlightthickness=0) # create the button
    generate_password_btn.grid(column=2, row=3) # place the button on the window

    add_btn = Button(width=36, text="Add", command=add, highlightthickness=0) # create the button
    add_btn.grid(column=1, row=4, columnspan=2) # place the button on the window
def create_textbox():
    """
    create a text box, set the text, and place it on the screen
    """
    input_website.grid(column=1, row=1, columnspan=2)
    input_website.focus() # set the focus to the text box

    input_email_username.grid(column=1, row=2, columnspan=2)
    input_email_username.insert(0, "alice@mail.com")

    input_password.grid(column=1, row=3)

window = Tk() # create a window
create_window() # call the function to create the window

create_labels() # call the function to create the labels
create_canvas() # call the function to create the canvas
create_btns() # call the function to create the buttons

input_website = Entry(width=38) # create a text box
input_email_username = Entry(width=38) # create a text box
input_password = Entry(width=21) # create a text box
create_textbox() # call the function to create the textbox

window.mainloop() # continuously run the program