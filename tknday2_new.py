import tkinter as tk
from tkinter import messagebox
from functools import partial 



window = tk.Tk()
window.title("Temperature Converter")
window.geometry("500x200")


temp = "Celsius"

def call_convert(a, b):
    temp2 = input_entry.get()

    if temp =="Celsius":
        x = (float(temp2) * 9/5)+ 32
        result_label.config(text ="%.if Fahrenheit" % x)

    if temp == "Fahrenheit":
        y = float((temp2) - 32) * 5 / 9
        result_label.config(txt ="%.if Celsius" % y)
        
    return

def store_temp(set_temp): 
    global temp2
    temp2 = set_temp 

window.grid_columnconfigure(1, weight = 0) 
window.grid_rowconfigure(1, weight = 0) 

inputNumber = tk.StringVar() 
var = tk.StringVar() 

input_label = tk.Label(window, text ="Enter temperature") 
input_entry = tk.Entry(window, textvariable = inputNumber) 
input_label.grid(row = 0, column = 1)
input_entry.grid(row = 1, column = 1) 
result_label = tk.Label(window) 
result_label.grid(row = 3, column = 1) 

# drop down setup 
dropDownList = ["Celsius", "Fahrenheit"] 
drop_down = tk.OptionMenu(window, var, *dropDownList, 
                          command = store_temp) 
var.set(dropDownList[0]) 
drop_down.grid(row = 2, columnspan = 1) 
  
# button widget 
call_convert = partial(call_convert, result_label, 
                       inputNumber) 
result_button = tk.Button(window, text ="Convert", 
                          command = call_convert) 
result_button.grid(row = 2, column = 3) 
  
# infinite loop which is required to 
# run tkinter program infinitely 
# until an interrupt occurs 

window.mainloop()



