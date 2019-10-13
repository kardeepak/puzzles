# Converts a sudoku grid to a exact cover problem

from solvers.sudoku.constants import *


def convert_grid_to_exact_cover(grid):
    positions = convert_grid_to_positions(grid)
    columns_to_rows = {}
    rows_to_columns = {}
    for position in positions:
        row, column = position

        if row not in rows_to_columns:
            rows_to_columns[row] = list()
        rows_to_columns[row].append(column)

        if column not in columns_to_rows:
            columns_to_rows[column] = set()
        columns_to_rows[column].add(row)
    return columns_to_rows, rows_to_columns


def convert_grid_to_positions(grid):
    positions = []

    for row in range(1, 10):
        for column in range(1, 10):
            current_value = grid[row, column]
            for value in range(1, 10):
                if value == current_value or current_value == 0:
                    positions += get_positions(row, column, value)
    return positions


def get_positions(row, column, value):
    constraints = map(
        lambda constraint: constraint.format(row=row, column=column, box=get_box(row, column), value=value),
        DLX_CONSTRAINTS)
    row_index = DLX_ROW_INDEX.format(row=row, column=column, value=value)
    return map(lambda constraint: (row_index, constraint), constraints)


def get_box(row, column):
    return ((row - 1) // 3) * 3 + (column - 1) // 3 + 1
