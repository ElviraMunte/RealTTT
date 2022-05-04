from abc import ABC, abstractmethod
from Game import Game

class Ui(ABC):

    @abstractmethod
    def run(self):
        raise NotImplementedError

class Gui(Ui):
    def __init__(self):
        pass

    def run(self):
        pass

class Terminal(Ui):
    def __init__(self):
        self.board = Game()
        self.user1 = input("Enter name of first player: ")
        self.user2 = input("Enter name of second player: ")

    def run(self):
        for i in range(9):
            if i % 2 == 1:
                toPlay = self.user1
                token = "X"
            else:
                toPlay = self.user2
                token = "O"

            print("It's",toPlay,"'s turn.")
            row = int(input("Enter the row number: "))
            col = int(input("Enter the column number: "))
            self.board.play(row,col,token)
            self.board.__repr__()
            result = self.board.winner()
            if result == "winner":
                print(toPlay,"has won. Well done!")
                break
            if i == 8:
                print("It's a draw...")
