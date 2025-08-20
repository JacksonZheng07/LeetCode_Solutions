# 28. Find the Index of the First Occurrence in a String

**Difficulty:** Easy  
**Topics:** String, Sliding Window  

## Problem

Implement `strStr()`. Given two strings `haystack` and `needle`, return the index of the **first occurrence** of `needle` in `haystack`, or `-1` if `needle` is not part of `haystack`.

### Examples

**Example 1**  
Input: `haystack = "hello"`, `needle = "ll"`  
Output: `2`  

**Example 2**  
Input: `haystack = "aaaaa"`, `needle = "bba"`  
Output: `-1`  

**Example 3**  
Input: `haystack = ""`, `needle = ""`  
Output: `0`  

---

### Intuition  

- The problem is asking for the first index where the substring `needle` appears in `haystack`.  
- Python provides a **built-in string method `.find()`** that returns the first index or `-1` if not found.

---

### Algorithm 

1. Use `haystack.find(needle)` to get the first index of `needle`.  
2. Return the result.

---

### Complexity

- **Time Complexity:** `O(n*m)` in the worst case for naive substring search (where `n` is the length of `haystack` and `m` is the length of `needle`).  
---