from tkinter import *
import tkinter.font   
# Function to Create 10 buttons, name,  and store them 
def buttonMaker():
    btArray = []
    zero =Button(calc, activebackground="red", width = 2, text="0", font=custom_font_buttons, command= lambda: placeNum(0), cursor = "hand2")
    btArray.append(zero)
    one =Button(calc, activebackground="red", width = 2, text="1", font=custom_font_buttons, command= lambda: placeNum(1), cursor = "hand2")
    btArray.append(one)
    two =Button(calc, activebackground="red", width = 2, text="2", font=custom_font_buttons, command= lambda: placeNum(2), cursor = "hand2")
    btArray.append(two)
    three =Button(calc, activebackground="red", width = 2, text="3", font=custom_font_buttons, command= lambda: placeNum(3), cursor = "hand2")
    btArray.append(three)
    four =Button(calc, activebackground="red", width = 2, text="4", font=custom_font_buttons, command= lambda: placeNum(4), cursor = "hand2")
    btArray.append(four)
    five =Button(calc, activebackground="red", width = 2, text="5", font=custom_font_buttons, command= lambda: placeNum(5), cursor = "hand2")
    btArray.append(five)
    six =Button(calc, activebackground="red", width = 2, text="6", font=custom_font_buttons,command= lambda: placeNum(6), cursor = "hand2")
    btArray.append(six)
    seven =Button(calc, activebackground="red", width = 2, text="7", font=custom_font_buttons, command= lambda: placeNum(7), cursor = "hand2")
    btArray.append(seven)
    eight =Button(calc, activebackground="red", width = 2, text="8", font=custom_font_buttons, command= lambda: placeNum(8), cursor = "hand2")
    btArray.append(eight)
    nine =Button(calc, activebackground="red", width = 2, text="9", font=custom_font_buttons, command= lambda: placeNum(9), cursor = "hand2")
    btArray.append(nine)
    return btArray

# Initialising variables to automate the grid layout of the numeric buttons
def buttonPlacer(btArray):
    p = 1
    y = 0
    z = 1
    while p <=9:
        btArray[p].grid(column=y, row=z, sticky=NSEW, padx=0, pady=0)
        p = p+1
        y=y+1
        if y ==3:
            y=0
            z=z+1
    btArray[0].configure(width = 9)
    btArray[0].grid(column = 0, row = 4, columnspan = 3, sticky=NSEW)

# Function for showing numbers in the text widget
def placeNum(btnNum):
    numToAdd = str(btnNum)
    current = textBox.get('1.0')
    if current == "Please enter number":
        textBox.delete('0', END) 
        textBox.insert(index=LAST, chars=numToAdd)
        current=''
        print(f"Function 'Placenum' Activated")
    else:
        textBox.insert(index=END, chars= numToAdd)

# Functions for initating operations
def plus(recents, operand):
    
    try:
        last_operation = operand[len(operand)-1]
    except IndexError:
        last_operation = 'M'
    number_to_store = int(textBox.get("1.0", END))
    recents.append(number_to_store)
    if (len(recents) > 1) and (last_operation=='P'):
           prevnum = recents[len(recents)-2]
           recents.append(prevnum + number_to_store )
    if (len(recents) > 1) and (last_operation=='M'):
           prevnum = recents[len(recents)-2]
           recents.append(prevnum - number_to_store )
    operand.append("P")
    textBox.delete('1.0', END)
    print(f"LOG: recents elements: {recent_num_array}\n     Operand: {last_operation}")
    return recents

def minus(recents, operand):
    try:
        last_operation = operand[len(operand)-1]
    except IndexError:
        last_operation = 'M'
    number_to_store = int(textBox.get("1.0", END))
    recents.append(number_to_store)
    if (len(recents) > 1) and (last_operation=='M'):
           prevnum = recents[len(recents)-2]
           recents.append(prevnum - number_to_store )
    if (len(recents) > 1) and (last_operation=='P'):
           prevnum = recents[len(recents)-2]
           recents.append(prevnum + number_to_store )
    operand.append("M")
    textBox.delete('1.0', END)
    print(f"LOG: recents elements: {recent_num_array}\n     Operand: {last_operation}")
    return recents

def times(recents, operand):
    operand.append("T")
    last_operation = operand[len(operand)-1]
    number_to_store = int(textBox.get("1.0", END))
    recents.append(number_to_store)
    if (len(recents) > 1) and (last_operation=='P'):
           prevnum = recents[len(recents)-2]
           recents.append(prevnum * number_to_store )
    textBox.delete('1.0', END)
    print(f"LOG: recents elements: {recent_num_array}\n     Operand: {last_operation}")
    return recents

