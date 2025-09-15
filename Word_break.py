
class Solution(object):
    def word_break(self, s, wordDict):
        word_set = set(wordDict)
        hash_map = {}

        def backtracking(s):
            if s == "":
                return True
            for word in word_set:
                if s.startswith(word):
                    hash_map[word] = True
                    return backtracking(s[len(word):])
            hash_map[s] = False
            return False

        return backtracking(s)

def main():
    s = "abcd"
    wordDict = ["ab", "cd", "e"]

    sol = Solution()
    result = sol.word_break(s, wordDict)
    print(result)

if __name__ == "__main__":
    main()
