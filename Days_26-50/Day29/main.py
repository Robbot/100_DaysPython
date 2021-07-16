from tkinter import *
import math

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=100, pady=50, bg="#FFFFFF")

canvas = Canvas(width=200, height=224, bg="#FFFFFF", highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 112, image=logo_img)
canvas.grid(column=2, row=2, padx=2, pady=2)

window.mainloop()