from tkinter import *
from tkinter.ttk import *
from time import strftime


root = Tk()
root.title("YEAMIN TIMES")

def time():
    string = strftime('%H:%M:%S %p %a')
    label.config(text=string)
    label.after(1000,time)



label = Label(root,font=("ds-digital",80), background = "red", foreground = "white")
label.pack(anchor = 'center')
time()


mainloop()