import json
from pathlib import Path
from tkinter import *
from tkinter import messagebox
import os
from random import choice, randint, shuffle
import pyperclip
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SYMBOLS = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
IMAGE = "/data/logo.png"
dir_path = os.path.dirname(os.path.abspath(__file__)) # get the path of the current file

def generate_password():
    """
    generate a random password
    """
    password_letters = [choice(LETTERS) for _ in range(randint(8, 10))] # generate a random password of 8 to 10 letters
    password_symbols = [choice(SYMBOLS) for _ in range(randint(2, 4))] # generate a random password of 2 to 4 symbols
    password_numbers = [choice(NUMBERS) for _ in range(randint(2, 4))] # generate a random password of 2 to 4 numbers

    password_list = password_letters + password_symbols + password_numbers # combine the lists
    shuffle(password_list) # shuffle the list

    password = "".join(password_list) # convert the list to a string
    input_password.insert(0, password) # insert the password into the text box
    pyperclip.copy(password) # copy the password to the clipboard
def add():
    """
    save a new credential to the file
    """
    website = input_website.get()
    email_username = input_email_username.get()
    password = input_password.get()
    new_data = {
        website: {
            "email/username": email_username,
            "password": password
        }
    }

    if len(website) == 0 or len(password) == 0: # if you have an empty website or password, display a warming message
        messagebox.showinfo("Empty field", "Please make sure you don't have any empty fields.") # show a message box
    else:
        is_ok = messagebox.askokcancel(website, f"There are the details entered: \nEmail/Username: {email_username}\nPassword: {password}\nIs it ok to save?") # show a message box

        if is_ok: # if the user clicks ok, save the credential to the file
            try:
                with open(dir_path + "/data/credentials.json", "r") as file: # read the file
                    data = json.load(file) # load the data from the file

            except FileNotFoundError:
                with open(dir_path + "/data/credentials.json", "w") as file: # write the file
                    json.dump(new_data, file, indent=4) # save the new_data to the file

            else: # if the file already exists
                data.update(new_data) # update the data with the new data
                with open(dir_path + "/data/credentials.json", "w") as file: # write the file
                    json.dump(data, file, indent=4) # save the new_data to the file

            finally: # always clear the text box
                input_website.delete(0, END)
                input_password.delete(0, END)
def find_password():
    """
    check if there exists a credential for that website, if there does, display the email/username and password
    """
    website = input_website.get().lower()
    email_username = input_email_username.get()

    if len(website) == 0 or len(email_username) == 0: # if you have an empty website or password
        messagebox.showinfo("Empty field", "Please make sure you don't have any empty fields.")
    else:
        try:
            with open(dir_path + "/data/credentials.json", "r") as file: # read the file
                data = json.load(file) # load the data from the file

        except FileNotFoundError:
            messagebox.showinfo(title="No Data File Found", message="Please make sure you have any credential created.")  # show a message box

        else:
            if website in data and email_username in data[website]["email/username"]:  # if there exists a credential
                messagebox.showinfo(title=website, message=f"Email/Username: {data[website]["email/username"]}\nPassword: {data[website]["password"]}") # show a message box

            else:
                messagebox.showinfo(title="No Credential", message="There is no credential for that website.")  # show a message box

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

    search_btn = Button(text="Search", command=find_password, highlightthickness=0, width=13) # create the button
    search_btn.grid(column=2, row=1) # place the button on the window
def create_textbox():
    """
    create a text box, set the text, and place it on the screen
    """
    input_website.grid(column=1, row=1)
    input_website.focus() # set the focus to the text box

    input_email_username.grid(column=1, row=2, columnspan=2)
    input_email_username.insert(0, "alice@mail.com")

    input_password.grid(column=1, row=3)

window = Tk() # create a window
create_window() # call the function to create the window

create_labels() # call the function to create the labels
create_canvas() # call the function to create the canvas
create_btns() # call the function to create the buttons

input_website = Entry(width=21) # create a text box
input_email_username = Entry(width=38) # create a text box
input_password = Entry(width=21) # create a text box
create_textbox() # call the function to create the textbox

window.mainloop() # continuously run the program