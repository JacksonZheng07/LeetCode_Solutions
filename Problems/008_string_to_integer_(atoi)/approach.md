# 8. String to Integer (atoi)

**Difficulty:** Medium  
**Topics:** String, Math

## Problem

Implement `myAtoi(string s)` to convert a string to a 32-bit signed integer (similar to C/C++ `atoi`).  

- Read in and ignore any leading whitespace.  
- Check for optional `+` or `-` sign.  
- Convert the following numeric characters until a non-digit is encountered.  
- Clamp the integer within the 32-bit signed range `[-2^31, 2^31 - 1]`.

### Examples

**Example 1**  
Input: `s = "42"`  
Output: `42`  

**Example 2**  
Input: `s = "   -42"`  
Output: `-42`  

**Example 3**  
Input: `s = "4193 with words"`  
Output: `4193`  

---

### Intuition  

- Strip leading/trailing spaces first.  
- Identify the optional sign.  
- Read digits sequentially until a non-digit is encountered.  
- Multiply by the sign and clamp the result to 32-bit range.

---

### Algorithm (Implemented Approach)
1. Strip whitespace from the input string.  
2. Initialize sign = 1 and an empty string to collect digits.  
3. Check for `+` or `-` sign at the beginning and adjust sign.  
4. Loop through characters and append digits to the string until a non-digit is found.  
5. Convert the collected digits to integer and apply the sign.  
6. Clamp the integer to the 32-bit signed range.  
7. Return the final integer.

---

### Complexity

- **Time Complexity:** `O(n)` — n = length of string.  
---