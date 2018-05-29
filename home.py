import tkinter as tk
from tkinter import ttk
#window creation
win=tk.Tk()
win.geometry("300x150")
#function1
def af():
    win1=tk.Tk()
    win1.mainloop()
#function2
def df():
    win2=tk.Tk()
    win2.mainloop()
#function3
def vf():
    win3=tk.Tk()
    win3.mainloop()
#Button1
action=ttk.Button(win,  text="Create Remainder",  command=af)
action.grid(column=0,  row=0)
#Button2
action=ttk.Button(win,  text="Update Remainder",  command=df)
action.grid(column=0,  row=2)
#Button3
action=ttk.Button(win,  text="View Remainder",  command=vf)
action.grid(column=0,  row=4)
win.mainloop()
