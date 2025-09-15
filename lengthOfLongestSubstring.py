class Solution(object):
    def lengthOfLongestSubstring(self, s):
        saved_chars = set()
        l = 0
        max_length = 0
        if s == "":
            return 0
        
        for r in range(len(s)):
            while s[r] in saved_chars:
                saved_chars.remove(s[l])
                l += 1
            saved_chars.add(s[r])
            max_length = max(max_length, r - l + 1)
        return max_length
    

def main():
    solution = Solution()
    print(solution.lengthOfLongestSubstring("abcabcbb"))  # Output: 3
    print(solution.lengthOfLongestSubstring("bbbbb"))     # Output: 1
    print(solution.lengthOfLongestSubstring("pwwkew"))    # Output: 3
    print(solution.lengthOfLongestSubstring(""))          # Output: 0

if __name__ == "__main__":
    main()