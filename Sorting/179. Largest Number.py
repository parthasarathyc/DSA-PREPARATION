from typing import List
import functools

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # Custom comparator: compare concatenated strings
        def compare(x: str, y: str) -> int:
            if x + y > y + x:
                return -1
            elif x + y < y + x:
                return 1
            else:
                return 0
        
        # Convert to strings for comparison
        nums_str = list(map(str, nums))
        
        # Sort using custom comparator
        nums_str.sort(key=functools.cmp_to_key(compare))
        
        # Edge case: if all numbers are zero
        if nums_str[0] == "0":
            return "0"
        
        return "".join(nums_str)
nums = [3,30,34,5,9]
print(Solution().largestNumber(nums))  # Output: "9534330"
