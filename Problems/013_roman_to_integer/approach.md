# 13. Roman to Integer

**Difficulty:** Easy  
**Topics:** Math, String

## Problem

Convert a Roman numeral to an integer.

- Roman numerals are represented by these symbols:

| Symbol | Value |
|--------|-------|
| I      | 1     |
| V      | 5     |
| X      | 10    |
| L      | 50    |
| C      | 100   |
| D      | 500   |
| M      | 1000  |

- Roman numerals use **subtractive notation** for numbers like 4 (IV) and 9 (IX).

### Examples

**Example 1**  
Input: `s = "III"`  
Output: `3`  

**Example 2**  
Input: `s = "LVIII"`  
Output: `58`  
Explanation: `L = 50, V = 5, III = 3`  

**Example 3**  
Input: `s = "MCMXCIV"`  
Output: `1994`  
Explanation: `M = 1000, CM = 900, XC = 90, IV = 4`  

---

### Intuition  

- Roman numerals are mostly additive, but a smaller numeral before a larger numeral means subtraction.  
- By iterating from right to left, we can easily handle subtractive notation:  
  - If current numeral < previous numeral, subtract it.  
  - Otherwise, add it.

---

### Algorithm
1. Map Roman symbols to their integer values.  
2. Initialize `total = 0` and `prev_value = 0`.  
3. Loop through the Roman string in reverse:  
   - If `value < prev_value`, subtract `value` from total.  
   - Else, add `value` to total.  
   - Update `prev_value`.  
4. Return `total`.

---

### Complexity

- **Time Complexity:** `O(n)` — iterate through the string once.  
---