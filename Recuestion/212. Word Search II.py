from typing import List

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # Build Trie
        trie = {}
        for word in words:
            node = trie
            for ch in word:
                node = node.setdefault(ch, {})
            node["#"] = word  # End marker
        
        res = []
        rows, cols = len(board), len(board[0])
        
        def dfs(r, c, node):
            ch = board[r][c]
            if ch not in node:
                return
            nxt = node[ch]
            
            # Found a word
            if "#" in nxt:
                res.append(nxt["#"])
                del nxt["#"]  # avoid duplicates
            
            board[r][c] = "*"  # mark visited
            
            for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                nr, nc = r+dr, c+dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] != "*":
                    dfs(nr, nc, nxt)
            
            board[r][c] = ch  # restore
            
            # Optimization: prune empty nodes
            if not nxt:
                node.pop(ch)
        
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, trie)
        
        return res
sol = Solution()
board = [
  ["o","a","a","n"],
  ["e","t","a","e"],
  ["i","h","k","r"],
  ["i","f","l","v"]
]
words = ["oath","pea","eat","rain"]

print(sol.findWords(board, words))
# Output: ["oath","eat"]
