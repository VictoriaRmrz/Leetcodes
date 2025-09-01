def min_conversion_cost(products, k):

    product = products[:]
    total = 0
    n = len(product)
    l = 0
    r = n - 1

    while 1 in product:
        left = product[l:l + k] if l + k <= n else product[l:]
        right = product[r - k + 1:r + 1] if r - k + 1 >= 0 else product[:r + 1]

        if sum(left) >= sum(right):
            total += sum(left)
            # Flip one 1 in the left window
            for i in range(l, min(l + k, n)):
                if product[i] == 1:
                    product[i] = 0
                    break
        else:
            total += sum(right)
            # Flip one 1 in the right window
            for i in range(r, max(r - k, -1), -1):
                if product[i] == 1:
                    product[i] = 0
                    break

    return total


def main():
    products = [1, 1, 1, 0, 1]
    k = 4
    result = min_conversion_cost(products, k)
    print(result)

if __name__ == "__main__":
    main()