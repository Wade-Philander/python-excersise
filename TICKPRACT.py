from tkinter import *

window = Tk()  #Make a window
window.geometry("500x500")
window.title("Changing Text")

enter = Entry(window, width=20)      #Entry is a widget to use in the window

label = Label(window, text="Label")     #how to make a label


def change():                                   # (function) was whatever i name it, also def
    label.config(text=enter.get())                                        

button = Button(window, text="Button", command=change) 




enter.grid(row=0, column=0)                                # will allow the winow to have a format
label.grid(row=5, column=2)                                # Will place the label in the window using grid
button.grid(row=6, column=4)                               # allow the button to show in window
window.mainloop()                           # Make Tk run by looping the window constantly