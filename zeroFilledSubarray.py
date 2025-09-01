class Solution(object):
    def zeroFilledSubarray(self, nums):
        sum = 0
        count = 0
        for n in nums:
            if n == 0:
                sum += 1
                count += sum
            else:
                sum = 0
        return count

def main():
    sol = Solution()
    nums = [0,0,0,2,0,0]
    result = sol.zeroFilledSubarray(nums)
    print(result)

if __name__ == "__main__":
    main()