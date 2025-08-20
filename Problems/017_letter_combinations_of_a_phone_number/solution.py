class Solution:
    def letterCombinations(self, digits):
        if not digits:  # Handle empty input
            return []

        # Map digits to corresponding letters
        phone = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }
        res = []  # Store all possible combinations

        def backtrack(combination, next_digits):
            # Base case: no more digits to process
            if not next_digits:
                res.append(combination)
                return

            # Loop through letters for the current digit
            for letter in phone[next_digits[0]]:
                # Append letter and continue with remaining digits
                backtrack(combination + letter, next_digits[1:])

        backtrack("", digits)  # Start backtracking
        return res
