class Solution(object):
    def lengthOfLongestSubstring(self, s):
        hash = {}
        l = 0
        max_length = 0
        for r in range(len(s)):
            if s[r] in hash:
                l = hash[s[r]] + 1
            hash[s[r]] = r
            max_length = max(max_length, r - l + 1)
        return max_length


def main():
    solution = Solution()
    print(solution.anotherWay("abcabcbb"))  # Output: 3
    print(solution.anotherWay("bbbbb"))     # Output: 1
    print(solution.anotherWay("pwwkew"))    # Output: 3
    print(solution.anotherWay(""))          # Output: 0

if __name__ == "__main__":
    main()