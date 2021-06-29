import tkinter

window = tkinter.Tk()
window.title("My very first GUI")
window.minsize(width=500, height=300)

#Label
my_label = tkinter.Label(text="I am a Label", font=("Ariel", 24, "bold"))
my_label.pack()


window.mainloop()
