from datetime import date

cont_menor = 0
cont_maior = 0
ano_atual = date.today().year

for i in range (7):
    ano_nascimento = int(input('Digite o ano de nascimento: '))
    idade = ano_atual - ano_nascimento
    if 0 <= idade < 21:
        cont_menor += 1
    else:
        cont_maior += 1
print(f'Maiores de idade: {cont_maior}')
print(f'Menores de idade: {cont_menor}')
