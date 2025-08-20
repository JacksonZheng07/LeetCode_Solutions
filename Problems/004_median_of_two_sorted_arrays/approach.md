# 4. Median of Two Sorted Arrays

**Difficulty:** Hard
**Topics:** Array, Binary Search

## Problem 

Given two sorted arrays `nums1` and `nums2` of size m and n respectively, return the median of the two sorted arrays.

- The overall run time complexity should be `O(log (m+n))`.


### Examples

**Example 1**  
Input: `nums1 = [1,3], nums2 = [2]`  
Output: `2.00000`  
Explanation: The merged array is `[1,2,3]`, and the median is `2`.

**Example 2**  
Input: `nums1 = [1,2], nums2 = [3,4]`  
Output: `2.50000`  
Explanation: The merged array is `[1,2,3,4]`, and the median is `(2 + 3) / 2 = 2.5`.

### Constraints
- `nums1.length == m`
- `nums2.length == n`
- `0 <= m <= 1000`
- `0 <= n <= 1000`
- `1 <= m + n <= 2000`
- `-106 <= nums1[i], nums2[i] <= 106`

---

### Intuition  

- Merge the two arrays and sort.  
- Use the middle element(s) to compute the median.

---

### Algorithm (Implemented Approach)
1. Merge `nums1` and `nums2` into a single list.  
2. Sort the merged list.  
3. If the total length is odd, return the middle element.  
4. If even, return the average of the two middle elements.

---

### Complexity
- **Time Complexity:** `O((m+n) log(m+n))` — due to sorting. 
---