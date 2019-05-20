
from tkinter import *

root = Tk()
root.title("CSOD App")
frame = Frame(root)
frame.grid(row=0, column=0)
frame.config(padx=10, pady=10)

topframe = Frame(root)
topframe.grid(row=0, column=0)

bottomframe = Frame(root)
bottomframe.grid(row=1, column=0)

redbutton = Button(topframe, text="Red", fg="red")
redbutton.grid(row=0, column=0)

greenbutton = Button(topframe, text="Brown", fg="brown")
greenbutton.grid(row=0, column=1)

bluebutton = Button(bottomframe, text="Blue", fg="blue")
bluebutton.grid(row=0, column=0)

blackbutton = Button(bottomframe, text="Black", fg="black")
blackbutton.grid(row=0, column=1)

root.mainloop()
