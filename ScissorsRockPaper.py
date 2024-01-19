# import modules
from tkinter import *

# define global variables
# TODO define global variables
global PointM
PointM=0
global PointJ
PointJ=0
global www
www=0
global R
R=0

# define all functions
# TODO define all functions
def chooseS (event):
    global www
    www+=1
    global R
    print(www, R, "chooseP")
    global PointM
    global PointJ
    if www==2:
        if R==1:
            labelJ.config(text="Scissors", bg="Red")
            labelM.config(text="Rock", bg="Green")
            PointM+=2
            labelPJ.config(text="                    " + str(PointJ) + "                    ")
            labelPM.config(text="                   " + str(PointM) + "                   ")

        elif R==2:
            labelJ.config(text="Scissors", bg="Blue")
            labelM.config(text="Scissors", bg="Blue")
            PointM+=1
            PointJ+=1
            labelPJ.config(text="                    " + str(PointJ) + "                    ")
            labelPM.config(text="                   " + str(PointM) + "                   ")

        elif R==3:
            labelJ.config(text="Scissors", bg="Green")
            labelM.config(text="Paper", bg="Red")
            PointJ+=2
            labelPJ.config(text="                    " + str(PointJ) + "                    ")
            labelPM.config(text="                   " + str(PointM) + "                   ")

        if PointM >= 10:
            labelJ.config(text="Dommage", bg="Red")
            labelM.config(text="Dommage", bg="Red")
            Button1.config(text="Dommage", bg="Red")
            Button2.config(text="Dommage", bg="Red")
            Button3.config(text="Dommage", bg="Red")
            window.config(bg="Red")

        if PointJ >= 10:
            labelJ.config(text="BRAVO", bg="pink")
            labelM.config(text="BRAVO", bg="pink")
            Button1.config(text="BRAVO", bg="pink")
            Button2.config(text="BRAVO", bg="pink")
            Button3.config(text="BRAVO", bg="pink")
            window.config(bg="pink")
        www=0
    else:
        R = 2
        labelJ.config(text="En attente de l'autre", bg="green")
def chooseR (event):
    global PointM
    global PointJ
    global www
    www += 1
    global R
    print(www, R, "chooseR")
    if www==2:
        if R==1:
            labelJ.config(text="Rock", bg="Blue")
            labelM.config(text="Rock", bg="Blue")
            PointM+=1
            PointJ+=1
            labelPJ.config(text="                    " + str(PointJ) + "                    ")
            labelPM.config(text="                   " + str(PointM) + "                   ")

        elif R==2:
            labelJ.config(text="Rock", bg="Green")
            labelM.config(text="Scissors", bg="Red")
            PointJ+=2
            labelPJ.config(text="                    " + str(PointJ) + "                    ")
            labelPM.config(text="                   " + str(PointM) + "                   ")


        elif R==3:
            labelJ.config(text="Rock", bg="Red")
            labelM.config(text="Paper", bg="Green")
            PointM+=2
            labelPJ.config(text="                    " + str(PointJ) + "                    ")
            labelPM.config(text="                   " + str(PointM) + "                   ")

        if PointM >= 10:
            labelJ.config(text="Dommage", bg="Red")
            labelM.config(text="Dommage", bg="Red")
            Button1.config(text="Dommage", bg="Red")
            Button2.config(text="Dommage", bg="Red")
            Button3.config(text="Dommage", bg="Red")
            window.config(bg="Red")

        if PointJ >= 10:
            labelJ.config(text="BRAVO", bg="pink")
            labelM.config(text="BRAVO", bg="pink")
            Button1.config(text="BRAVO", bg="pink")
            Button2.config(text="BRAVO", bg="pink")
            Button3.config(text="BRAVO", bg="pink")
            window.config(bg="pink")
        www = 0
    else:
        R = 1
        labelJ.config(text="En attente de l'autre", bg="green")
