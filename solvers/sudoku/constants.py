# Contains string formats for sudoku solver and dancing links algorithm

SUDOKU_HEADER = ".-----.-----.-----."
SUDOKU_ROW_DELIMITER = ":----- ----- -----:"
SUDOKU_FOOTER = "'-----'-----'-----'"
SUDOKU_ROW_FORMAT = "|{} {} {}|{} {} {}|{} {} {}|"
SUDOKU_FINAL_FORMAT = SUDOKU_HEADER \
                      + "\n" "{}\n" "{}\n" "{}\n" \
                      + SUDOKU_ROW_DELIMITER \
                      + "\n" "{}\n" "{}\n" "{}\n" \
                      + SUDOKU_ROW_DELIMITER \
                      + "\n" "{}\n" "{}\n" "{}\n" \
                      + SUDOKU_FOOTER

DLX_ROW_INDEX = "Index{{" "{row}-{column}:{value}" "}}"
DLX_CELL_CONSTRAINT = "Cell{{" "{row}:{column}"  "}}"
DLX_ROW_CONSTRAINT = "Row{{" "{row}:{value}" "}}"
DLX_COLUMN_CONSTRAINT = "Column{{" "{column}:{value}" "}}"
DLX_BOX_CONSTRAINT = "Box{{" "{box}:{value}" "}}"

DLX_CONSTRAINTS = [DLX_CELL_CONSTRAINT, DLX_ROW_CONSTRAINT, DLX_COLUMN_CONSTRAINT, DLX_BOX_CONSTRAINT]


def parse_index(row_index: str):
    row_column_value = row_index.replace("Index{", "").replace("}", "")
    row_column, value = row_column_value.split(":")
    row, column = row_column.split("-")
    return int(row), int(column), int(value)