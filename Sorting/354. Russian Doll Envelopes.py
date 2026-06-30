from typing import List
import bisect

class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        # Step 1: Sort envelopes
        # Sort by width ascending, and if equal, by height descending
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        
        # Step 2: Extract heights
        heights = [h for _, h in envelopes]
        
        # Step 3: Find LIS on heights
        lis = []
        for h in heights:
            idx = bisect.bisect_left(lis, h)
            if idx == len(lis):
                lis.append(h)
            else:
                lis[idx] = h
        return len(lis)
envelopes = [[5,4],[6,4],[6,7],[2,3]]
print(Solution().maxEnvelopes(envelopes))  # Output: 3
