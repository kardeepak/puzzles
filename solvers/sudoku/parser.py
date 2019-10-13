# Parses sudoku from single line or grid
from .solver import SudokuSolver
import string


class SudokuParser(object):
    """
    Parses string from a line in the format of all row strings concatenated.
    For empty cells, write '0' or '.'.
    Input string should be of exactly 81 characters excluding spaces and new lines.
    :param input_string: The input string
    :param is_grid: True if the input string is in the grid format
    """
    def __init__(self, input_string: str, is_grid: bool = False):
        input_string = input_string.replace(" ", "").replace("\n", "").strip()
        character_set = set(string.digits) | {"."}
        assert character_set.issuperset(set(input_string)), "Invalid Input String"
        assert len(input_string) == 81, "Invalid input string"
        self.input_string = input_string

    def parse(self):
        grid = SudokuSolver()
        for i in range(1, 10):
            for j in range(1, 10):
                index = (i - 1) * 9 + j
                value = self.input_string[index - 1]
                grid[i, j] = int(value) if value != '.' else 0
        return grid
