import tkinter as tk
from tkinter import ttk
import sqlite3
from tkinter import  messagebox
#window creation
win=tk.Tk()
#function1
def af():
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
    #cur.execute("CREATE TABLE FRUIT(unum INTEGER PRIMARY KEY, name TEXT UNIQUE);")
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
#function2
def df():
    win2=tk.Tk()
    #label
    aLabel=ttk.Label(win2,  text="number")
    aLabel.grid(column=0, row=2)
#textbox
    number=tk.StringVar()
    number=ttk.Entry(win2,  width=12,  textvariable=number)
    number.grid(column=2,  row=2)
#function
    def ef():
        unum1=number.get()
    #name1=name.get()
        conn=sqlite3.connect("Remainder.db")
        cur=conn.cursor()
        cur.execute("DELETE FROM REMAINDER WHERE number=?", (unum1))
        conn.commit()
        conn.close()
        print(conn)
        number.bind('<Return>', ef)
        messagebox.showinfo("Confirmation", "Remainder deleted"  )
    #name.bind('<Return>', ef)
#button
    action=ttk.Button(win2,  text="Delete",  command=ef)
    action.grid(column=12,  row=12)
    win2.mainloop()
#function3
def vf():
    win3=tk.Tk()
    aLabel=ttk.Label(win3,  text="number")
    aLabel.grid(column=0, row=0)
#textbox
    number=tk.StringVar()
    number=ttk.Entry(win3, width=12,  textvariable=number)
    number.grid(column=2,  row=0)
#function gf
    def gf():
        unum1=number.get()
    #name1=name.get()
        conn=sqlite3.connect("Remainder.db")
        cur=conn.cursor()
        cur.execute("SELECT * FROM REMAINDER WHERE number = ?", (unum1))
        for row in cur.fetchall():
            s=row
        number.bind('<Return>',  gf)
    #name.bind('<Return>',  gf)
        conn.commit()
        conn.close()
        print(conn)
        aLabel=ttk.Label(win3,  text=s)
        aLabel.grid(column=4, row=4)
#button
    action=ttk.Button(win3,  text="View",  command=gf)
    action.grid(column=12,  row=12)
    win3.mainloop()
#Button1
action=ttk.Button(win,  text="Create Remainder",  command=af)
action.grid(column=0,  row=0)
#Button2
action=ttk.Button(win,  text="Delete Remainder",  command=df)
action.grid(column=0,  row=2)
#Button3
action=ttk.Button(win,  text="View Remainder",  command=vf)
action.grid(column=0,  row=4)
win.mainloop()
