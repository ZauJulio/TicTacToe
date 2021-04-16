import random
from .Board import Board
from .Computer import Computer


class Game:
    def __init__(self):
        self.playerLetter = 'X'
        self.computerLetter = 'O'

        self.__board = Board()
        self.__computer = Computer(self.playerLetter, self.computerLetter)

    def getPlayerMove(self):
        move = 0
        while not (move >= 1 and move <= 9) or not self.isFreeSpace(move):
            move = input('Next move? (1-9): ')
            try:
                move = int(move)
            except ValueError:
                move = 0
        return move

    # Wrap Methods

    def getComputerMove(self):
        return self.__computer.getMove(self.__board)

    def isFreeSpace(self, move: int):
        return self.__board.isFreeSpace(move)

    def isWinner(self, playerLetter: str):
        return self.__board.isWinner(playerLetter)

    def makeMove(self, letter: str, move: int):
        self.__board.makeMove(letter, move)

    def draw(self):
        self.__board.draw()

    def drawMap(self):
        self.__board.drawMap()

    @property
    def isFull(self):
        return self.__board.isFull

    def reset(self):
        self.__board = Board()
