#problem 2027 leetcode
# 2027. Minimum Moves to Convert String
class Solution:
    def minimumMoves(self, s: str) -> int:
        i = 0
        n = len(s)
        count = 0
        while i < n:
            if s[i] == 'X':
                count += 1
                i += 3
            else:
                i += 1
        return count
# Test the function
s = "XXX"
print(Solution().minimumMoves(s))  # Output: 1

