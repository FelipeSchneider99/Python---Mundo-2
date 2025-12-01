# num = int(input('Digite um numero: '))
# cont = 0
# for i in range(1, num + 1):
#     if num % i == 0:
#         cont += 1
# if cont == 2:
#     print(f'{num} é primo')
# else:
#     print(f'{num} não é primo')

num = int(input('Digite um numero: '))
total = 0
for i in range(1, num + 1):
    if num % i == 0:
        print(f'\033[34m', end = ' ')
        total += 1
    else:
        print(f'\033[31m', end = ' ')
    print(f'{i}', end=' ')
print (f'\n\033[mO numero {num} foi dividido {total} vezes')
if total == 2:
    print('E por isso ele é PRIMO!')
else:
    print('E por isso ele NÃO é PRIMO!')
