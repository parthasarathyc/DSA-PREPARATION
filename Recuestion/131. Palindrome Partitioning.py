from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        
        def isPalindrome(sub: str) -> bool:
            return sub == sub[::-1]
        
        def backtrack(start, path):
            if start == len(s):
                res.append(path[:])
                return
            
            for end in range(start+1, len(s)+1):
                sub = s[start:end]
                if isPalindrome(sub):
                    path.append(sub)
                    backtrack(end, path)
                    path.pop()
        
        backtrack(0, [])
        return res
sol = Solution()
print(sol.partition("aab"))
# Output: [["a","a","b"], ["aa","b"]]

print(sol.partition("a"))
# Output: [["a"]]
