class Solution(object):
    def intToRoman(self, num):
        # Mapping of integer values to Roman numerals
        RNum = {
            1: "I",
            4: "IV",   5: "V",
            9: "IX",   10: "X",
            40: "XL",  50: "L",
            90: "XC",  100: "C",
            400: "CD", 500: "D",
            900: "CM", 1000: "M",
        }
        Roman = ''  # store the resulting Roman numeral

        # Iterate over values from largest to smallest
        for n in [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]:
            # Append Roman numeral while num >= current value
            while n <= num:
                Roman += RNum[n]  # add corresponding Roman numeral
                num -= n          # decrease num by the value added

        return Roman
