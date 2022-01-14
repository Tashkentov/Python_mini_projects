from tkinter import *

def click(calculus_system):
    to_convert = int(calculus_system)
    result_digit=0
    if to_convert == 2:
        result_digit = bin(int(enter_digit.get()))[2:]
    elif to_convert == 8:
        result_digit = oct(int(enter_digit.get()))[2:]
    elif to_convert == 16:
        result_digit = hex(int(enter_digit.get()))[2:].upper()


    label_result.configure(text=str(result_digit))


window = Tk()
window.title("DIGIT CONVERTER")
window.geometry("320x120")

enter_digit = Entry(window,width=50)
enter_digit.grid(column=0, row=0, columnspan=3, padx=5, pady=5, ipady=3)

label_result = Label(window,text="", font="Fira-Code 10",)
label_result.grid(row=2, columnspan=3)

button_2 = Button(window, text="2", command=lambda text="2": click(text))
button_2.grid(row=1, column=0, sticky="nswe", padx=3, pady=3,)
button_8 = Button(window, text="8", command=lambda text="8": click(text))
button_8.grid(row=1, column=1, sticky="nswe", padx=3, pady=3)
button_16 = Button(window, text="16", command=lambda text="16": click(text))
button_16.grid(row=1, column=2, sticky="nswe", padx=3, pady=3)


window.mainloop()