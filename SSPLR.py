from tkinter import *
import random

class Main(Frame):
    def __init__(self, root):
        super(Main, self).__init__(root)
        self.startUI()

    def startUI(self):
        btn_scissor = Button(root, text = "scissor", font = ("Fira Code", 12),
                    command = lambda x = "scissor" : self.user_choice(x))
        btn_rock = Button(root, text = "rock", font = ("Fira Code", 12),
                    command = lambda x = "rock" : self.user_choice(x))
        btn_paper = Button(root, text = "paper", font = ("Fira Code", 12),
                    command = lambda x = "paper" : self.user_choice(x))
        btn_lizard = Button(root, text = "lizard", font = ("Fira code", 12),
                    command = lambda x = "lizard" : self.user_choice(x))
        btn_spock = Button(root, text = "spock", font = ("Fira Code", 12),
                    command = lambda x = "spock" : self.user_choice(x))
        self.win = self.draw = self.lose = 0
        self.info_game = Label(root, text = "Start game!", bg = "#FFF",
                    font = ("Fira Code", 20, "bold"))
        self.info_game.place( x = 260, y = 25)

        self.result = Label(root, justify = "left",
                    font = ("Fira Code ", 12),
                    text = f" * Win: {self.win}\n * Lose:{self.lose}\n * Draw: {self.draw}", bg="#FFF")
        self.result.place(x=5, y=5)

        btn_scissor.place(x = 25, y = 200, width = 100, height = 30)
        btn_rock.place(x = 150, y = 200, width = 100, height = 30)
        btn_paper.place(x = 275, y = 200, width = 100, height = 30)
        btn_lizard.place(x = 400, y = 200, width = 100, height = 30)
        btn_spock.place(x = 525, y = 200, width = 100, height = 30)

    def user_choice(self, user_choice):
        pc_choice = random.choice(["scissor", "paper", "rock", "lizard", "spock"])

        if user_choice == pc_choice:
            self.draw += 1
            self.info_game.configure(text = "DRAW")

        elif user_choice == "scissor" and pc_choice == "paper" or pc_choice == "lizard":
            self.win += 1
            self.info_game.configure(text = "WIN")
        elif user_choice == "scissor" and pc_choice == "rock" or pc_choice == "spock":
            self.lose += 1
            self.info_game.configure(text = "LOSE")

        elif user_choice == "paper" and pc_choice == "rock" or pc_choice == "spock":
            self.win += 1
            self.info_game.configure(text = "WIN")
        elif user_choice == "paper" and pc_choice == "lizard" or pc_choice == "scissor":
            self.lose += 1
            self.info_game.configure(text = "LOSE")

        elif user_choice == "rock" and pc_choice == "lizard" or pc_choice == "scissor":
            self.win += 1
            self.info_game.configure(text = "WIN")
        elif user_choice == "rock" and pc_choice == "spock" or pc_choice == "paper":
            self.lose += 1
            self.info_game.configure(text = "LOSE")

        elif user_choice == "lizard" and pc_choice == "spock" or pc_choice == "paper":
            self.win += 1
            self.info_game.configure(text = "WIN")
        elif user_choice == "lizard" and pc_choice == "rock" or pc_choice == "scissor":
            self.lose += 1
            self.info_game.configure(text = "LOSE")

        elif user_choice == "spock" and pc_choice == "scissor" or pc_choice == "rock":
            self.win += 1
            self.info_game.configure(text = "WIN")
        elif user_choice == "spock" and pc_choice == "paper" or pc_choice == "lizard":
            self.lose += 1
            self.info_game.configure(text = "LOSE")

        self.result.configure( text=f" * Win: {self.win}\n * Lose:{self.lose}\n * Draw: {self.draw}", bg="#FFF")


if __name__ == '__main__':
    root = Tk()
    root.geometry("650x300")
    root.title("Scissor - paper - rock - lizard - Spock")
    root.resizable(False, False)
    root["bg"] = "#FFF"
    app = Main(root)
    app.pack()
    root.mainloop()