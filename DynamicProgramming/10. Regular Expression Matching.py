class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # DP table: dp[i][j] means s[:i] matches p[:j]
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        dp[0][0] = True  # empty string matches empty pattern
        
        # Handle patterns like a*, a*b*, a*b*c* that can match empty string
        for j in range(2, len(p) + 1):
            if p[j-1] == '*':
                dp[0][j] = dp[0][j-2]
        
        # Fill DP table
        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if p[j-1] == s[i-1] or p[j-1] == '.':
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == '*':
                    # Case 1: '*' means zero occurrence of previous char
                    dp[i][j] = dp[i][j-2]
                    
                    # Case 2: '*' means one or more occurrence
                    if p[j-2] == s[i-1] or p[j-2] == '.':
                        dp[i][j] = dp[i][j] or dp[i-1][j]
        
        return dp[len(s)][len(p)]
s = "aab"
p = "c*a*b"
print(Solution().isMatch(s, p))  # Output: True
