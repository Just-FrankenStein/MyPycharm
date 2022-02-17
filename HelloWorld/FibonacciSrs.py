def fib_list(n):
    fib_sum = 0
    temp = [0]

    for x in range(1, n + 1):
        if x == 1:
            fib_sum = fib_sum + 1
            temp.append(fib_sum)
        else:
            fib_sum = fib_sum + temp[x - 2]
            temp.append(fib_sum)

    return temp
