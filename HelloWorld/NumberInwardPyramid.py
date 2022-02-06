n = int(input('Enter the Max number: '))

for i in range(1, n+1):
    for j in range(i-1):
        print(' ', end='')
    for j in range(i, n+1):
        print(j, end='')
    print()

for i1 in range(1, n):
    for j1 in range(1, n-i1):
        print(' ', end='')
    for j1 in range(n-i1, n+1):
        print(j1, end='')
    print()
