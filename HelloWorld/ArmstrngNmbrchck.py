def checkArmstrng(num):
    l = len(str(num))

    Arm_sum = 0
    temp = num

    while num > 0:
        x = num % 10
        Arm_sum = Arm_sum + x ** l
        num = num // 10

    if temp == Arm_sum:
        return True
    else:
        return False


n = int(input())

if checkArmstrng(n):
    print('true')
else:
    print('false')