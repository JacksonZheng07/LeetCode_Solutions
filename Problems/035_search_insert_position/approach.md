# 35. Search Insert Position

**Difficulty:** Easy  
**Topics:** Binary Search  

## Problem

Given a sorted array `nums` and a `target`, return the index if the `target` is found.  
If not, return the **index where it would be inserted in order**.

### Examples

**Example 1**  
Input: `nums = [1,3,5,6]`, `target = 5`  
Output: `2`  

**Example 2**  
Input: `nums = [1,3,5,6]`, `target = 2`  
Output: `1`  

**Example 3**  
Input: `nums = [1,3,5,6]`, `target = 7`  
Output: `4`  

---

### Intuition

- Since the array is **sorted**, use **binary search** to find the target efficiently.  
- If the target is not present, `left` will point to the position where it should be inserted.

---

### Algorithm 

1. Initialize `left = 0` and `right = len(nums) - 1`.  
2. While `left <= right`:
   - Compute `mid = left + (right - left) // 2`.  
   - If `nums[mid] == target`, return `mid`.  
   - If `nums[mid] > target`, move `right = mid - 1`.  
   - Else, move `left = mid + 1`.  
3. Return `left` as the insert position.

---

### Complexity

- **Time Complexity:** `O(log n)` — binary search.  
---