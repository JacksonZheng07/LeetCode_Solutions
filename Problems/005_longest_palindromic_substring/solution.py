class Solution(object):
    def longestPalindrome(self, s):
        longest = ''  # stores the longest palindromic substring found

        for i in range(len(s)):
            # --- Check for odd-length palindrome centered at i ---
            current = s[i]  # start with the single character at index i
            deviation = 1    # how far to expand on both sides
            while i - deviation >= 0 and i + deviation < len(s) and s[i - deviation] == s[i + deviation]:
                # Expand outward while characters on both sides match
                current = s[i - deviation] + current + s[i + deviation]
                deviation += 1
            # Update longest palindrome if this one is longer
            if len(current) > len(longest):
                longest = current

            # --- Check for even-length palindrome centered between i and i+1 ---
            current = ''   # reset current for even-length palindrome
            deviation = 0  # start expanding from the center gap
            while i - deviation >= 0 and i + 1 + deviation < len(s) and s[i - deviation] == s[i + 1 + deviation]:
                # Expand outward while characters on both sides match
                current = s[i - deviation] + current + s[i + 1 + deviation]
                deviation += 1
            # Update longest palindrome if this one is longer
            if len(current) > len(longest):
                longest = current

        return longest
