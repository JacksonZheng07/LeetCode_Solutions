class Solution:
    def threeSum(self, nums):
        nums.sort()  # Sort the array to use two-pointer technique
        l = []       # Store the resulting triplets

        # Loop through each number as the first element of triplet
        for i in range(len(nums)):
            # Skip duplicates for the first element
            if i > 0 and nums[i-1] == nums[i]:
                continue

            j = i + 1          # Left pointer
            k = len(nums) - 1  # Right pointer

            while j < k:
                s = nums[i] + nums[j] + nums[k]

                if s > 0:       # Sum too large, move right pointer left
                    k -= 1
                elif s < 0:     # Sum too small, move left pointer right
                    j += 1
                else:
                    l.append([nums[i], nums[j], nums[k]])  # Found a triplet
                    j += 1
                    # Skip duplicates for the second element
                    while j < k and nums[j-1] == nums[j]:
                        j += 1

        return l
