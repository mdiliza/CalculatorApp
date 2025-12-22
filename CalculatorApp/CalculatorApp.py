from tkinter import *

# function for storing numbers
def storeNum(inputNum):
    recentNums = []
    recentNums.append(inputNum)

# Function for showing numbers in the entry widget
def placeNum(btnNum):
    numToAdd = btnNum
    current = calDisp.get()
    calDisp.textvariable.set(current+btnNum)
    print("Function 'Placenum' Activated")

# Function to Create 10 buttons, name,  and store them 
def buttonMaker():    
    x = 0
    btnArr = [] 
    while x < 10:   
        buttonTitle = str(x)
        buttonNumber = x
        btnArr.append(Button(calc, activebackground="red", width = 2, text=buttonTitle, command=placeNum(buttonNumber), cursor = "hand1"))
        x = x+1
    return btnArr

# Initialising variables to automate the layout of the buttons
def buttonPlacer():
    p = 1
    y = 0
    z = 1
    while p <=9:
        btArray[p].grid(column=y, row=z)
        p = p+1
        y=y+1
        if y ==3:
            y=0
            z=z+1
    btArray[0].configure(width = 9)
    btArray[0].grid(column = 0, row = 5, columnspan = 4)

# Creating root window
calc = Tk()
calc.geometry("500x600")
calc.title("Calcul8r")

# Creating entry widget for numbers 
text_behaviour = StringVar()
calDisp = Entry(calc, width= 10, justify="left", textvariable = text_behaviour, bg = "lightgray", text = "Please enter a number")
calDisp.grid(column = 0, row = 0, columnspan = 3)

# call functions for creating the tk window
btArray = buttonMaker()
buttonPlacer()
calc.mainloop()
