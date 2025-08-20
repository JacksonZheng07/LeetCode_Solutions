# 11. Container With Most Water

**Difficulty:** Medium  
**Topics:** Array, Two Pointers

## Problem

Given `n` non-negative integers `height` where each represents a vertical line at position `i`, find two lines that together with the x-axis form a container, maximizing the area of water it can hold.

- The area of water is determined by the shorter line of the two selected lines multiplied by the distance between them.

### Examples

**Example 1**  
Input: `height = [1,8,6,2,5,4,8,3,7]`  
Output: `49`  
Explanation: The container formed by lines at positions 1 and 8 gives the max area.

**Example 2**  
Input: `height = [1,1]`  
Output: `1`  

---

### Intuition  

- Use two pointers at both ends of the array.  
- The area is determined by the shorter line; moving the taller line inward will not help, so move the shorter line.  
- Continue until pointers meet to check all possible containers.

---

### Algorithm (Implemented Approach)
1. Initialize `HighestArea = 0`.  
2. Set `pointer1` at start, `pointer2` at end.  
3. While `pointer1 < pointer2`:  
   - Compute width = `pointer2 - pointer1`.  
   - Area = width × min(height[pointer1], height[pointer2]).  
   - Update `HighestArea` if area is larger.  
   - Move the pointer pointing to the shorter height inward.  
4. Return `HighestArea`.

---

### Complexity

- **Time Complexity:** `O(n)` — each element is visited once.  
---