class Solution(object):
    def isValid(self, s):
        stack = []  # Use a stack (list) to track opening brackets
        mapping = {')': '(', '}': '{', ']': '['}  # Map closing to opening

        for char in s:
            if char in '({[':  # Opening bracket
                stack.append(char)
            else:  # Closing bracket
                if not stack:  # No matching opening bracket
                    return False
                top_element = stack.pop()  # Pop last opening bracket
                if mapping[char] != top_element:  # Mismatch
                    return False

        return not stack  # True if all brackets matched
