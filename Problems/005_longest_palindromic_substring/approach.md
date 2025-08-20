# 5. Longest Palindromic Substring

**Difficulty:** Medium  
**Topics:** String, Dynamic Programming (Expand Around Center)

## Problem 

Given a string `s`, return the longest palindromic substring in `s`.

### Examples

**Example 1**  
Input: `s = "babad"`  
Output: `"bab"` or `"aba"`  
Explanation: Both `"bab"` and `"aba"` are valid palindromic substrings of maximum length.

**Example 2**  
Input: `s = "cbbd"`  
Output: `"bb"`  
Explanation: `"bb"` is the longest palindromic substring.

**Example 3**  
Input: `s = "a"`  
Output: `"a"`  
Explanation: A single character is trivially a palindrome.

---

### Intuition  

- A palindrome mirrors around its center.  
- We can try expanding around each character (and between characters for even-length palindromes) to find the longest one.

---

### Algorithm (Implemented Approach)
1. Initialize an empty string `longest` to store the longest palindrome found.  
2. Loop through each index `i` in `s`:  
   - **Odd-length palindrome:**  
     - Start with `current = s[i]`.  
     - Expand outwards while `s[i - deviation] == s[i + deviation]` and indices are valid.  
     - Update `longest` if `current` is longer.  
   - **Even-length palindrome:**  
     - Start with `current = ''`.  
     - Expand outwards while `s[i - deviation] == s[i + 1 + deviation]` and indices are valid.  
     - Update `longest` if `current` is longer.  
3. Return `longest`.

---

### Complexity
- **Time Complexity:** `O(n^2)` — expanding around each character. 
---