import os
import random
from .Game import Game


class TicTacToe(Game):
    def __init__(self):
        """ TicTacToe Game """
        super(TicTacToe, self).__init__()

        self.playerLetter = 'X'
        self.computerLetter = 'O'

    @staticmethod
    def clear():
        """ Clear console/terminal """
        if os.name == 'posix':
            os.system('clear')
        else:
            os.system('cls')

    def play(self):
        """ Starting match """
        self.clear()
        self.turn = self.randomInitialTurn()
        self.playing = True

        while self.playing:
            self.clear()

            if self.turn == 'player':
                self.turnPlayer()
            else:
                self.turnComputer()

    def endGame(self):
        """ Enclose Match """
        self.playing = False

    @staticmethod
    def randomInitialTurn():
        """ Select first start player """
        if random.randint(0, 1) == 0:
            return 'computer'
        else:
            return 'player'

    def turnPlayer(self):
        self.draw()
        self.makeMove(self.playerLetter, self.getPlayerMove())

        if self.isWinner(self.playerLetter):
            self.draw()
            self.endGame()
            print('[You won!]')
        elif self.isFull:
            self.draw()
            self.endGame()
            print('[Tie]')
        else:
            self.turn = 'computer'

    def turnComputer(self):
        self.makeMove(self.computerLetter, self.getComputerMove())

        if self.isWinner(self.computerLetter):
            self.draw()
            self.endGame()
            print('[You lost.]')
        elif self.isFull:
            self.draw()
            self.endGame()
            print('[Tie]')
        else:
            self.turn = 'player'


if __name__ == '__main__':
    game = TicTacToe()

    game.clear()
    print("""
    ######################################
    #####       T i c T a c T o e    #####
    ######################################

    Game map : )
    """)

    game.drawMap()
    input('[PRESS ANY KEY TO CONTINUE...]')

    while True:
        game.play()

        if not input('Play Again? (y/n)').lower().startswith('y'):
            break
        else:
            game.reset()
