# A Confederação Nacional de Natação precisa de um programa que leia:
# o ano de nascimento de um atleta e mostre sua categoria de acordo com a idade:
# até 9 anos MIRIM
# ate 14 anos INFANTIL
# ate 19 anos JUNIOR
# ate 25 anos SENIOR
# acima MASTER
from datetime import date

ano = int(input('Digite o ano de seu nascimento: '))
ano_atual = date.today().year

if ano_atual - ano <= 9:
    print('Categoria MIRIM')
elif ano_atual - ano <= 14:
    print('Categoria INFANTIL')
elif ano_atual - ano <= 19:
    print('Categoria JUNIOR')
elif ano_atual - ano == 25:
    print('Categoria SENIOR')
else:
    print('Categoria MASTER')