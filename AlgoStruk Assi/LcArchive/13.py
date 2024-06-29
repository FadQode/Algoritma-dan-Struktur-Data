class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            "I": 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000,
        }
        double = {
            "IV" : 4,
            "IX" : 9,
            "XL" : 40,
            "XC" : 90,
            "CD" : 400,
            "CM" : 900,
        }

        n = len(s)
        i = 0
        res = 0
        while i < n:
            if i < n - 1 and s[i:i+2] in double:
                res += double[s[i:i+2]]
                i += 2
            else:
                res += roman[s[i]]
                i += 1
        return res

    
# Test the function
s = "XXVII"
print(Solution().romanToInt(s))  # Output: 3
s = "VVV"
print(Solution().romanToInt(s))  # Output: 4
            