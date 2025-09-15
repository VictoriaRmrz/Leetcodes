class Solution(object):
    def isValid(self, s):
        stack = []
        mapping = {
                    ")": "(", 
                    "}": "{", 
                    "]": "["
                }
        for char in s:
            if stack.pop() != mapping[char]:
                return False
            else:
                stack.append(char)
        return not stack

def main():
    solution = Solution()
    test_cases = [
        "{[}]"
    ]
    for s in test_cases:
        print(f"Input: {s} -> Output: {solution.isValid(s)}")   

if __name__ == "__main__":
    main()