from tkinter import *
# Function for showing numbers in the entry widget
def placeNum(btnNum,btArray):
    btArray = btArray
    numToAdd = str(btnNum)
    current = textBox.get('1.0')
    if current == "Please enter number":
        textBox.delete('0', END) 
        textBox.insert(index='1.0', chars=numToAdd)
        current=''
        print(f"Function 'Placenum' Activated")
    else:
        textBox.insert(index="1.0", chars= numToAdd)
        print(btArray.find(Button.text))
      

# Function to Create 10 buttons, name,  and store them 

def buttonMaker():
    #Button(calc, activebackground="red", width = 2, text=buttonTitle, command= lambda: placeNum(self.text)),cursor = "hand2")
    
    x = 0
    btnArr = [] 
    
    while x < 10:   
        buttonTitle = str(x)
        buttonNumber = x
        btnArr.append(Button(calc, 
                             activebackground="red", 
                             width = 2, 
                             text=buttonTitle, 
                             command= lambda: placeNum(int()),
                             #command = testButton,
                             #state='disabled', 
                             cursor = "hand2"))
        x = x+1
    
    return btnArr


# Initialising variables to automate the layout of the buttons
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

# function for storing numbers
def storeNum(inputNum):
    number_to_store = textBox.get()
    print(f"number being stored: {number_to_store}")
    recentNums = []
    recentNums.append(inputNum)

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

# Creating Text widget for entering numbers 
textBox = Text(calc, bg = "grey", height=1, width=6)
#textBox['state'] = 'disabled'
textBox.grid(column = 0, row = 0, columnspan=4, sticky=NSEW)

#program for testing buttons
def testButton(text):
    textBox.insert('1.0', chars= '')
    print(f"numbers being stored: {textBox.get(1.0)}")
# Main program
def main():
    btArray = buttonMaker()
    buttonPlacer(btArray)
    calc.mainloop()
#running program
main()
