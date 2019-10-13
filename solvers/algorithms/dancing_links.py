# Solves the Sudoku using dancing links algorithm using implementation from:
# https://www.cs.mcgill.ca/~aassaf9/python/algorithm_x.html


def solve(columns_to_rows, rows_to_columns, solution=None):
    """
    This function solves the exact cover problem, i.e., given a matrix A in which each element is 0 or 1.
    Is there a subset of rows which have exactly one 1 in each column?
    The exact cover problem can also be stated as following,
    "Given a set X and a set of subsets of X called Y, is there a subset of Y such that all of its elements
    are disjoint and union of its elements is X."
    :param columns_to_rows: It is a dictionary where value of key `i` is the set of columns in which ith row is 1.
    :param rows_to_columns: It is a dictionary where value of key `i` is the set of rows in which ith column is 1.
    :param solution: gru selected rows
    :return:
    """
    if solution is None:
        solution = []

    if 'Index{1-2:3}' in solution and 'Index{1-3:2}' in solution and len(solution) == 81:
        import pprint
        pprint.pprint(solution)

    if not columns_to_rows:
        return list(solution)
    else:
        # Column with minimum 1's in it.
        selected_column = min(columns_to_rows, key=lambda col: len(columns_to_rows[col]))
        # For each row which has a 1 in the `selected_column`.
        for selected_row in columns_to_rows[selected_column]:
            solution.append(selected_row)
            # Select and remove all columns which have 1's in the `selected_row`
            # Also remove all the rows which have 1's in the same column as the `selected_row`
            removed_columns = select_and_remove(columns_to_rows, rows_to_columns, selected_row)
            tmp = solve(columns_to_rows, rows_to_columns, solution)
            if tmp is not None:
                return tmp
            deselect_and_insert(columns_to_rows, rows_to_columns, selected_row, removed_columns)
            solution.pop()


def select_and_remove(column_to_rows, rows_to_columns, selected_row):
    """
    This method selects each of the columns which have 1 in the selected row.
    Then removes all the rows which have 1's in the selected column from all the corresponding columns.
    Then removes the selected column from `column_to_rows` map.
    :param column_to_rows: It is a dictionary where value of key `i` is the set of columns in which ith row is 1.
    :param rows_to_columns: It is a dictionary where value of key `i` is the set of rows in which ith column is 1.
    :param selected_row: Row to be selected
    :return: Returns the list of lists of rows which where removed
    """
    removed_columns = []
    # For each column in which `selected_row` is 1.
    for selected_column in rows_to_columns[selected_row]:
        # For each row which has 1 in the `selected_column`.
        for row in column_to_rows[selected_column]:
            # For each column other than `selected_column` which has 1 in the `row`,
            # Remove `row` from it.
            for column in rows_to_columns[row]:
                if column != selected_column and row in column_to_rows[column]:
                    column_to_rows[column].remove(row)
        removed_columns.append(column_to_rows.pop(selected_column))
    return removed_columns


def deselect_and_insert(column_to_rows, rows_to_columns, selected_row, removed_columns):
    """
    This method undo's the `select_and_remove`.
    :param column_to_rows: It is a dictionary where value of key `i` is the set of columns in which ith row is 1.
    :param rows_to_columns: It is a dictionary where value of key `i` is the set of rows in which ith column is 1.
    :param selected_row: Row that was selected
    :param removed_columns: List of columns that were removed
    :return: Returns None.
    """
    # For each column that had a 1 in the `selected_row`, i.e, that was removed
    for removed_column in reversed(rows_to_columns[selected_row]):
        # Add the list of rows of that column back to the matrix.
        column_to_rows[removed_column] = removed_columns.pop()
        # For each row of the `removed_column` that has a 1
        for row in column_to_rows[removed_column]:
            # For each column of `row` that has a 1.
            for column in rows_to_columns[row]:
                if column != removed_column:
                    column_to_rows[column].add(row)
