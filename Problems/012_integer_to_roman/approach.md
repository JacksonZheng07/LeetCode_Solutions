# 12. Integer to Roman

**Difficulty:** Medium  
**Topics:** Math, String

## Problem

Convert an integer to a Roman numeral.

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

- Some numbers use subtractive notation: IV = 4, IX = 9, XL = 40, XC = 90, CD = 400, CM = 900.

### Examples

**Example 1**  
Input: `num = 3`  
Output: `"III"`  

**Example 2**  
Input: `num = 58`  
Output: `"LVIII"`  
Explanation: `50 = L, 5 = V, 3 = III`  

**Example 3**  
Input: `num = 1994`  
Output: `"MCMXCIV"`  
Explanation: `1000 = M, 900 = CM, 90 = XC, 4 = IV`  

---

### Intuition  

- Start from the largest Roman numeral and subtract its value from the number.  
- Append the corresponding Roman numeral to the result.  
- Repeat until the number reduces to zero.  
- Subtractive notation is handled naturally in the mapping.

---

### Algorithm 
1. Create a dictionary mapping integers to Roman numerals, including subtractive values.  
2. Initialize an empty string `Roman`.  
3. Iterate over the integer values from largest to smallest.  
   - While `num >= value`, append corresponding Roman numeral and subtract value.  
4. Continue until `num` becomes zero.  
5. Return `Roman`.

---

### Complexity
- **Time Complexity:** `O(n)` — `n` is the number of Roman numerals added (proportional to `num`).  
---