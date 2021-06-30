from tkinter import *


window = Tk()
window.title("Mile to Km Converter")
window.config(padx=10, pady=20)


entry = Entry(width="10")
entry.grid(column=2, row=1, padx=2, pady=2)
label = Label(text="Miles")
label.grid(column=3, row=1, padx=2, pady=2)
label1 = Label(text="is equal to")
label1.grid(column=1, row=2,  padx=2, pady=2)
label2 = Label(text="0")
label2.grid(column=2, row=2,  padx=2, pady=2)
label3 = Label(text="Km")
label3.grid(column=3, row=2,  padx=2, pady=2)
#Button
def action():
    miles = float(entry.get()) * 1.60934
    return label2.config(text=miles)

#calls action() when pressed
button = Button(text="Calculate", command=action)
button.grid(column=2, row=3,  padx=2, pady=2)













window.mainloop()