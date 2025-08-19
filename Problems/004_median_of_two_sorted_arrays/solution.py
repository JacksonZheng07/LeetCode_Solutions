class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        # Merge the two arrays
        merged = nums1 + nums2
        merged.sort()  # Sort the combined list

        n = len(merged)

        # If odd number of elements, return the middle one
        if n % 2 == 1:
            return float(merged[n // 2])
        else:
            # If even number of elements, return the average of the two middle elements
            mid1 = merged[n // 2 - 1]
            mid2 = merged[n // 2]
            return (mid1 + mid2) / 2.0
