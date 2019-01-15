from tkinter import *
def sel():
   Label(root, text="Thank you for your Rating",font=("Times",15),fg="maroon2",bg="white").pack()
root = Tk()
root.geometry('1000x1000')
var = IntVar()
logo1 = PhotoImage(file="feedback.png")
w2 = Label(root, image=logo1,width=600,height=500).place(x=190,y=100)
Label(root, text="FEEDBACK FORM",font=("Lucida Handwriting",30),fg="red",bg="white").pack()
Label(root, text="Rate Us For further Development in Quiz Program",font=("Lucida Handwriting",15),fg="blue",bg="white").pack()
label_1 = Label(root, text="Type What You think about us",width=25,font=("Times",15,"bold"),fg="green",bg="yellow")
label_1.place(x=105,y=130)
entry_1 = Entry(root)
entry_1.place(x=420,y=133)
Button(root, text='Submit Feedback',width=20,bg='brown',fg='white').place(x=370,y=160)

R1 = Radiobutton(root, text="ONE STAR",width=10, variable=var, value=1,
                  command=sel,font=("Times",10,"bold"),bg="white",fg="black")
R1.place(x=10,y=10)
R1.pack( anchor = W )

R2 = Radiobutton(root, text="TWO STAR",width=10, variable=var, value=2,
                  command=sel,font=("Times",10,"bold"),bg="white",fg="black")
R2.place(x=10,y=20)
R2.pack( anchor = W )
R3 = Radiobutton(root, text="THREE STAR",width=10, variable=var, value=3,
                  command=sel,font=("Times",10,"bold"),bg="white",fg="black")
R3.place(x=10,y=10)
R3.pack( anchor = W )
R4 = Radiobutton(root, text="FOUR STAR",width=10, variable=var, value=4,
                  command=sel,font=("Times",10,"bold"),bg="white",fg="black")
R4.place(x=10,y=10)
R4.pack( anchor = W )
R5 = Radiobutton(root, text="FIVE STAR",width=10, variable=var, value=5,
                  command=sel,font=("Times",10,"bold"),bg="white",fg="black")
R5.place(x=10,y=10)
R5.pack( anchor = W )


label = Label(root)
label.pack()
root.mainloop()
