# 33. Search in Rotated Sorted Array

**Difficulty:** Medium  
**Topics:** Binary Search  

## Problem

Given an array `nums` sorted in ascending order, **rotated at an unknown pivot**, and an integer `target`, return the index of `target` if it exists, otherwise return `-1`.

### Examples

**Example 1**  
Input: `nums = [4,5,6,7,0,1,2]`, `target = 0`  
Output: `4`  

**Example 2**  
Input: `nums = [4,5,6,7,0,1,2]`, `target = 3`  
Output: `-1`  

**Example 3**  
Input: `nums = [1]`, `target = 0`  
Output: `-1`  

---

### Intuition  

- The simplest approach is to **check if the target exists** and then **search linearly**.  
- This is not optimal; a binary search adapted to the rotated array would reduce time complexity.

---

### Algorithm 

1. Check if `target` is in `nums`. If not, return `-1`.  
2. Loop through the array:
   - If `nums[i] == target`, return `i`.  
3. If the loop completes without finding the target, return `-1`.

---

### Complexity

- **Time Complexity:** `O(n)` — worst case linear scan.
---