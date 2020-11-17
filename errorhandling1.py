from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("500x500")
root.title("Error Handling")


def verify():
    user_password1 = {"jack": "111", "fred": "222", "jeff": "333", "sam": "555", "naomi": "888", "sarah": "444"}
    username = myentry1.get()
    password = myentry2.get()

    if (username, password) in user_password1.items():
        messagebox.showinfo("Checks", "Correct Login")
        window = Tk()


        def status():
            window = Tk()
            window.geometry("500x500")
            window.title("Error Handling")

        label3 = Label(window, text="Please enter amount in your account")
        label3.pack()
        entry3 = Entry(window)
        entry3.pack()

        def checkm():
            if int(entry3.get()) >= 3000:
                messagebox.showinfo("my status", "You qualify for the Malaysia trip. Congratulations. ")
            else:
                messagebox.showinfo("My status" , "Please deposit more funds for this excursion.")

        button3 = Button(window, text="Check Qualification", command=checkm)
        button3.pack()


        myb = Button(window, text="check status", command=status)
        myb.pack()
        window.mainloop()

    else:
        messagebox.showinfo("Checks", "incorrect Login, please try again")


label1 = Label(root, text="Enter username")
label1.pack()
myentry1 = Entry(root, textvariable="username")
myentry1.pack()
myentry1.pack()
label2 = Label(root, text="Enter password")
label2.pack()
myentry2 = Entry(root, textvariable="password", show="*")
myentry2.pack()

mycheck = Button(root, text="Check", command=verify)
mycheck.pack()
root.mainloop()