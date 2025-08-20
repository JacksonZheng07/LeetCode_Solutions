# 34. Find First and Last Position of Element in Sorted Array

**Difficulty:** Medium  
**Topics:** Binary Search  

## Problem

Given an array `nums` sorted in ascending order and a `target`, return the **starting and ending position** of `target` in `nums`.  
If `target` is not found, return `[-1, -1]`.

### Examples

**Example 1**  
Input: `nums = [5,7,7,8,8,10]`, `target = 8`  
Output: `[3,4]`  

**Example 2**  
Input: `nums = [5,7,7,8,8,10]`, `target = 6`  
Output: `[-1,-1]`  

**Example 3**  
Input: `nums = []`, `target = 0`  
Output: `[-1,-1]`  

---

### Intuition

- Use **binary search** to find the **first** and **last occurrence** of the target separately.  
- This avoids a linear scan and ensures **O(log n)** time complexity.

---

### Algorithm 

1. Define a helper `compare(state, nums, target)`:
   - `state = True` → find first occurrence.  
   - `state = False` → find last occurrence.  
   - Perform standard binary search:
     - If `nums[mid] == target`:
       - Save `mid` in `result`.
       - Move left (`r = mid - 1`) if finding first occurrence.
       - Move right (`l = mid + 1`) if finding last occurrence.
     - If `nums[mid] > target`, move left.
     - Else, move right.
2. Call `compare(True, nums, target)` to get the start index.
3. Call `compare(False, nums, target)` to get the end index.
4. Return `[start, end]`.

---

### Complexity

- **Time Complexity:** `O(log n)` — binary search twice.  
---