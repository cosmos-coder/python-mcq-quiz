from tkinter import *



root=Tk()
class first():
        root.geometry('700x700')
        logo1 = PhotoImage(file="quiz789.png")
        w2 = Label(root, image=logo1,width=1000,height=1000).pack(side="right")
        root.title("Registration Form")
        label_0 = Label(root, text="Registration form for Quiz",width=30,font=("bold", 20),fg="white",bg="black")
        label_0.place(x=90,y=53)


        label_1 = Label(root, text="FullName",width=20,font=("Times",10,"bold"),fg="green",bg="yellow")
        label_1.place(x=85,y=130)

        entry_1 = Entry(root)
        entry_1.place(x=240,y=130)
        
        label_2= Label(root, text="Registration No:",width=20,font=("Times",10,"bold"),fg="green",bg="yellow")
        label_2.place(x=85,y=170)

        entry_2 = Entry(root)
        entry_2.place(x=240,y=170)

        label_3 = Label(root, text="DOB",width=20,font=("Times",10,"bold"),fg="green",bg="yellow")
        label_3.place(x=83,y=210)

        entry_3 = Entry(root)
        entry_3.place(x=240,y=210)

        label_4 = Label(root, text="Gender",width=20,font=("Times",10,"bold"),fg="green",bg="yellow")
        label_4.place(x=83,y=250)

        var = IntVar()
        Radiobutton(root, text="Male",padx = 5, variable=var, value=1).place(x=235,y=250)
        Radiobutton(root, text="Female",padx = 20, variable=var, value=2).place(x=290,y=250)

        label_5 = Label(root, text="Branch",width=18,font=("Times",10,"bold"),fg="green",bg="yellow")
        label_5.place(x=83,y=290)

        list1 = ['Computer Science','Electronics','Mechanical','Electrical','Automobile Eng','Civil'];
        c=StringVar()
        d=OptionMenu(root,c, *list1)
        d.config(width=18)
        c.set("select your Branch")
        d.place(x=240,y=290)
  
        label_4 = Label(root, text="level",width=20,font=("Times",10,"bold"),fg="green",bg="yellow")
        label_4.place(x=83,y=330)
        def amir():
                import easy.py
        def saurabh():
                import average.py
        def aditya():
                import HARD.py
        
        Button(root, text='Submit and Start Quiz in easy mode',command=amir,  width=30,bg='brown',fg='white').place(x=180,y=380)
        
        Button(root, text='Submit and Start Quiz in average mode',command=saurabh, width=30,bg='brown',fg='white').place(x=180,y=410)
        


        Button(root, text='Submit and Start Quiz in hard mode',command=aditya, width=30,bg='brown',fg='white').place(x=180,y=440)
        


root.mainloop()
