from collections import defaultdict
class Solution(object):
    def searchingNames(self, book, names):
        name_count = defaultdict(int)
        with open(book,'r') as file:
            for line in file:
                for name in names:
                    name_count[name] += line.count(name)
        return name_count

def main():
    book = "Alice is in Wonderland.txt"
    names = ["Alice", "Bob", "Charlie"]
    sol = Solution()
    result = sol.searchingNames(book, names)
    print(result)

if __name__ == "__main__":
    main()