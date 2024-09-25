class Solution:
    def intToRoman(self, num: int) -> str:
        # Mapping of integers to their corresponding Roman numeral representations
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
        ]
        
        syms = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
        ]
        
        roman_numeral = ""
        
        # Iterate over the values and symbols
        for i in range(len(val)):
            # While the current value can fit into num, append the corresponding symbol
            while num >= val[i]:
                roman_numeral += syms[i]
                num -= val[i]  # Decrease num by the value
                
        return roman_numeral
