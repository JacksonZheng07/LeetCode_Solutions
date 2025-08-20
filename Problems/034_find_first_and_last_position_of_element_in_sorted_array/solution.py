class Solution:
    def compare(self, state, nums, target):
        """
        Helper function to find the first or last occurrence of target.

        state = True  -> find first occurrence
        state = False -> find last occurrence
        """
        n = len(nums)
        l, r, result = 0, n - 1, -1

        while r >= l:
            mid = (r + l) // 2
            if nums[mid] == target:
                result = mid
                if state:
                    # Move left to find first occurrence
                    r = mid - 1
                else:
                    # Move right to find last occurrence
                    l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1

        return result

    def searchRange(self, nums, target):
        """
        Returns the start and end indices of target in nums.
        """
        start = self.compare(True, nums, target)  # First occurrence
        end = self.compare(False, nums, target)  # Last occurrence
        return [start, end]
