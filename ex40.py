# Crie um programa que leia duas notas de um aluno e calcule sua media
# Mostrando uma mensagem no final de acordo com a media atingida:
# media abaixo de 5,0: REPROVADO
# media entre 5,0 e 6,9: RECUPERAÇÃO
# media 7,0 ou superior: APROVADO
nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))
media = (nota1 + nota2) / 2
if media < 5:
    print('REPROVADO')
elif media >= 5 and media < 7:
    print('RECUPERACAO')
else:
    print('APROVADO')