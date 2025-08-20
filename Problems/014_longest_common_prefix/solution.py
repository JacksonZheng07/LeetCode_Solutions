class Solution(object):
    def longestCommonPrefix(self, strs):
        pre = ''  # store the common prefix

        # Loop through characters of the first string
        for i in range(len(strs[0])):
            letter = strs[0][i]  # current character to compare

            # Compare the current character with the same position in all strings
            for item in strs:
                # If index exceeds string length or character doesn't match, return prefix
                if i >= len(item) or item[i] != letter:
                    return pre
            pre += letter  # all strings have this character, add to prefix

        return pre  # return full prefix if loop completes
