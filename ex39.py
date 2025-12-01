# Faça um programa que leia o ano de nascimento de um jovem e informe de acordo com sua idade:
# Se ele ainda vai se alistar ao serviço militar
# Se é a hora de se alistar
# Se ja passou do tempo do alistamento
# Seu programa tambem devera mostrar o tempo que falta ou que passou do prazo
from datetime import date

ano_atual = date.today().year
ano_nasc = int(input('Qual seu ano de nascimento: '))
idade = ano_atual - ano_nasc
if idade < 18:
    print(f'Ainda não é hora de se alistar. Ainda faltam {18 - idade} ano(s).')
    print(f'Seu alistamento será em {ano_atual + (18 - idade)}')
elif ano_nasc == 18:
    print('É hora de se alistar.')
else:
    print(f'O seu tempo de alistamento ja passou tem {idade - 18} ano(s).')
    print(f'O seu alistamento foi em {ano_atual - (idade - 18)}')