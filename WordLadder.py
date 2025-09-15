from collections import deque
class Solution(object):
    def wordladder(self, beginWord, endWord, wordList):
        # Using bfs, treats the problem as a tree
        # try each combination of the alphabet
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0
        queue = deque([beginWord])
        visited = set([beginWord])
        length = 1

        while queue:
            for _ in range(len(queue)):
                word = queue.popleft()
                if word == endWord:
                    return length
                for i in range(len(word)):
                    for char in 'abcdefghijklmnopqrstuvwxyz':
                        new_word = word[:i] + char + word[i+1:]
                        if new_word in wordSet and new_word not in visited:
                            visited.add(new_word)
                            queue.append(new_word)
            length += 1
        return 0


def main():
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot","dot","dog","lot","log","cog"]
    solution = Solution()
    print(solution.wordladder(beginWord, endWord, wordList))

if __name__ == "__main__":
    main()