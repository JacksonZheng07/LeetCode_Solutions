class Solution(object):
    def lengthOfLongestSubstring(self, s):

        Sub = ''  # Current substring without repeating characters
        HighestSub = ''  # Longest substring found so far

        for letter in s:
            if letter in Sub:
                # If the letter is already in the substring, remove everything
                # up to and including its first occurrence, then add the letter back
                Sub = Sub.replace(Sub[0:Sub.index(letter) + 1], '')
                Sub += letter
            else:
                # Otherwise, just add the new letter to the current substring
                Sub += letter

                # Update longest substring if the current one is longer
                if len(HighestSub) <= len(Sub):
                    HighestSub = Sub

        return len(HighestSub)
