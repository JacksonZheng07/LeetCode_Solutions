class Solution(object):
    def generateParenthesis(self, n):
        result = []  # Store all valid combinations

        def backtrack(current, open_count, close_count):
            # If the current string has 2*n characters, it's complete
            if len(current) == 2 * n:
                result.append(current)
                return

            # If we can still add an open bracket, do it
            if open_count < n:
                backtrack(current + "(", open_count + 1, close_count)

            # If we can add a closing bracket without breaking validity, do it
            if close_count < open_count:
                backtrack(current + ")", open_count, close_count + 1)

        backtrack("", 0, 0)  # Start the recursion
        return result
