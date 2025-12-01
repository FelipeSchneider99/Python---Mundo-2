print('FATORIAL FOR')
n = int(input('Digite um numero: '))
fatorial = 1

if n == 0:
    print('O fatorial de 0 é igual a 1')
elif n < 0:
    print('Não existe fatorial de número negativo')
else:
    for i in range(n, 0, -1):
        fatorial *= i
    print(f'O fatorial de {n} é igual a {fatorial}')