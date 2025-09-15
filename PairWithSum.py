class Solution(object):
    def has_pair_with_sum(self, numbers, target):
        hash = {}
        for i in range(len(numbers)):
            aux = target - numbers[i]
            if aux in hash:
                return True
            hash[numbers[i]] = i
        return False
    
    def another(self, numbers, target):
        for i in range(len(numbers)):
            aux = target - numbers[i]
            if aux in numbers[i+1:]:
                return True
        return False

def main():
    nums = [2, 7, 11, 15]
    target = 9
    sol = Solution()
    result = sol.another(nums, target)
    print(result)

if __name__ == "__main__":
    main()  