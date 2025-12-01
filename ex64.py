number = cont = s = 0

print('If you want the program to stop, digit 999')
while number != 999:
    number = int(input('Digit a number: '))
    if number == 999:
        break
    else:
        cont += 1
        s += number
print(f'Sum = {s}')
print(f'Cont = {cont}')
