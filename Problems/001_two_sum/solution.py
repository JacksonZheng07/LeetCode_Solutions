class Solution(object):
    def twoSum(self, nums, target):
        # Dictionary to store numbers and their indices
        num_to_index = {}

        # Iterate through the array
        for i, num in enumerate(nums):
            # Calculate the number needed to reach the target
            complement = target - num

            # If complement exists in dictionary, return the pair of indices
            if complement in num_to_index:
                return [num_to_index[complement], i]

            # Store the current number with its index
            num_to_index[num] = i

        # Return -1 if no solution is found (problem guarantees a solution)
        return -1
