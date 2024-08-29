first, second, third = input('Введите три числа: ').split()
print( first, second, third)
if first != second and third:
    print(0)
else:
    if  first == second or third:
        print(3)
    else:
        print(2)