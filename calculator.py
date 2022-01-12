from tkinter import *
from decimal import *

window = Tk()
window.title("Calculator")

buttons = ( ('7', '8', '9', '/', '4'),
            ('4', '5', '6', '*', '5'),
            ('1', '2', '3', '-', '4'),
            ('0','.','=', '+', '4') )

active_str = ""
stack = []

def calculate():
    global stack
    global label
    result = 0
    operand2 = Decimal(stack.pop())
    operation = stack.pop()
    operand1 = Decimal(stack.pop())

    if operation == "+":
        result = operand1 + operand2
    if operation == "-":
        result = operand1 - operand2
    if operation == "/":
        result = operand1 / operand2
    if operation == "*":
        result = operand1 * operand1
    label.configure(text=str(result))

def click(text):
    global active_str
    global stack
    if text == 'CE':
        stack.clear()
        active_str = ""
        label.configure(text="0")
    elif "0" <= text <= "9":
        active_str += text
        label.configure(text=active_str)
    elif text == ".":
        if active_str.find(".") == -1:
            active_str += text
            label.configure(text=active_str)
    else:
        if len(stack) >=2:
            stack.append(label["text"])
            calculate()
            stack.clear()
            stack.append(label["text"])
            active_str = ""
            if text != "=":
                stack.append(text)
        else:
            if text != "=":
                stack.append(label["text"])
                stack.append(text)
                active_str = ""
                label.configure(text="0")

label = Label(window, text="0", width=35)
label.grid(row=0, column=0, columnspan=4, sticky="nsew")

button = Button(window, text="CE", command=lambda text="CE": click(text))
button.grid(row=1, column=3, sticky="nsew")
for row in range(4):
    for col in range(4):
        button = Button(window, text = buttons[row][col],
                command=lambda row=row, col=col: click(buttons[row][col]))
        button.grid(row=row + 2, column=col, sticky="nsew")

window.grid_rowconfigure(6,weight=1)
window.grid_columnconfigure(4,weight=1)

window.mainloop()

