class Solution:
    def triangle(self, numRows):
        result = []
        for i in range(numRows):
            row = [1] * (i + 1)
            for j in range(1, i): # first and last element is always 1
                row[j] = result[i-1][j] + result[i-1][j-1]
            result.append(row)
        return result



def main():
    sol = Solution()
    numRows = 5
    result = sol.triangle(numRows)
    print(result)

if __name__ == "__main__":
    main()