from tkinter import Tk, Frame, Label, Button, PhotoImage
from time import sleep

class Question():
    def __init__(self, question, answers, correctLetter):
        self.question = question
        self.answers = answers
        self.correctLetter = correctLetter

    def check(self, letter, view):
        global right
        global marks
        if(letter == self.correctLetter):
            label = Label(view, text="Right!",font=("Times",20),fg="maroon1",bg="white")
            right += 1
            marks +=1
        else:
            label = Label(view, text="Wrong!",font=("Times",20),fg="maroon1",bg="white")
        label.pack()
        view.after(1000, lambda *args: self.unpackView(view))


    def getView(self, window):
        view = Frame(window)
        Label(view, text=self.question,font=("Times",15),fg="red",bg="white").pack()
        Button(view, text=self.answers[0], command=lambda *args: self.check("A", view),width=40,font=("Times",10,"bold"),fg="green",bg="yellow").pack()
        Button(view, text=self.answers[1], command=lambda *args: self.check("B", view),width=40,font=("Times",10,"bold"),fg="green",bg="yellow").pack()
        Button(view, text=self.answers[2], command=lambda *args: self.check("C", view),width=40,font=("Times",10,"bold"),fg="green",bg="yellow").pack()
        Button(view, text=self.answers[3], command=lambda *args: self.check("D", view),width=40,font=("Times",10,"bold"),fg="green",bg="yellow").pack()
        return view

    def unpackView(self, view):
        view.pack_forget()
        askQuestion()

def askQuestion():
    global questions, window, index, button, right, number_of_questions,marks 
    if(len(questions) == index + 1):
        Label(window, text="Thank you for answering the questions. " + str(right) + " of " + str(number_of_questions) + " questions answered right \n Your Total Score :"+str(marks),font=("Times",15),fg="maroon1",bg="white").pack()
        return
    button.pack_forget()
    index += 1
    questions[index].getView(window).pack()

questions = []
file = open("Hard.txt", "r")
line = file.readline()
while(line != ""):
    questionString = line
    answers = []
    for i in range (4):
        answers.append(file.readline())

    correctLetter = file.readline()
    correctLetter = correctLetter[:-1]
    questions.append(Question(questionString, answers, correctLetter))
    line = file.readline()
file.close()
index = -1
right = 0
marks=0
number_of_questions = len(questions)


window = Tk()
window.geometry('1000x1000')
logo1 = PhotoImage(file="difficult.png")
w2 = Label(window, image=logo1,width=700,height=200).pack(side="top")
logo = PhotoImage(file="difficult1.png")
w1 = Label(window, image=logo,width=150,height=200).pack(side="right")
logo2 = PhotoImage(file="difficult1.png")
w3 = Label(window, image=logo2,width=150,height=200).pack(side="left")





label= Label(window, text="Welcome To Online Python Quiz",justify="left",width="150",height="2",font=("Lucida Handwriting",20),fg="medium blue",bg="white")
label.pack()
label= Label(window, text="Instructions",width="150",height="2",font=("Lucida Handwriting",20),fg="maroon1",bg="white")
label.pack()
print("\n")
print("\n")
print("\n")
Label(window,text="1.Questions are related to python programming \n 2.Each Question as Four Options Out of which only one is correct \n 3.Correct Option will be displayed soon after answering \n 4.You cannot reback the question \n 5.final result will be displayed after the test completion",width="150",justify="left",font=("Berlin Sans FB",10),fg="black",bg="white").pack()
button = Button(window, text="Start", command=askQuestion,font=("Times",15),fg="green",bg="yellow")
        
button.pack()
window.mainloop()

