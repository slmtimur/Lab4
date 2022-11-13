def block_sort(arr, n):
    min_n, max_n = min(arr), max(arr)
    if n == 1 or min_n == max_n:
        return arr
    max_n = (min_n + max_n) // 2
    sort_arr = [[], []]
    
    count0 = 0
    count1 = 0
    for i in range(n):
        if arr[i] <= max_n:
            sort_arr[0].append(arr[i])
            count0 += 1
        else:
            sort_arr[1].append(arr[i])
            count1 += 1
    return block_sort(sort_arr[0], count0) + block_sort(sort_arr[1], count1)


n = int(input("Введите количество элементов в массиве: "))
arr = list(map(int, input("Введите элементы массива через пробел: ").split()))

print("\nРезультат работы:")
print(*block_sort(arr, n))
