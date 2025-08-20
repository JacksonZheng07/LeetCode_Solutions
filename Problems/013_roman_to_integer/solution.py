class Solution(object):
    def romanToInt(self, s):
        # Mapping of Roman numerals to integers
        roman_values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        total = 0        # store the resulting integer
        prev_value = 0   # previous numeral value for subtractive check

        # Iterate through the Roman numeral from right to left
        for char in reversed(s):
            value = roman_values[char]
            # If the current value is smaller than previous, subtract it
            if value < prev_value:
                total -= value
            else:  # otherwise, add it
                total += value
            prev_value = value  # update previous value

        return total
