import tkinter
from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("Choose your beverage")
window.geometry("300x200")

def submit_action():
    messagebox_text =""
    if c_var.get():
        message_text +="You have chosen Coffee \n"
    if l_var.get():
        message_text +="You have chosen Fred \n"
    if g_var.get():
        message_text +="You have chosen Milk \n"
    if p_var.get():
        message_text +="You have chosen Mushroom \n"
    if message_text =="":
        message_text = "Don't you smaak a drink?"
    messagebox.showinfo("Chose a drink on me bro", message_text)

submit_button = Button(window, text="Submit", command=submit_action)

c_var = BooleanVar()
l_var = BooleanVar()
g_var = BooleanVar()
p_var = BooleanVar()

coffee_cb = Checkbutton(window, text="Coffee", variable=c_var, onvalue=True, offvalue=False, width=20, height=2)
Fred_cb = Checkbutton(window, text="Fred", variable=l_var, onvalue=True, offvalue=False, width=20, height=2)
Milk_cb = Checkbutton(window, text="Milk", variable=g_var, onvalue=True, offvalue=False, width=20, height=2)
Mushrooms_cb = Checkbutton(window, text="Mushroom", variable=p_var, onvalue=True, offvalue=False, width=20, height=2)

coffee_cb.pack()
Fred_cb.pack()
Milk_cb.pack()
Mushrooms_cb.pack()

submit_button.pack()
window.mainloop()
