class Solution(object):
    def convert(self, s, numRows):
        # If only one row, zigzag is just the original string
        if numRows == 1:
            return s

        # ListAll will hold a list of characters for each row
        ListAll = []
        Combine = ''  # Final output string

        # Initialize empty lists for each row
        for i in range(numRows):
            ListAll.append([])

        descending = True  # Direction flag: True = moving down, False = moving up
        row = 1  # Start at the first row (1-based indexing in this implementation)

        # Special handling for 2 rows
        if numRows == 2:
            num = 1
            for letter in s:
                if num == 1:
                    ListAll[0].append(letter)  # Add to first row
                    num -= 1
                else:
                    ListAll[1].append(letter)  # Add to second row
                    num += 1
        else:
            # General case for numRows > 2
            for letter in s:
                if row > numRows:
                    # Reached bottom row, switch direction to up
                    row = numRows - 1
                    descending = False
                    ListAll[row - 1].append(letter)
                    row -= 1
                elif row == 1:
                    # Reached top row, switch direction to down
                    ListAll[row - 1].append(letter)
                    row += 1
                    descending = True
                else:
                    # Middle rows
                    ListAll[row - 1].append(letter)
                    if descending:
                        row += 1  # Move down
                    else:
                        row -= 1  # Move up

        # Combine all rows into a single string
        for lists in ListAll:
            for letter in lists:
                Combine += letter

        return Combine
