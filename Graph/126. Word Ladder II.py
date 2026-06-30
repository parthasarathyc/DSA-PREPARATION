from collections import defaultdict, deque

class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        wordSet = set(wordList)
        if endWord not in wordSet:
            return []

        # Step 1: BFS to build graph of shortest paths
        parents = defaultdict(set)
        level = {beginWord}
        visited = set()
        found = False

        while level and not found:
            next_level = set()
            for word in level:
                visited.add(word)
            for word in level:
                for i in range(len(word)):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        new_word = word[:i] + c + word[i+1:]
                        if new_word in wordSet and new_word not in visited:
                            if new_word == endWord:
                                found = True
                            next_level.add(new_word)
                            parents[new_word].add(word)
            level = next_level

        # Step 2: Backtrack to build all paths
        res = []
        def dfs(word, path):
            if word == beginWord:
                res.append(path[::-1])
                return
            for p in parents[word]:
                dfs(p, path + [p])

        if found:
            dfs(endWord, [endWord])
        return res
