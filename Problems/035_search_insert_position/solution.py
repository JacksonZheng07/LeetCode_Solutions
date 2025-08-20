class Solution(object):
    def searchInsert(self, nums, target):
        """
        Returns the index where target is found, or the position where it should be inserted.
        """
        left, right = 0, len(nums) - 1

        while right >= left:
            mid = left + (right - left) // 2  # Avoid overflow
            if nums[mid] == target:
                return mid  # Target found
            elif nums[mid] > target:
                right = mid - 1  # Move left
            else:
                left = mid + 1   # Move right

        return left  # Position to insert target
