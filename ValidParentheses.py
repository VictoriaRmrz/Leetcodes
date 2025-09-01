class Solution(object):
    def isValid(self, s):
        stack = []
        for char in s:
            if char in "({[": 
                stack.append(char)
            elif char in ")}]":
                if (char == ")" and stack[-1] != "(") or \
                  (char == "}" and stack[-1] != "{") or \
                  (char == "]" and stack[-1] != "["):
                   return False

                stack.pop()
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