class Solution(object):
    def search(self, nums, target):
        # Check if target exists in the array
        if target not in nums:
            return -1

        # Linear search to find the index of target
        for i in range(len(nums)):
            if nums[i] == target:
                return i
