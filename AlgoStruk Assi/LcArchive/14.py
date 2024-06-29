class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        for i in range(len(strs[0])):
            for string in strs[1:]:
                if i >= len(string) or string[i] != strs[0][i]:
                    return strs[0][:i]
                   
        return strs[0]
    
# Test the function
strs = ["flower","flow","flight"]
print(Solution().longestCommonPrefix(strs))  # Output: "
strs = ["dog","racecar","car"]
print(Solution().longestCommonPrefix(strs))  # Output: ""
strs = ["flower","flower","flower"]
print(Solution().longestCommonPrefix(strs))  # Output: "flower"
strs = ["flower","flower","flower","flower"]
print(Solution().longestCommonPrefix(strs))  # Output: "flower"