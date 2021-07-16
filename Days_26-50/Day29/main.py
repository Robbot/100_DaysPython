from tkinter import *
import math

FONT_NAME = "Ariel"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    pass

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_password():
    pass


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=224)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 112, image=logo_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website: ", font=(FONT_NAME, 10))
website_label.grid(column=0, row=1, sticky=E)
email_label = Label(text="Email/Usernaname: ", font=(FONT_NAME, 10))
email_label.grid(column=0, row=2,sticky=E)
password_label = Label(text="Password:", font=(FONT_NAME, 10))
password_label.grid(column=0, row=3,)

button1 = Button(text="Generate Password", command=generate_password, highlightthickness=0)
button1.grid(column=2, row=3)
button2 = Button(text="Add", command=add_password, highlightthickness=0, width=36)
button2.grid(column=1, row=4, columnspan=2)

website_entry = Entry(width=35)
website_entry.grid(column=1, row=1,  columnspan=2)
email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2)
pass_entry = Entry(width=17)
pass_entry.grid(column=1, row=3)

window.mainloop()