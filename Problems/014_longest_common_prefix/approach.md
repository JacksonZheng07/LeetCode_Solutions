# 14. Longest Common Prefix

**Difficulty:** Easy  
**Topics:** String  

## Problem

Write a function to find the **longest common prefix** string among an array of strings.  

- If there is no common prefix, return an empty string `""`.

### Examples

**Example 1**  
Input: `strs = ["flower","flow","flight"]`  
Output: `"fl"`  

**Example 2**  
Input: `strs = ["dog","racecar","car"]`  
Output: `""`  
Explanation: There is no common prefix among the input strings.

---

### Intuition  

- The longest common prefix is determined by the **first mismatch** among characters at the same positions in all strings.  
- We can check each character index sequentially and **stop at the first mismatch**.

---

### Algorithm 
1. Initialize an empty string `pre` to store the prefix.  
2. Loop through each character index `i` of the first string.  
3. For each string in the list, check if the character at index `i` matches the first string.  
   - If any string has a mismatch or is shorter than `i + 1`, return `pre`.  
4. If all strings match, append the character to `pre`.  
5. Return `pre` after checking all characters.

---

### Complexity

- **Time Complexity:** `O(S)` — `S` is the sum of all characters in all strings (in worst case, check every character).  
---