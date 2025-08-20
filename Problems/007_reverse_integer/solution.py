class Solution(object):
    def reverse(self, x):
        # Convert the integer to a string to simplify reversal
        Reverse = str(x)

        # Check if the number is negative
        if Reverse[0] == '-':
            Reverse = Reverse.replace('-', "")  # remove the negative sign
            Reverse = Reverse[::-1]             # reverse the digits
            Reverse = '-' + Reverse             # add the negative sign back
        else:
            Reverse = Reverse[::-1]             # reverse digits for positive numbers

        # Check if the reversed integer is within 32-bit signed integer range
        if int(Reverse) > 2**31 - 1 or int(Reverse) < -2**31:
            return 0  # return 0 if it overflows
        else:
            return int(Reverse)  # return the reversed integer
