class Solution(object):
    def maxArea(self, height):
        HighestArea = 0           # store the maximum area found
        pointer1 = 0              # left pointer
        pointer2 = len(height) - 1  # right pointer

        # Iterate until pointers meet
        while pointer1 < pointer2:
            diff = pointer2 - pointer1  # width of current container

            # Determine the limiting height
            if height[pointer1] > height[pointer2]:
                Area = diff * height[pointer2]
                pointer2 -= 1  # move right pointer inward
            else:
                Area = diff * height[pointer1]
                pointer1 += 1  # move left pointer inward

            # Update maximum area
            if Area > HighestArea:
                HighestArea = Area

        return HighestArea
