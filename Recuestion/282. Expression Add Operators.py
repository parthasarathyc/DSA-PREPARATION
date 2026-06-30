from typing import List

class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        res = []
        
        def backtrack(index, expr, value, last):
            # Base case: reached end of string
            if index == len(num):
                if value == target:
                    res.append(expr)
                return
            
            for i in range(index, len(num)):
                # Avoid numbers with leading zeros
                if i > index and num[index] == "0":
                    break
                
                curr_str = num[index:i+1]
                curr_num = int(curr_str)
                
                if index == 0:
                    # First number, no operator
                    backtrack(i+1, curr_str, curr_num, curr_num)
                else:
                    # Try '+'
                    backtrack(i+1, expr + "+" + curr_str, value + curr_num, curr_num)
                    # Try '-'
                    backtrack(i+1, expr + "-" + curr_str, value - curr_num, -curr_num)
                    # Try '*'
                    backtrack(i+1, expr + "*" + curr_str, value - last + last * curr_num, last * curr_num)
        
        backtrack(0, "", 0, 0)
        return res
sol = Solution()
print(sol.addOperators("123", 6))
# Output: ["1+2+3", "1*2*3"]

print(sol.addOperators("232", 8))
# Output: ["2*3+2", "2+3*2"]

print(sol.addOperators("105", 5))
# Output: ["1*0+5", "10-5"]

print(sol.addOperators("00", 0))
# Output: ["0+0", "0-0", "0*0"]

print(sol.addOperators("3456237490", 9191))
# Output: []
