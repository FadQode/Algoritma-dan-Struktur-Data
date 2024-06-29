# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         if x < 0:
#             return False
#         if x < 10:
#             return True
#         x = str(x)
#         sta = []
#         for i in x:
#             print(i)
#             sta.append(i)
#             print(sta)
            
#         pal = []
#         for i in sta:
#             a = sta.pop()
#             pal.append(a)
#             print(a)
#         print(sta, pal)    
#         for i in range(len(sta) - 1):
#             if sta[i] != pal[i]:
#                 return False
#         return  True
class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        print(x[::-1])
        if x == x[::-1]:
            return True
        else:
            return False
# Test the function
x = 10
print(Solution().isPalindrome(123123))  # Output: False