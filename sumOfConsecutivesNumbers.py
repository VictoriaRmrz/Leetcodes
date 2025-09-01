class Solution(object):
    def sumOfConsecutives(self, target):
        ways = 0
        for i in range(1, target + 1):
            j = i
            while sum(range(i, j + 1)) <= target: 
                if sum(range(i, j + 1)) == target and (i != j):
                    ways += 1
                j += 1
        return ways

    def sumOfConsecutivesEfficient(self, target):
        combinations = []
        ways = 0
        i = 1
        while i < target:
            sum = i
            j = i + 1

            while sum < target: 
                sum += j 
                if sum == target:
                    #combinations.append(list(range(i, j + 1)))
                    ways += 1
                j += 1
            i += 1

        return ways

def main():
    sol = Solution()
    target = 15 
    result = sol.sumOfConsecutivesEfficient(target)
    print(result)

if __name__ == "__main__":
    main()