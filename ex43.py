# Desenvolva uma logica que leia o peso e a altura de uma pessoa,
# calcule seu IMC  e mostre seu status, de acordo com a tabela abaixo:
# - Abaixo de 18.5: Abaixo do Peso
# - Entre 18.5 e 25: Peso ideal
# - 25 ate 30: Sobrepeso
# - 30 ate 40: Obesidade
# - acima de 40: Obesidade morbida

altura = float(input('Altura em metros: '))
peso = float(input('Peso em Kgs: '))
imc = peso / (altura ** 2)
print(f'Seu IMC: {imc:.1f}')
if imc < 18.5:
    print('Abaixo do Peso')
elif 18.5 <= imc < 25:
    print ('Peso ideal')
elif 25 <= imc < 30:
    print ('Sobrepeso')
elif 30 <= imc < 40:
    print ('Obesidade')
elif imc >= 40:
    print('Obesidade morbida')