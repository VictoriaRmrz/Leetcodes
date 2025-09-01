class RemoveValues:
    def removeTarget(self, nums, val):
        for i in range(len(nums)):
            if nums[i] == val:
                nums[i] = float('inf') # inf, 2, 2, inf
        nums.sort() # 2, 2, inf, inf 

        for i in range(len(nums)):
            if nums[i] == float('inf'):
                nums[i] = "_"
        
        return nums

def main():
    remover = RemoveValues()
    nums = [3, 2, 2, 3]
    val = 3
    new_length = remover.removeTarget(nums, val)
    print(new_length)

if __name__ == "__main__":
    main()