class Solution(object):
    def letterCombinations(self, digits):
        phone = {
            2: ['a', 'b', 'c'],
            3: ['d', 'e', 'f'],
            4: ['g', 'h', 'i'],
            5: ['j', 'k', 'l'],
            6: ['m', 'n', 'o'],
            7: ['p', 'q', 'r', 's'],
            8: ['t', 'u', 'v'],
            9: ['w', 'x', 'y', 'z']
        }
        result = []
        def backtracking(digits, combination):
            if not digits:
                result.append(combination)
                return
            digit = int(digits[0]) # take the first digit
            for letter in phone[digit]:
                # combine first letter of first digit with letters of the other numbers
                backtracking(digits[1:], combination + letter) 

        backtracking(digits, "")
        return result

    def anotherWay(self, digits):
        phone = {
            2: ['a', 'b', 'c'],
            3: ['d', 'e', 'f'],
            4: ['g', 'h', 'i'],
            5: ['j', 'k', 'l'],
            6: ['m', 'n', 'o'],
            7: ['p', 'q', 'r', 's'],
            8: ['t', 'u', 'v'],
            9: ['w', 'x', 'y', 'z']
        }
        if not digits:
            return [""]
        result = []
        def backtracking(i, combination):
            if i == len(digits):
                result.append(combination)
                return
            digit = int(digits[i])
            for letter in phone[digit]:
                backtracking(i + 1, combination + letter)
        backtracking(0, "")
        return result

                    
def main():
    sol = Solution()
    digits = "23"
    print(sol.anotherWay(digits))

if __name__ == "__main__":
    main()