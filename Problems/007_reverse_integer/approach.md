# 7. Reverse Integer

**Difficulty:** Medium  
**Topics:** Math, String Manipulation

## Problem 

Given a signed 32-bit integer `x`, return `x` with its digits reversed.  
- If reversing `x` causes the value to go outside the 32-bit signed integer range `[-2^31, 2^31 - 1]`, return `0`.

### Examples

**Example 1**  
Input: `x = 123`  
Output: `321`  

**Example 2**  
Input: `x = -123`  
Output: `-321`  

**Example 3**  
Input: `x = 120`  
Output: `21`  

---

### Intuition  

- Convert the integer to a string for easy reversal.  
- Handle the negative sign separately.  
- Reverse the digits and convert back to integer.  
- Check for 32-bit overflow.

---

### Algorithm (Implemented Approach)
1. Convert integer `x` to string `Reverse`.  
2. If the first character is `'-'`, remove the sign, reverse the digits, and prepend `'-'`.  
3. Otherwise, just reverse the string.  
4. Convert back to integer.  
5. Check if it falls within the 32-bit signed integer range; if not, return `0`.  
6. Return the reversed integer.

---

### Complexity
- **Time Complexity:** `O(n)` — `n` is the number of digits in `x`.  

---