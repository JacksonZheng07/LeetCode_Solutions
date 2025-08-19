# 1. Two Sum
**Difficulty:** Easy
**Topics:** Array, Hash Map

## Problem
Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.  

- Each input has **exactly one solution**.  
- You may **not use the same element twice**.  
- You can return the answer in **any order**.  

### Examples
**Example 1**  
Input: `nums = [2,7,11,15], target = 9`  
Output: `[0,1]`  
Explanation: Because `nums[0] + nums[1] == 9`, we return `[0, 1]`.  

**Example 2**  
Input: `nums = [3,2,4], target = 6`  
Output: `[1,2]`  

**Example 3**  
Input: `nums = [3,3], target = 6`  
Output: `[0,1]`  

### Constraints
- `2 <= nums.length <= 10^4`  
- `-10^9 <= nums[i] <= 10^9`  
- `-10^9 <= target <= 10^9`  
- Only **one valid answer** exists  

---

### Intuition
The problem asks for two numbers that sum to a target.

- Instead of checking every pair (O(n²)), we can use a hash map (dictionary) to remember numbers we’ve seen.

- For each number num, the complement target - num tells us what number we need to complete the sum.

- If the complement already exists in the hash map, we’ve found the solution.

- This allows us to find the pair in a single pass through the array.

---

### Algorithm (Brute Force)
1. Create an empty dictionary num_to_index to map numbers to their indices.
2. Loop through the array using enumerate(nums) to get both index i and value num.
3. Compute the complement: complement = target - num.
4. Check if complement is already in num_to_index.
5. If yes, return [num_to_index[complement], i].
6. If not, store num in the dictionary: num_to_index[num] = i.
7. Continue until the solution is found.
8. (Optional) Return -1 if no solution is found, though the problem guarantees one.

---
### Time Complexity

- We iterate through the array once.  
- Dictionary lookups (`complement in num_to_index`) and insertions are O(1) on average.  
- Therefore, total time is linear with respect to the number of elements.

---