def chooseP (event):
    global PointM
    global PointJ
    global www
    www += 1
    global R
    print(www, R, "chooseP")
    if www==2:
        if R==1:
            labelJ.config(text="Paper", bg="Green")
            labelM.config(text="Rock", bg="Red")
            PointJ+=2
            labelPJ.config(text="                    "+str(PointJ)+"                    ")
            labelPM.config(text="                   "+str(PointM)+"                   ")


        elif R==2:
            labelJ.config(text="Paper", bg="Red")
            labelM.config(text="Scissors", bg="Green")
            PointM+=2
            labelPJ.config(text="                    "+str(PointJ)+"                    ")
            labelPM.config(text="                   "+str(PointM)+"                   ")



        elif R==3:
            labelJ.config(text="Paper", bg="Blue")
            labelM.config(text="Paper", bg="Blue")
            PointM+=1
            PointJ+=1
            labelPJ.config(text="                    "+str(PointJ)+"                    ")
            labelPM.config(text="                   "+str(PointM)+"                   ")
        if PointM >= 10:
            labelJ.config(text="Dommage", bg="Red")
            labelM.config(text="Dommage", bg="Red")
            Button1.config(text="Dommage", bg="Red")
            Button2.config(text="Dommage", bg="Red")
            Button3.config(text="Dommage", bg="Red")
            window.config(bg="Red")

        if PointJ >= 10:
            labelJ.config(text="BRAVO", bg="pink")
            labelM.config(text="BRAVO", bg="pink")
            Button1.config(text="BRAVO", bg="pink")
            Button2.config(text="BRAVO", bg="pink")
            Button3.config(text="BRAVO", bg="pink")
            window.config(bg="pink")
        www = 0
    else:
        R = 3
        labelJ.config(text="En attente de l'autre", bg="green")


def chooseSMMM (event):
    global www
    www+=1
    global R
    print(www, R, "chooseP")
    global PointM
    global PointJ
    if www==2:
        if R==1:
            labelM.config(text="Scissors", bg="Red")
            labelJ.config(text="Rock", bg="Green")
            PointJ += 2
            labelPJ.config(text="                    " + str(PointJ) + "                    ")
            labelPM.config(text="                   " + str(PointM) + "                   ")
        elif R==2:
            labelJ.config(text="Scissors", bg="Blue")
            labelM.config(text="Scissors", bg="Blue")
            PointM+=1
            PointJ+=1
            labelPJ.config(text="                    " + str(PointJ) + "                    ")
            labelPM.config(text="                   " + str(PointM) + "                   ")

        elif R==3:
                labelM.config(text="Scissors", bg="Green")
                labelJ.config(text="Paper", bg="Red")
                PointM += 2
                labelPJ.config(text="                    " + str(PointJ) + "                    ")
                labelPM.config(text="                   " + str(PointM) + "                   ")
        if PointM >= 10:
            labelJ.config(text="Dommage", bg="Red")
            labelM.config(text="Dommage", bg="Red")
            Button1.config(text="Dommage", bg="Red")
            Button2.config(text="Dommage", bg="Red")
            Button3.config(text="Dommage", bg="Red")
            window.config(bg="Red")

        if PointJ >= 10:
            labelJ.config(text="BRAVO", bg="pink")
            labelM.config(text="BRAVO", bg="pink")
            Button1.config(text="BRAVO", bg="pink")
            Button2.config(text="BRAVO", bg="pink")
            Button3.config(text="BRAVO", bg="pink")
            window.config(bg="pink")
        www=0
    else:
        R = 2
        labelM.config(text="En attente de l'autre", bg="green")
def chooseRMMM (event):
    global PointM
    global PointJ
    global www
    www += 1
    global R
    print(www, R, "chooseR")
    if www==2:
        if R==1:
            labelJ.config(text="Rock", bg="Blue")
            labelM.config(text="Rock", bg="Blue")
            PointM+=1
            PointJ+=1
            labelPJ.config(text="                    " + str(PointJ) + "                    ")
            labelPM.config(text="                   " + str(PointM) + "                   ")

        elif R==2:
                labelM.config(text="Rock", bg="Green")
                labelJ.config(text="Scissors", bg="Red")
                PointM += 2
                labelPJ.config(text="                    " + str(PointJ) + "                    ")
                labelPM.config(text="                   " + str(PointM) + "                   ")

        elif R==3:
                labelM.config(text="Rock", bg="Red")
                labelJ.config(text="Paper", bg="Green")
                PointJ += 2
                labelPJ.config(text="                    " + str(PointJ) + "                    ")
                labelPM.config(text="                   " + str(PointM) + "                   ")
        if PointM >= 10:
            labelJ.config(text="Dommage", bg="Red")
            labelM.config(text="Dommage", bg="Red")
            Button1.config(text="Dommage", bg="Red")
            Button2.config(text="Dommage", bg="Red")
            Button3.config(text="Dommage", bg="Red")
            window.config(bg="Red")

        if PointJ >= 10:
            labelJ.config(text="BRAVO", bg="pink")
            labelM.config(text="BRAVO", bg="pink")
            Button1.config(text="BRAVO", bg="pink")
            Button2.config(text="BRAVO", bg="pink")
            Button3.config(text="BRAVO", bg="pink")
            window.config(bg="pink")
        www = 0
    else:
        R = 1
        labelM.config(text="En attente de l'autre", bg="green")
