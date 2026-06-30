class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        # Last occurrence of each character
        last_index = {c: i for i, c in enumerate(s)}
        
        stack = []
        seen = set()
        
        for i, c in enumerate(s):
            if c not in seen:
                # Maintain lexicographical order
                while stack and c < stack[-1] and i < last_index[stack[-1]]:
                    removed = stack.pop()
                    seen.remove(removed)
                stack.append(c)
                seen.add(c)
        
        return "".join(stack)
s = "cbacdcbc"
print(Solution().removeDuplicateLetters(s))  # Output: "acdb"
