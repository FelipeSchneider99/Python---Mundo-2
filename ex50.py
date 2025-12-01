soma = 0
cont = 0
for i in range(1, 7):
    num = int(input('digite um numero: '))
    if num % 2 == 0:
        soma += num
        cont += 1
print(f'Voce informou {cont} numeros pares e a soma dos valores é {soma}')