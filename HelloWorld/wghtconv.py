wght = input('Weight : ')
try:
    wght = float(wght)
    unit = input("Enter the unit (L)bs or (K)g : ")
    x = unit.upper()
    if x == 'L':
        wght = wght*0.45359
        print(f"Your weight in kilograms : {wght} Kgs ")
    elif x == 'K':
        wght = wght/0.45359
        print(f"Your weight in pounds :{wght} pounds ")
except:
    print('Enter a valid input data')
