from tkinter import *  

root =Tk()

def leftClick(Event):
    print("Left")

def rigtClick(Event):
    print("Right")

def middleClick(Event):
    print("Middle")

frame = Frame(root, width=300, height=250)
frame.bind("<Button-1>",leftClick)
frame.bind("<Button-2>",middleClick)
frame.bind("<Button-3>",rigtClick)
frame.pack()

root.mainloop()
