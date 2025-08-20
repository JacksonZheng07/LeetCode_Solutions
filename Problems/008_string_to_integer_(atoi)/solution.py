class Solution(object):
    def myAtoi(self, s):
        s = s.strip()  # remove leading/trailing whitespaces O(n)

        # Allowed characters: digits and negative sign
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '-']

        if not s:
            return 0  # empty string after stripping

        # Default sign is positive
        sign = 1
        string = ''  # to store numeric characters

        # Check for sign at the beginning
        if s[0] == '-':
            sign = -1
            s = s[1:]  # remove the sign for further processing
        elif s[0] == '+':
            s = s[1:]

        # Extract continuous numeric characters
        while len(s) > 0:
            if s[0] in numbers[:1]()
