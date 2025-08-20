class Solution(object):
    def longestValidParentheses(self, s):
        stack = [-1]  # Initialize stack with -1 to handle edge case for first valid substring
        max_len = 0

        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)  # Push index of '(' onto stack
            else:
                stack.pop()  # Pop the last '(' index
                if not stack:
                    stack.append(i)  # If stack empty, push current index as new base
                else:
                    # Calculate length of current valid substring
                    max_len = max(max_len, i - stack[-1])

        return max_len
