"""
Minesweeper
~~~~~~~~~~~
"""

from typing import List


class Minesweeper(object):
    """Minesweeper"""
    
    def __init__(self):
        """Constructor"""
        pass


    def is_valid_cell(self, board: List[List[tuple]], row: int, column: int) -> bool:
        """Check if the column and row position of a board is valid.

        Args:
            board (list): A 2 dimension list of the board.
            column (int): The column position of the cell.
            row (int): The row position of the cell.

        Returns:
            A boolean of whether the cell is valid.
        """
        
        return False


    def create_board(self, row: int, column: int, mine: List[tuple]) -> List[List[tuple]]:
        """Create the board.

        Args:
            row (int): The number of row(s) for the board.
            column (int): The number of column(s) for the board.
            mine(list): The location of mine(s) with their coordinate.

        Returns:
            A 2 dimension list of the board.
        """
        
        # c = (i for i in range(width))
        # r = (j for j in range(height))

        # Create a new board
        board = [ [ (r, c, '0#') for c in range(column) ] for r in range(row) ]

        # Add the mine(s) to the board
        for m in mine:
            # The row of the mine
            m_r = m[0]
            # The column of the mine
            m_c = m[1]

            # Set the mine
            board[m_r][m_c] = (m_r, m_c, '0M')

        return board

    
    def display_board(self, board: List[List[tuple]]):
        """Display the board.

        Args:
            board (list): A 2 dimension list of the board.
        """

        # Print the board using `join`
        # print('\n')
        # print('\n'.join([
        #     ' '.join([
        #         f'{item}' for item in row
        #     ]) for row in board
        # ]))

        # Print the board using `for`
        print('\n')
        for row in board:
            print(' '.join(f'{item}' for item in row))