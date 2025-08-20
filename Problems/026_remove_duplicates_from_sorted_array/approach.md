# 26. Remove Duplicates from Sorted Array

**Difficulty:** Easy  
**Topics:** Array  

## Problem

Given a sorted array `nums`, remove the duplicates **in-place** such that each element appears only once and return the new length.  

Do not allocate extra space for another array; you must do this by modifying the input array in-place with `O(1)` extra memory.

### Examples

**Example 1**  
Input: `nums = [1,1,2]`  
Output: `2`  
Explanation: The array is modified to `[1,2]`.

**Example 2**  
Input: `nums = [0,0,1,1,1,2,2,3,3,4]`  
Output: `5`  
Explanation: The array is modified to `[0,1,2,3,4]`.

---

### Intuition  

- Since the array is sorted, duplicates are consecutive.  
- Use **two pointers**:
  - `i` tracks the position of the last unique element.
  - `j` scans through the array for new unique elements.

---

### Algorithm 

1. Initialize `i = 0` to point to the first element.  
2. Loop `j` from 1 to `len(nums) - 1`:
   - If `nums[j] != nums[i]`:
     - Increment `i`.
     - Move `nums[j]` to `nums[i]`.  
3. Return `i + 1` as the new length of unique elements.

---

### Complexity

- **Time Complexity:** `O(n)` — each element is visited once.  
---