def swapAlternate(arr, n):
    l = arr[:]
    l.append(l[n - 1])

    for i in range(n):
        if i % 2 == 0:
            arr[i] = l[i + 1]
        elif i % 2 == 1:
            arr[i] = l[i - 1]
    return arr