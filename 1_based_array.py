mod = 10**9 + 7
def powerArray(arr):
    n = len(arr)
    max_value = 0
    min_index = -1

    for i in range(n - 1):
        result = pow(arr[i], arr[i + 1], mod)
        if result > max_value:
            max_value = result
            min_index = i
    return (max_value, min_index)

def main():
    arr = [3,1,2,3]
    result = powerArray(arr)
    print("Maximum Value:", result[0])
    print("Minimum Index:", result[1])

if __name__ == "__main__":
    main()