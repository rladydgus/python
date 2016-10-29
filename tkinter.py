from tkinter import *
from tkinter import messagebox

def onclick():
    name=lbl.get()
    messagebox.showinfo('이름', name)
    
win = Tk()
txt = Label(win, text="이름")
txt.grid(row=0, column=0)
lbl = Entry(win)
lbl.grid(row=0, column=1)
btn = Button(win, text="OK", command=onclick)
btn.grid(row=1, column=1)
win.mainloop()
