from collections import Counter

class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        if not s or not words:
            return []
        
        word_len = len(words[0])
        word_count = len(words)
        total_len = word_len * word_count
        word_map = Counter(words)
        
        result = []
        
        # We need to check for each possible offset
        for i in range(word_len):
            left = i
            right = i
            window_map = {}
            count = 0
            
            while right + word_len <= len(s):
                word = s[right:right + word_len]
                right += word_len
                
                if word in word_map:
                    window_map[word] = window_map.get(word, 0) + 1
                    count += 1
                    
                    # If word frequency exceeds, shrink from left
                    while window_map[word] > word_map[word]:
                        left_word = s[left:left + word_len]
                        window_map[left_word] -= 1
                        left += word_len
                        count -= 1
                    
                    # If all words matched
                    if count == word_count:
                        result.append(left)
                else:
                    # Reset window
                    window_map.clear()
                    count = 0
                    left = right
        
        return result
s = "barfoothefoobarman"
words = ["foo","bar"]
print(Solution().findSubstring(s, words))  # Output: [0, 9]
