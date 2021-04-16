import random
from typing import Iterator, Union
from .Board import Board


class Computer:
    def __init__(self, playerLetter: str, computerLetter: str):
        """ Simple Search Algorithm with Victory Strategy

        Parameters
        ----------
        playerLetter: str
            Player Letter to assing the board
        computerLetter: str
            Computer Letter to assing the board
        """
        self.playerLetter = playerLetter
        self.computerLetter = computerLetter

    @staticmethod
    def chooseRandomMoveFromList(board: Board, movesList):
        """ Get random play by list

        Parameters
        ----------
        board: Board
            Playing board with game status

        Returns
        -------
            move: int
        """
        possibleMoves = [move for move in movesList if board.isFreeSpace(move)]
        return random.choice(possibleMoves) if len(possibleMoves) > 0 else None

    def getStrategyMove(self, board) -> int:
        """ Get better strategic movement

        Parameters
        ----------
        board: Board
            Playing board with game status

        Returns
        -------
            move: int
        """
        if (move := self.chooseRandomMoveFromList(board, [1, 3, 7, 9])) is not None:
            return move

        if board.isFreeSpace(5):
            return 5

        return self.chooseRandomMoveFromList(board, [2, 4, 6, 8])

    def getMove(self, board: Board) -> int:
        """ Get better movement

        Parameters
        ----------
        board: Board
            Playing board with game status

        Returns
        -------
            move: int
        """
        if board.isEmpty:
            return self.getStrategyMove(board)
        elif (move := self.search(board)) is not None and move != 0:
            return move
        else:
            return self.getStrategyMove(board)

    @staticmethod
    def iterBoard(board: Board, letter: str) -> Iterator[Union[Board, int]]:
        """ Iter on the board

        Parameters
        ----------

        board: Board
            Playing board with game status
        letter: str
            Player letter to assing the board

        Returns
        -------
            iterator[Board(copy with current move), int -> move]
        """
        for move in range(1, 10):
            copy = board.copy()  # Copy current board

            if copy.isFreeSpace(move):
                copy.makeMove(letter, move)

                if copy.isWinner(letter):
                    yield copy, move
                else:
                    yield copy, 0

    def search(self, board: Board) -> int:
        """ Search Victorious Play

        Parameters
        ----------

        board: Board
            Playing board with game status

        Returns
        -------
            move: int
        """
        self.moves = []

        if (move := self._search(board)) is not None:
            return move[0]

        # Best play for victory
        if len((move := sorted(self.moves, key=lambda x: x[1]))) > 1:
            return move[0][0]
        else:
            return 0

    def _search(self, board: Board, upper: int = 0) -> None:
        """ Search Victorious Play

        Parameters
        ----------

        board: Board
            Playing board with game status
        upper: int, default = 0
            Current iteration Used for ranking plays for
            victory with smaller number of plays.

        Returns
        -------
            None, utilize self.moves instance attribute
        """
        # Direct victory
        # Check all available players who provide direct victory
        for _, pcMove in self.iterBoard(board, self.computerLetter):
            if pcMove:
                return [pcMove, upper + 1]

        # Direct defense
        # Checks every possible opponent's play that supplies a direct victory
        for _, playerMove in self.iterBoard(board, self.playerLetter):
            if playerMove:
                return [playerMove, upper + 1]

        # Search
        # Verifies recursively if each move can provide a victory
        for pcBoard, _ in self.iterBoard(board, self.computerLetter):

            if not pcBoard.isFull:

                for playerBoard, _ in self.iterBoard(pcBoard, self.playerLetter):

                    if not playerBoard.isFull:
                        move = self._search(playerBoard, upper+1)
                        if move is not None and move not in self.moves:
                            self.moves.append(move)
