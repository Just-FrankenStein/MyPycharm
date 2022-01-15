x = input("Enter the number of Elements required: ")

def list1_size(n):
    try:
        n = int(n)
        list1 = []
        for i in range(n):
            element = int(input('Enter the element : '))
            list1.append(element)
        print(f'The input list is : {list1}')
        return list1
    except:
        print('Please use a number as a parameter of the list1_size() function!')

list2 = list1_size(x)
maxi = list2[0]
for number in list2:
    if number > maxi:
        maxi = number
print(f'The largest number in the given set of number is {maxi}')