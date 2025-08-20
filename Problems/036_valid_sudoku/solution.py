class Solution(object):
    def isValidSudoku(self, board):
        """
        Check if a 9x9 Sudoku board is valid.
        A valid board has no repeated numbers in any row, column, or 3x3 box.
        """
        rows = [set() for _ in range(9)]  # Track numbers seen in each row
        cols = [set() for _ in range(9)]  # Track numbers seen in each column
        boxes = [set() for _ in range(9)]  # Track numbers seen in each 3x3 box

        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val == '.':
                    continue  # Skip empty cells

                # Check row
                if val in rows[i]:
                    return False
                rows[i].add(val)

                # Check column
                if val in cols[j]:
                    return False
                cols[j].add(val)

                # Check 3x3 box
                box_index = (i // 3) * 3 + (j // 3)
                if val in boxes[box_index]:
                    return False
                boxes[box_index].add(val)

        return True  # All checks passed