def choosePMMM (event):
    global PointM
    global PointJ
    global www
    www += 1
    global R
    print(www, R, "chooseP")
    if www==2:
        if R==1:
                labelM.config(text="Paper", bg="Green")
                labelJ.config(text="Rock", bg="Red")
                PointM += 2
                labelPJ.config(text="                    " + str(PointJ) + "                    ")
                labelPM.config(text="                   " + str(PointM) + "                   ")

        elif R==2:
                labelM.config(text="Paper", bg="Red")
                labelJ.config(text="Scissors", bg="Green")
                PointJ += 2
                labelPJ.config(text="                    " + str(PointJ) + "                    ")
                labelPM.config(text="                   " + str(PointM) + "                   ")


        elif R==3:
            labelJ.config(text="Paper", bg="Blue")
            labelM.config(text="Paper", bg="Blue")
            PointM+=1
            PointJ+=1
            labelPJ.config(text="                    "+str(PointJ)+"                    ")
            labelPM.config(text="                   "+str(PointM)+"                   ")
        if PointM >= 10:
            labelJ.config(text="Dommage", bg="Red")
            labelM.config(text="Dommage", bg="Red")
            Button1.config(text="Dommage", bg="Red")
            Button2.config(text="Dommage", bg="Red")
            Button3.config(text="Dommage", bg="Red")
            window.config(bg="Red")

        if PointJ >= 10:
            labelJ.config(text="BRAVO", bg="pink")
            labelM.config(text="BRAVO", bg="pink")
            Button1.config(text="BRAVO", bg="pink")
            Button2.config(text="BRAVO", bg="pink")
            Button3.config(text="BRAVO", bg="pink")
            window.config(bg="pink")
        www = 0
    else:
        R = 3
        labelM.config(text="En attente de l'autre", bg="green")

# create window
PointM=0
PointJ=0
window = Tk()
window.title("Exercise 3")
window.config(bg="pink")
top_frame = Frame(window)
left_frame = Frame(window)
right_frame = Frame(window)
right_middle_frame = Frame(right_frame)
right_bottom_frame = Frame(right_frame)
left_middle_frame = Frame(left_frame)
left_bottom_frame = Frame(left_frame)
left_bottom_frame.config(bg="pink")

top_frame.pack()
left_frame.pack(side=LEFT)
right_frame.pack(side=RIGHT)
left_middle_frame.pack()
left_bottom_frame.pack()
right_middle_frame.pack()
right_bottom_frame.pack()



Button1 = Button(top_frame, text="Rock", bg="pink")
Button2 = Button(top_frame, text="Paper", bg="pink")
Button3 = Button(top_frame, text="Scissors", bg="pink")
labelM = Label(right_middle_frame, text="En attente de la réponse", bg="pink")
labelJ = Label(left_middle_frame, text="En attente de la réponse", bg="pink")
labelPJ = Label(left_middle_frame, text="                    "+str(PointM)+"                    ", fg="green", bg="pink")
labelPM = Label(right_middle_frame, text="                   "+str(PointJ)+"                   ", fg="green", bg="pink")
window.bind("a",chooseS)
window.bind("s",chooseP)
window.bind("d",chooseR)
window.bind("j",chooseSMMM)
window.bind("k",choosePMMM)
window.bind("l",chooseRMMM)
labelM.pack()
labelJ.pack()
labelPJ.pack()
labelPM.pack()

Button1.pack(side=RIGHT)
Button2.pack(side=RIGHT)
Button3.pack(side=LEFT)

window.mainloop()

# create widgets
# TODO create widgets


# place widgets into window container using a layout
# TODO place widgets into window container using a layout

# open window
window.mainloop()