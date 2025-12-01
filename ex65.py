number = s = cont = 0
lista = []
exit_program = False

print('Digit 0 to exit the program.')
while True:
    try:
        number = int(input('Number: '))
        if number == 0:
            break
        lista.append(number)
        s += number
        cont += 1
        if cont > 0 and cont % 5 == 0:
            while True:
                option = input('Would you like to add more numbers? [Y/N]').strip().upper()
                if  option == 'Y':
                    print(f'\nPlease, add more numbers\n')
                    break
                elif option == 'N':
                    print('\nNo more numbers will be added.\n')
                    exit_program = True
                    break
                else:
                    print('Invalid input, try again.')
            if exit_program:
                break
    except ValueError:
        print('Please, add a valid number or digit 0 to exit.')

media = s / cont
maior_numero = max(lista)
menor_numero = min(lista)
print(f'Sum = {s}')
print(f'Cont = {cont}')
print(f'Media = {media:.1f}')
print(f'Maior numero = {maior_numero}')
print(f'Menor numero = {menor_numero}')
