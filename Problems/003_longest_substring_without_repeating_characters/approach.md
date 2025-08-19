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
We want to find the longest substring that contains no duplicate characters. A brute force approach would check all substrings, but that would be too slow. Instead, we can use a sliding window with a hash map (or set) to keep track of characters we’ve seen.

---

### Algorithm  
1. Initialize two pointers `left` and `right` to represent the sliding window.  
2. Use a hash map (or set) to track which characters are currently in the window.  
3. Expand `right` step by step, adding new characters.  
   - If the character is already in the set, move `left` until the duplicate is removed.  
4. Update the maximum window size whenever we expand.  
5. Continue until the end of the string.  

---

### Complexity  
- **Time Complexity:** `O(n)` – each character is visited at most twice (once by `right`, once by `left`).  