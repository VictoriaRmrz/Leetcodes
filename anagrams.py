class Solution(object):
    def is_anagram(self, s1, s2):
        # Usa sort() si quieres modificar la lista original.
        # Usa sorted() si necesitas una nueva lista ordenada sin alterar el objeto original.
        return sorted(s1) == sorted(s2)

def main():
    s = "anagram"
    t = "nagaram"
    sol = Solution()
    print(sol.is_anagram(s, t))

if __name__ == "__main__":
    main()

