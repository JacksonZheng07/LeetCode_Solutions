# 17. Letter Combinations of a Phone Number

**Difficulty:** Medium  
**Topics:** Backtracking  

## Problem

Given a string containing digits from 2-9 inclusive, return all possible **letter combinations** the number could represent.  
- Return the answer in **any order**.  
- Use the standard telephone mapping of digits to letters.

### Examples

**Example 1**  
Input: `digits = "23"`  
Output: `["ad","ae","af","bd","be","bf","cd","ce","cf"]`  

**Example 2**  
Input: `digits = ""`  
Output: `[]`  

**Example 3**  
Input: `digits = "2"`  
Output: `["a","b","c"]`  

---

### Intuition  

- Each digit maps to a set of letters.  
- We want all **combinations of letters** for the sequence of digits.  
- **Backtracking** is ideal to explore all paths efficiently.

---

### Algorithm 
1. Handle empty input by returning `[]`.  
2. Define a mapping `phone` from digits to letters.  
3. Initialize an empty list `res` to store results.  
4. Define a recursive function `backtrack(combination, next_digits)`:
   - If no more digits remain, append the current combination to `res`.  
   - Otherwise, loop through letters corresponding to the first remaining digit, and recursively call `backtrack` with updated combination and remaining digits.  
5. Start recursion with `backtrack("", digits)`.  
6. Return `res`.

---

### Complexity

- **Time Complexity:** `O(3^N * 4^M)` — N is the number of digits mapping to 3 letters, M is the number mapping to 4 letters (like '7' and '9').  
---