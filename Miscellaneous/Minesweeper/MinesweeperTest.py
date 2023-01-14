"""
Minesweeper
~~~~~~~~~~~
"""

import pytest

from Minesweeper import Minesweeper


class MinesweeperTest(object):
    """Test the Minesweeper class."""

    # def minesweeper
    
    def test_create_board_success(self):
        """Test a successful creation of a board.
        """

        # Create a Minesweeper object
        minesweeper = Minesweeper()

        # Create a board with `column`, `row`, and a list of mine
        board = minesweeper.create_board(4, 5, [(2,0), (3,0)])

        # Test to ensure the correct number of row(s)
        assert len(board) == 4

    
    def test_display_board(self):
        minesweeper = Minesweeper()
        board = minesweeper.create_board(4, 5, [(2,0), (3,0)])

        minesweeper.display_board(board)