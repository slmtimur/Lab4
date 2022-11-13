def quick_sort(arr, n):
    opor = n - 1
    i = 0
    while i < opor:
        if arr[i] >= arr[opor]:
            if i == opor - 1:
                arr[opor], arr[opor - 1] = arr[opor - 1], arr[opor]
            else:
                arr[opor], arr[opor - 1] = arr[opor - 1], arr[opor]
                arr[opor], arr[i] = arr[i], arr[opor]
            opor -= 1
            continue
        i += 1
        if i == opor:
            break
    if n <= 1:
        return arr
    else:
        return quick_sort(arr[:opor], opor) + [arr[opor]] + quick_sort(arr[opor + 1:], n - opor - 1)

def comb_sort(arr, n):
    amount = n - 1
    while amount != 0:
        l = 0
        r = l + amount
        while r != n:
            if arr[l] > arr[r]:
                arr[l], arr[r] = arr[r], arr[l]
            l, r = l + 1, r + 1
        amount -= 1
    return arr