n = int(input('Enter the number of Rows: '))
q = n//2 + 1

for i in range(1, q+1):
    for j in range(1, q-i+1):
        print(" ", end='')
    for j in range(q-i+1, (n-(q-i))+1):
        print('*', end='')
    print()

for i in range(1, q):
    for j in range(1, i+1):
        print(' ', end='')
    for j in range(i+1, n-i+1):
        print('*', end='')
    print()

