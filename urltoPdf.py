# Import Module
from ctypes import alignment
from tkinter import *
from tkinter import font
from selenium import webdriver
import pdfkit
from wonder import *
# create root window
root = Tk()
root.option_add('*Font', '80')
# root window title and dimension
root.title("Url convertor")
# Set geometry(widthxheight)
root.geometry('1300x1000')

# adding a label to the root window
lbl = Label(root, text = "Enter the URL")
lb2 = Label(root, text = "Python automation to convert website to PDF",fg='red')
lbl.grid()

# adding Entry Field
txt = Entry(root, width=90)
txt.grid(column =1, row =0)


# function to display user text when
# button is clicked
def clicked():
    fun(txt.get())

# button widget with red color text inside
btn = Button(root, text = "Click me" ,
			fg = "red", command=clicked)
# Set Button Grid
btn.grid(column=2, row=0)
lb2.grid()
# Execute Tkinter
root.mainloop()
