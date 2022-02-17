n = int(input('Enter the number of lines required: '))
q = n // 2 + 1

for i in range(1, q + 1):
    for j in range(1, i):
        print(' ', end='')
    for j in range(1, i + 1):
        print('*', end=' ')
    print()

for i in range(1, q):
    for j in range(1, q - i):
        print(" ", end='')
    for j in range(1, q - i + 1):
        print('*', end=' ')
    print()