# Sudoku Solver
from solvers.algorithms import dancing_links
from solvers.sudoku.constants import *
from solvers.sudoku.convertor import convert_grid_to_exact_cover


class SudokuSolver(object):
    """
    This class solves a sudoku. Example:
    sudoku_solver = SudokuSolver()
    sudoku_solver[1,1] = 3
    sudoku_solver[1,4] = 5
    ...
    ...
    sudoku_solver[7,8] = 9
    Calling `sudoku_solver.solve()` will return a solved sudoku grid.
    """

    def __init__(self):
        self._grid = [[0 for _ in range(9)] for _ in range(9)]

    def __getitem__(self, index):
        row, column = index
        return self._grid[row - 1][column - 1]

    def __setitem__(self, index, value):
        row, column = index
        self._grid[row - 1][column - 1] = value

    def solve(self):
        columns_to_rows, rows_to_columns = convert_grid_to_exact_cover(self)
        row_indices = dancing_links.solve(columns_to_rows, rows_to_columns, None)
        if row_indices is None:
            raise Exception("Sudoku is unsolvable")
        for row_index in row_indices:
            row, column, value = parse_index(row_index)
            current_value = self[row, column]
            if current_value != 0 and current_value != value:
                raise Exception("Sudoku is unsolvable")
            self[row, column] = value
        return self

    def __str__(self):
        row_strings = []
        for row in self._grid:
            row_strings.append(SUDOKU_ROW_FORMAT.format(*map(lambda v: v if v != 0 else ".", row)))
        return SUDOKU_FINAL_FORMAT.format(*row_strings)

    def __repr__(self):
        return "SudokuSolver{\n" + str(self) + "\n}";
