from collections import deque
class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        # implement using bfs
        word_set = set(wordList)
        visited = set([beginWord])
        queue = deque([beginWord])
        result = []

        if endWord not in word_set:
            return []

        while queue:
            solution = []
            for _ in range(len(queue)):
                word = queue.popleft()
                if word == endWord:
                    return result
                for i in range(len(word)):
                    for char in 'abcdefghijklmnopqrstuvwxyz':
                        new_word = word[:i] + char + word[i+1:]
                        if new_word in word_set and new_word not in visited:
                            visited.add(new_word)
                            queue.append(new_word)
                            solution.append(new_word)
            result.append(solution)
        return []

def main():
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
    sol = Solution()
    result = sol.findLadders(beginWord, endWord, wordList)
    print(result)


if __name__ == "__main__":
    main()