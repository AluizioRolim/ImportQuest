import tkinter
import sqlite3
import re

window=tkinter.Tk()
window.title("Login Form")
window.geometry('640x440')
#window.configure(bg="#333333")

#creating widgets
login_label = tkinter.Label(window, text="Login")
username_label = tkinter.Label(window, text="Username")
username_entry = tkinter.Entry(window)
password_entry = tkinter.Entry(window, show="*")
password_label = tkinter.Label(window, text="Password")
login_button = tkinter.Button(window, text="Login")

#placing widgets
login_label.grid(row=0, column=0, columnspan=2)
username_label.grid(row=1, column=0)
username_entry.grid(row=1, column=1)
password_label.grid(row=2, column=0)
password_entry.grid(row=2 ,column=1)
login_button.grid(row=3, column=0, columnspan=2)


#label = tkinter.Label(window, text="login")
#label.grid(row=0, column=0)


window.mainloop()

