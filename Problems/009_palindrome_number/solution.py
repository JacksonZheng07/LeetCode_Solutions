class Solution(object):
    def isPalindrome(self, x):
        x = str(x)  # convert integer to string to simplify comparison
        newN = ''   # will store the reversed number as string
        Numb = []   # list to store each character

        # Convert string to list of characters
        for i in x:
            Numb.append(i)

        # Reverse the list
        Numb.reverse()

        # Reconstruct the reversed string
        for n in Numb:
            newN += n

        # Check if reversed string matches original
        if newN == x:
            return True
        else:
            return False
