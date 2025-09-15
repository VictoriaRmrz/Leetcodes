from collections import defaultdict
class Solution(object):
    def group_anagrams(self, strs):
        hash_map = defaultdict(list)
        for word in strs:
            chars = tuple(sorted(word)) # because it cannot save a list as key
            hash_map[chars].append(word)
        return list(hash_map.values()) # to save them into a list without the defaultDict identifier

def main():
    strs = ["eat","tea","tan","ate","nat","bat"]
    sol = Solution()
    print(sol.group_anagrams(strs))

if __name__ == "__main__":
    main()