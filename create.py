import tkinter as tk
import sqlite3
from tkinter import  ttk
from tkinter import  messagebox
win1=tk.Tk()
#adding a label
aLabel=ttk.Label(win1,  text="number")
aLabel.grid(column=0,  row=2)
#adding another label
aLabel=ttk.Label(win1,  text="date")
aLabel.grid(column=0,  row=4)
#adding textbox 
number=tk.StringVar()
number=ttk.Entry(win1,  width=12,  textvariable=number)
number.grid(column=2,  row=2)
date=tk.StringVar()
date=ttk.Entry(win1, width=12,  textvariable=date)
date.grid(column=2,  row=4)
#function
def mf():
    unum1=number.get()
    name1=date.get()
    
    conn=sqlite3.connect("Remainder.db")
    cur=conn.cursor()
    #cur.execute("SELECT * FROM FRUIT WHERE unum = ?", (unum1))
    #rows=cur.fetchall()
    #for column in rows:
        #print(column)
    #cur.execute("CREATE TABLE REMAINDER(number INTEGER PRIMARY KEY, date TEXT UNIQUE);")
    cur.execute("INSERT INTO REMAINDER(number, date)VALUES(?, ?);", (unum1,  name1) )
    number.bind('<Return>',  mf) 
    date.bind('<Return>',  mf)
    conn.commit()
    conn.close() 
    print(conn)
    #messagebox.showwarning("Warning",  "Fruit exists")
    messagebox.showinfo("Validation", "Remainder Set")
#adding button
action=ttk.Button(win1, text="OK",  command=mf)
action.grid(column=10, row=10)
win1.mainloop()
