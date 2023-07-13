
from ast import Lambda
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
import os
from PIL import Image, ImageTk
import sqlite3
#username and password generator using python
#the last page displays the email and username and password
bg_color="#0066FF"
#what starts the program+the title
root = tk.Tk()
root.title("Twitter")
root.eval("tk::PlaceWindow . center")
def load_frame2():
    print("Welcome")
#Geometry
root.geometry('645x600')
text = tk.Text(root, height=12)
text.grid(column=0, row=0, sticky='nsew')

#creating the icon
photo = tk.PhotoImage(file = "twitter icon.png")
root.iconphoto(False, photo)
b = tk.Button(root, text = 'Click me !')

#first page
frame1=tk.Frame(root, width=700, height= 500,bg=bg_color)
frame1.grid(row= 0, column=0)
#frame1.pack_propagate(False) this line makes the color wrap around the widget

#first page widget
logo_img= ImageTk.PhotoImage(file="firstframeimage.png")
logo_widget=tk.Label(frame1, image=logo_img )
logo_widget.image = logo_img
logo_widget.pack()
#second page
frame2=tk.Frame(root, width=700, height= 200,bg= "#0066FF" )
frame2.grid(row= 1, column=0)
#text
tk.Label(frame1,
        text = "Hello! welcome to twitter!\n Sign up to now!!!!",
        bg = "#0066FF",
        fg = "white",
        font = ("TkMenuFont",14) ).pack()
#button widget
tk.Button(
    frame1,
    text = "Press to continue",
    font = ("TkHeadingFont", 20),
    bg = "#28393a",
    fg = "white",
    cursor= "hand2",
    activebackground="#badee2",
    activeforeground="black",
    command=lambda:load_frame2()
    
).pack(pady=20)


#Execution of the window.
root.mainloop()
