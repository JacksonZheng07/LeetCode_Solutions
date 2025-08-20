class Solution(object):
    def removeDuplicates(self, nums):
        i = 0  # Pointer for the position of the last unique element
        for j in range(1, len(nums)):
            if nums[i] != nums[j]:  # Found a new unique element
                i += 1
                nums[i] = nums[j]  # Move it to the next position
        return i + 1  # Length of unique elements
