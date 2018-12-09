from tkinter import *
import tkinter.messagebox

root = Tk(className="Cem's")

tkinter.messagebox.showinfo('window Title','Why did you do that?')
answer  = tkinter.messagebox.askquestion("Q1", "Do you want to open me?")

if answer == "yes":
    print("Welkommen!")
else:
    print("See Ya!!")


root.mainloop()