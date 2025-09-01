class Solution:
    def minFlips(self, initial, target):
        flips = 0
        for i in range(len(initial)):
            if initial[i] != target[i]:
                flips += 1
        return flips

def main():
    sol = Solution()
    initial = "00000"
    target = "01011"
    result = sol.minFlips(initial, target)
    print(result)