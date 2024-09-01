first = int(input("Введите первое число: "))
second = int(input("Введите второе число: "))
third = int(input("Введите третье число: "))
print( first, second, third)
if first == second and first == third and third == second:
    print(3)
elif first == second or second == third or third == first:
    print(2)
else:
    print(0)