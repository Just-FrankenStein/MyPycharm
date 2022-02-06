n = int(input('Enter the factorial number: '))
def factorial(n):
    result = 1
    for x in range(1, n+1):
        if n != 0:
            result = result * x
        else:
            result = 1
    return result

for n in range(n+1):
    print(n, factorial(n))