
from tkinter import *
from tkinter import messagebox as mb
'''
class sick:
    def __init__(self):
        pass

class influenza(sick):
    def __init__(self, medication, cons_fee):
        self.medication=medication
        self.cons_fee=cons_fee
    def treat_amount(self, medication, cons_fee):
        if self.cons_fee>600:
            amount=self.medication + (self.cons_fee*0.98)
            print(amount)
        else:
            amount=self.medication + self.cons_fee
            print(amount)

label = tk.Label(window, text ="Sickness Code")

obj_patient=influenza(0,0)
#attributes
obj_patient.medication=350.50
obj_patient.cons_fee=float(input("Please enter consultation fee: "))

#call the method
obj_patient.treat_amount(0,0)

class cancer(sick):
    def __init__(self, medication, scan_fee):
        self.medication=medication
        self.scan_fee=scan_fee

    def treat_amount(self, medication,scan_fee):
        if self.scan_fee>600:
            print("Sorry, Unfortunately we can't treat you.")
        else:
            amount=medication + scan_fee
            print(amount)

'''


from tkinter import *
from tkinter import messagebox as mb


window = Tk()

medFlu = 350
medCan = 400

window.config(bg='light blue')

a = Entry(window, width=20)
b = Entry(window, width=10)
c = Entry(window, width=20)
x = Entry(window, width=20)
y = Label(window, text="Sickness Cod:")
z = Label(window, text="Duration of Treatment:")
dpt = Label(window, text="Dr Practice code:")
fc = Label(window, text="Fee/Consultation:")
wm = Label(window, text="Weeks/Months")
la_w= Label(window)

rvar = StringVar()

def selected_sickness():
    if rvar.get() == "Flu":
        if int(x.get()) >= 600:
            flutot = medFlu + int(x.get())
            la_w.config(text="Total:" + str(flutot))
        if int(x.get()) < 600:
            flutot = medFlu + int(x.get())
            disflu = (flutot * (2/100)) + flutot
            mb.showinfo("message", "you got a discount of 2%")
            la_w.config(text="Total" + str(disflu))
        if rvar.get() == "Cancer":
            if int(x.get()) > 600:
                mb.showinfo("Message", "Sorry, Unfortunately we are not able to treat you")
        if int(x.get()) < 600:
            canTot = int(x.get()) + medCan
            la_w.config(text="Total:" + str(canTot))

def clr():
    la_w.config(text="")
    a.delete("0",END)
    b.delete("0",END)
    c.delete("0",END)
    x.delete("0",END)

def ex():
    window.destroy()

exbtn = Button(window, text="exit", command=ex)
clrbtn = Button(window, text="clear", command=clr)
btn = Button(window, text="Calculate", command=selected_sickness)
radcan = Radiobutton(window, text="Cancer", variable=rvar,value="Cancer")
radin = Radiobutton(window, text="Influenza", variable=rvar, value="Flu")


y.grid(row=0, column=0, sticky=W)
z.grid(row=1, column=0, sticky=W)
fc.grid(row=2, column=0, sticky=W)
dpt.grid(row=3, column=0, sticky=W)
wm.grid(row=1, column=3)
a.grid(row=0, column=1)
b.grid(row=1, column=1)
x.grid(row=2, column=1)
c.grid(row=3, column=1)
radcan.grid(row=4, column=0)
radin.grid(row=5, column=0)
la_w.grid(row=6, column=0)
btn.grid(row=7, column=0)
clrbtn.grid(row=7, column=1)
exbtn.grid(row=7, column=2, sticky=E)


window.mainloop()
