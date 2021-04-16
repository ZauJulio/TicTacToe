from copy import deepcopy


class Board:
    def __init__(self):
        """ TicTacToeBoard """
        self.table = [' '] * 10

    def copy(self):
        """ Return copy of board"""
        return deepcopy(self)

    @property
    def isFull(self) -> bool:
        """ Check if the board is fully completed """
        for pos in range(1, 10):
            if self.isFreeSpace(pos):
                return False
        return True

    @property
    def isEmpty(self) -> None:
        """ Check if the board is empty """
        if all(pos == ' ' for pos in self.table):
            return True
        else:
            return False

    def isFreeSpace(self, move: int) -> bool:
        """ Check if move is free space(Valid move)"""
        return self.table[move] == ' '

    def draw(self) -> None:
        """ Draw current board state """
        print(f"""
        ######################
        ##       |   |      ##
        ##     {self.table[7]} | {self.table[8]} | {self.table[9]}    ##
        ##       |   |      ##
        ##    --- --- ---   ##
        ##       |   |      ##
        ##     {self.table[4]} | {self.table[5]} | {self.table[6]}    ##
        ##       |   |      ##
        ##    --- --- ---   ##
        ##       |   |      ##
        ##     {self.table[1]} | {self.table[2]} | {self.table[3]}    ##
        ##       |   |      ##
        ######################
        """)

    @staticmethod
    def drawMap():
        """ Draw map of board """
        print(f"""
        ######################
        ##       |   |      ##
        ##     7 | 8 | 9    ##
        ##       |   |      ##
        ##    --- --- ---   ##
        ##       |   |      ##
        ##     4 | 5 | 6    ##
        ##       |   |      ##
        ##    --- --- ---   ##
        ##       |   |      ##
        ##     1 | 2 | 3    ##
        ##       |   |      ##
        ######################
      """)

    def makeMove(self, letter: str, move: int) -> None:
        """ Set move with letter if is free space in board"""
        if self.isFreeSpace(move):
            self.table[move] = letter

    def isWinner(self, letter: str) -> bool:
        """ Prints out the board

        Parameters
        ----------
            bo: list() - (ignore index 0)
            letter: str() player

        Returns
        -------
            bool(), True if that player has won.
        """
        return (
            # top
            (self.table[7] == letter and self.table[8] == letter and self.table[9] == letter) or
            # middle
            (self.table[4] == letter and self.table[5] == letter and self.table[6] == letter) or
            # bottom
            (self.table[1] == letter and self.table[2] == letter and self.table[3] == letter) or
            # down the left
            (self.table[7] == letter and self.table[4] == letter and self.table[1] == letter) or
            # down the middle
            (self.table[8] == letter and self.table[5] == letter and self.table[2] == letter) or
            # down the right side
            (self.table[9] == letter and self.table[6] == letter and self.table[3] == letter) or
            # diagonal
            (self.table[7] == letter and self.table[5] == letter and self.table[3] == letter) or
            # diagonal
            (self.table[9] == letter and self.table[5] == letter and self.table[1] == letter))
