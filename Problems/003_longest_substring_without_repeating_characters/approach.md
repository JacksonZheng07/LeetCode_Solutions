# 3. Longest Substring Without Repeating Characters

**Difficulty:** Medium
**Topics:** Hash Map, Sliding Window

## Problem 

Given a string `s`, find the length of the longest substring without duplicate characters.

### Examples

**Example 1**  
Input: `s = "abcabcbb"`  
Output: `3`  
Explanation: The answer is `"abc"`, with the length of 3.

**Example 2**  
Input: `s = "bbbbb"`  
Output: `1`  
Explanation: The answer is `"b"`, with the length of 1.

**Example 3**  
Input: `s = "pwwkew"`  
Output: `3`  
Explanation: The answer is `"wke"`, with the length of 3.  
Notice that the answer must be a substring, `"pwke"` is a subsequence and not a substring.

### Constraints
- `0 <= s.length <= 5 * 104`
- `s consists of English letters, digits, symbols and spaces.`

---
### Intuition  

- Keep track of the current substring without duplicates.  
- When a duplicate character appears, remove characters from the start until the duplicate is gone.  
- Update the longest substring found so far.

---

### Algorithm 
1. Initialize two strings: `Sub` for the current substring, `HighestSub` for the longest substring found.  
2. Loop through each character `letter` in `s`:  
   - If `letter` is already in `Sub`, remove all characters from the start of `Sub` up to and including the first occurrence of `letter`.  
   - Append `letter` to `Sub`.  
   - Update `HighestSub` if `Sub` is longer.  
3. Return the length of `HighestSub`.

---

### Complexity
- **Time Complexity:** `O(n^2)` — `letter in Sub` and `Sub.replace()` can take up to O(n) each. 