from tkinter import *

root=Tk()

def saved():
    txt=textbox.get('1.0', END+'-1c')
    fp = open('txt.txt','w')
    fp.write(txt)
    fp.close()

textbox=Text(root)
textbox.grid(row=0, column=0)

btn=Button(root, text="Save", command=saved)
btn.grid(row=1, column=0)

root.mainloop()
