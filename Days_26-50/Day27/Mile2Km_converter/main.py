import tkinter

window = tkinter.Tk()
#if you would use "from tkinter import *" then you can write in the line above window = Tk()
window.title("My very first GUI")
window.minsize(width=500, height=300)
#window.config(pad=100,pady=200) #adding padding gives more space from the window border

#Label
my_label = tkinter.Label(text="I am a Label", font=("Ariel", 24, "bold"))

#my_label.pack(side="left") # notice if there is side= left added then button is first before label because of pack()
# but there is also place(x=0,y=0) or grid(column=5,row=5)-but it will be placed at 0,0 if there is no column=4 or 1 taken
# DON'T MIX PACK WITH PLACE OR GRID !!
my_label.pack()
#The other methods to write the label
#my_label["text"] = "New Text"
#my_label.config(text="New Text1")

#Button
def button_clicked():

    return my_label.config(text=input.get())

button = tkinter.Button(text="Click me", command=button_clicked)
button.pack()

#Entry
input = tkinter.Entry(width=15)
input.pack()
#input.config(padx=100, pady=200)


window.mainloop()
