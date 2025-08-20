# 15. 3Sum

**Difficulty:** Medium  
**Topics:** Array, Two Pointers  

## Problem

Given an array `nums`, return all **unique triplets** `[nums[i], nums[j], nums[k]]` such that:  

- `i != j != k`  
- `nums[i] + nums[j] + nums[k] == 0`  

You may return the answer in **any order**.

### Examples

**Example 1**  
Input: `nums = [-1,0,1,2,-1,-4]`  
Output: `[[-1,-1,2],[-1,0,1]]`  

**Example 2**  
Input: `nums = [0,1,1]`  
Output: `[]`  
Explanation: No triplets sum to 0.

**Example 3**  
Input: `nums = [0,0,0]`  
Output: `[[0,0,0]]`  

---

### Intuition  

- By sorting the array, we can fix one number and use **two pointers** to find pairs summing to its negative.  
- Skipping duplicates ensures only **unique triplets** are added.  

---

### Algorithm 
1. Sort the array `nums`.  
2. Loop through each number `nums[i]` as the first element.  
   - Skip duplicates for `nums[i]`.  
3. Initialize two pointers: `j = i + 1` (left) and `k = len(nums) - 1` (right).  
4. While `j < k`:  
   - Compute `s = nums[i] + nums[j] + nums[k]`.  
   - If `s > 0`, move right pointer `k` left.  
   - If `s < 0`, move left pointer `j` right.  
   - If `s == 0`, append `[nums[i], nums[j], nums[k]]` to results and move `j` skipping duplicates.  
5. Return the list of triplets.

---

### Complexity

- **Time Complexity:** `O(n^2)` — outer loop over `i` and inner two-pointer loop.  
---