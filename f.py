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
    aLabel=ttk.Label(win1,  text="Date")
    aLabel.grid(column=0,  row=4)
    aLabel=ttk.Label(win1,  text="Time")
    aLabel.grid(column=0,  row=6)
    aLabel=ttk.Label(win1,  text="Remainder on:")
    aLabel.grid(column=0,  row=8)
#adding textbox 
    number=tk.StringVar()
    number=ttk.Entry(win1,  width=12,  textvariable=number)
    number.grid(column=2,  row=2)
    Date=tk.StringVar()
    Date=ttk.Entry(win1, width=12,  textvariable=Date)
    Date.grid(column=2,  row=4)
    aLabel=ttk.Label(win1,  text="Format: yyyy-mm-dd")
    aLabel.grid(column=4,  row = 4)
    Time=tk.StringVar()
    Time=ttk.Entry(win1,  width=12,  textvariable=Time)
    Time.grid(column=2,  row=6)
    aLabel=ttk.Label(win1,  text="Format: hh:mm:ss")
    aLabel.grid(column=4, row=6)
    rem=tk.StringVar()
    rem=ttk.Entry(win1,  width=12,  textvariable=rem)
    rem.grid(column=2,  row=8)
    
#function
    def mf():
        unum1=number.get()
        name1=Date.get()
        t1=Time.get()
        r1=rem.get()
        conn=sqlite3.connect("Remainder.db")
        cur=conn.cursor()
    #cur.execute("SELECT * FROM FRUIT WHERE unum = ?", (unum1))
    #rows=cur.fetchall()
    #for column in rows:
        #print(column)
        #cur.execute("CREATE TABLE REMAINDER(number INTEGER PRIMARY KEY, Date TEXT, Time TEXT, rem TEXT);")
        cur.execute("INSERT INTO REMAINDER(number, Date, Time, rem)VALUES(?, ?, ?, ?);", (unum1,  name1,  t1,  r1) )
        number.bind('<Return>',  mf) 
        Date.bind('<Return>',  mf)
        Time.bind('<Return>',  mf)
        rem.bind('<Return>',  mf)
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
    aLabel=ttk.Label(win2,  text="Date")
    aLabel.grid(column=0,  row=4)
    aLabel=ttk.Label(win2,  text="Time")
    aLabel.grid(column=0,  row=6)
    aLabel=ttk.Label(win2,  text="Remainder on:")
    aLabel.grid(column=0,  row=8)
#adding textbox 
    number=tk.StringVar()
    number=ttk.Entry(win2,  width=12,  textvariable=number)
    number.grid(column=2,  row=2)
    Date=tk.StringVar()
    Date=ttk.Entry(win2, width=12,  textvariable=Date)
    Date.grid(column=2,  row=4)
    aLabel=ttk.Label(win2,  text="Format: yyyy-mm-dd")
    aLabel.grid(column=4,  row = 4)
    Time=tk.StringVar()
    Time=ttk.Entry(win2,  width=12,  textvariable=Time)
    Time.grid(column=2,  row=6)
    aLabel=ttk.Label(win2,  text="Format: hh:mm:ss")
    aLabel.grid(column=4, row=6)
    rem=tk.StringVar()
    rem=ttk.Entry(win2,  width=12,  textvariable=rem)
    rem.grid(column=2,  row=8)
#function
    def ef():
        unum1=number.get()
        name1=Date.get()
        t1=Time.get()
        r1=rem.get()
    #name1=name.get()
        conn=sqlite3.connect("Remainder.db")
        cur=conn.cursor()
        cur.execute("UPDATE REMAINDER SET Date=?, Time=?, rem=? WHERE number=?", (name1, t1,  r1,   unum1))#name2,  t2,  r2
        number.bind('<Return>', ef)
        Date.bind('<Return>',  ef)
        Time.bind('<Return>',  ef)
        rem.bind('<Return>',  ef)
        conn.commit()
        conn.close()
        print(conn)
        
        messagebox.showinfo("Confirmation", "Remainder Updated"  )
    #name.bind('<Return>', ef)
#button
    action=ttk.Button(win2,  text="Update",  command=ef)
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
action=ttk.Button(win,  text="Update Remainder",  command=df)
action.grid(column=0,  row=2)
#Button3
action=ttk.Button(win,  text="View Remainder",  command=vf)
action.grid(column=0,  row=4)
win.mainloop()
