from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        
        for word in strs:
            # Key: sorted characters as tuple
            key = tuple(sorted(word))
            groups[key].append(word)
        
        return list(groups.values())
sol = Solution()
print(sol.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
# Output: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]

print(sol.groupAnagrams([""]))
# Output: [['']]

print(sol.groupAnagrams(["a"]))
# Output: [['a']]
