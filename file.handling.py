# file handling task

from tkinter import *

#Renaming tkinter and changing miscellaneous window data
root = Tk()
root.title("Text Files")
root.geometry('600x500')
root.configure(bg='red')

#This class contains the program
class page:
    def __init__(self):
        #creating label and textbox
        heading = Label(root, text="My new page", font=('Helvetica', 20), bg='red')
        self.display_text = Text(root, height=16, width=60,borderwidth=0, bg='red')
        self.display_text.config(highlightbackground="blue")
        self.box = Text(root, height=7, width=60)

        #creating buttons
        create_btn = Button(root, text="Create textfile", command=self.create)
        display_btn = Button(root, text="Display", command=self.display)
        append_btn = Button(root, text="Append data", command=self.append)
        clear_btn = Button(root, text="Clear", command=self.clear)
        exit_btn = Button(root, text="Exit", command=root.destroy)

        #label and text placements
        heading.place(x=50, y=50)
        self.display_text.place(x=50, y=280)
        self.box.place(x=50, y=90)

        #button placements
        create_btn.place(x=45,y=235)
        display_btn.place(x=175,y=235)
        append_btn.place(x=260,y=235)
        clear_btn.place(x=380,y=235)
        exit_btn.place(x=450,y=235)


    #Modules(functions) for the buttons' instructions after clicked
    def create(self):
        f=open("page.txt", "w+")
        f.write(self.box.get("1.0", END))
        f.close()

    def display(self):
        f=open("page.txt", "r+")
        self.display_text.insert(END, f.read())

    def append(self):
        f=open("page.txt", "a+")
        f.write(self.box.get("1.0", END))
        f.close()

    def clear(self):
        self.box.delete("1.0", END)
        self.display_text.delete("1.0", END)


p = page()
root.mainloop()