def piramid_sort(arr, n, ans, flag):
    if not arr:
        return ans
    if flag:
        for i in range(1, n):
            ind = i
            while arr[ind] > arr[(ind - 1) // 2] and ind != 0:
                arr[ind], arr[(ind - 1) // 2] = arr[(ind - 1) // 2], arr[ind]
                ind = (ind - 1) // 2
        flag = False
        ans.append(arr[0])
        arr[0], arr[-1] = arr[-1], arr[0]
        arr.pop()
    else:
        ind = 0
        while ind * 2 + 1 < n:  # пока у элемента есть хотя бы 1 потомок
            if ind * 2 + 2 < n:  # если у элемента есть два потомка
                if arr[ind * 2 + 1] > arr[ind * 2 + 2] and arr[ind] < arr[ind * 2 + 1]:
                    arr[ind], arr[ind * 2 + 1] = arr[ind * 2 + 1], arr[ind]
                    ind = ind * 2 + 1
                elif arr[ind * 2 + 2] > arr[ind * 2 + 1] and arr[ind] < arr[ind * 2 + 2]:
                    arr[ind], arr[ind * 2 + 2] = arr[ind * 2 + 2], arr[ind]
                    ind = ind * 2 + 2
                else:
                    break
            elif arr[ind] < arr[ind * 2 + 1]:
                arr[ind], arr[ind * 2 + 1] = arr[ind * 2 + 1], arr[ind]
                ind = ind * 2 + 1
            else:
                break
        ans.append(arr[0])
        arr[0], arr[-1] = arr[-1], arr[0]
        arr.pop()
    return piramid_sort(arr, n - 1, ans, False)


n = int(input("Введите количество элементов в массиве: "))
arr = list(map(int, input("Введите элементы массива через пробел: ").split()))

print("\nРезультат работы: ")
print(*piramid_sort(arr, n, [], True)[::-1])