def divide(recents, operand):
    operand.append("D")
    last_operation = operand[len(operand)-1]
    number_to_store = int(textBox.get("1.0", END))
    recents.append(number_to_store)
    if (len(recents) > 1) and (last_operation=='P'):
           prevnum = recents[len(recents)-2]
           recents.append(prevnum / number_to_store )
    textBox.delete('1.0', END)
    print(f"LOG: recents elements: {recent_num_array}\n     Operand: {last_operation}")
    return recents

# Adding buttons for operations 
def operations():
    addButton = Button(calc, text = "+",  font=custom_font_buttons, command= lambda: plus(recent_num_array, operand), cursor = "hand2")
    addButton.grid(column=3,row=1, sticky= NSEW)
    minusButton = Button(calc, text = "-", font=custom_font_buttons, command= lambda: minus(recent_num_array, operand), cursor = "hand2")
    minusButton.grid(column=3,row=2, sticky= NSEW)
    '''   
   timesButton = Button(calc, text = "x", command= lambda: times(recent_num_array, operand), cursor = "hand2")
    timesButton.grid(column=3,row=3, sticky= NSEW)
    divideButton = Button(calc, text = "/", command= lambda: divide(recent_num_array, operand), cursor = "hand2")
    divideButton.grid(column=3,row=4, sticky= NSEW)
    '''    

def displayAnswer(recents, operand):
    last_num_typed = textBox.get("1.0", END)
    
    #textBox.delete("1.0", END)
    print(operand)
    print(recent_num_array)
    try:
        last_op = operand[len(operand)-1]
        if last_op =='P':
            prevnum = recents[len(recents)-1]
            answer = prevnum + int(last_num_typed)
            textBox.delete("1.0", END)
            textBox.insert('1.0', answer) 
        if last_op =='M':
            prevnum = recents[len(recents)-1]
            answer = prevnum - int(last_num_typed)
            textBox.delete("1.0", END)
            textBox.insert('1.0', answer) 
        if last_op =='T':
            prevnum = recents[len(recents)-1]
            answer = prevnum * int(last_num_typed)
            textBox.delete("1.0", END)
            textBox.insert('1.0', answer) 
        if last_op =='D':
            prevnum = recents[len(recents)-1]
            answer = prevnum / int(last_num_typed)
            textBox.delete("1.0", END)
            textBox.insert('1.0', answer)
    except IndexError:
        textBox.delete("1.0", END)
        textBox.insert(END, last_num_typed)

def acFuntion():
    textBox.delete("1.0", END)
    recent_num_array.clear()
    answer_array.clear()

# Main initialisers and callers
# Creating root window
calc = Tk()
calc.geometry("500x600")
calc.title("Calcul8r")
calc.resizable('False', 'False')    
calc.columnconfigure(0,weight=1)
calc.columnconfigure(1,weight=1)
calc.columnconfigure(2,weight=1)
calc.columnconfigure(3,weight=2)
calc.rowconfigure(0, weight=2)
calc.rowconfigure(1, weight=1)
calc.rowconfigure(2, weight=1)
calc.rowconfigure(3, weight=1)
calc.rowconfigure(4, weight=1)
calc.rowconfigure(5, weight=1)
recent_num_array = []
answer_array = []
operand = []

#Custom Fonts
custom_font_buttons = tkinter.font.Font(family= "Arial", size = 20, weight = "bold")
custom_font_numbers = tkinter.font.Font(family= "consola", size = 60, weight = "bold")

# Creating Text widget for entering numbers 
textBox = Text(calc, bg = "grey", height=1, width=6)
textBox.grid(column = 0, row = 0, columnspan=4, sticky=NSEW,)
 # <-- custom font
textBox.configure(font = custom_font_numbers)

# Creating Equals Button
equal_button = Button(calc, activebackground="green", text="=",  font=custom_font_buttons, command= lambda: displayAnswer(recent_num_array, operand))
equal_button.grid(column=0, row = 5, columnspan = 3, sticky=NSEW)

# Creating AC button (or 'CANCEL' button)
ACbutton = Button(calc, width = 2, text="AC",  font=custom_font_buttons, command= acFuntion, cursor = "hand2", padx = 1)
ACbutton.grid(column=3, row = 5, sticky=NSEW)

# Constructing and initialising window
btArray = buttonMaker()
buttonPlacer(btArray)
operations()
calc.mainloop()