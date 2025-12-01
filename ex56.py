soma_idade = 0
media_idade = 0
contador_mulher = 0
mais_velho = 0
nome_velho = ''
for i in range(1, 5):
    print(f'----- {i}ª PESSOA ------')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo (M/F): ')).strip()
    soma_idade += idade
    if i == 1 and sexo in 'Mm':
        mais_velho = idade
        nome_velho = nome
    if sexo in 'Mm' and idade > mais_velho:
        mais_velho = idade
        nome_velho = nome
    if sexo in 'Ff' and idade < 20:
        contador_mulher += 1


media_idade = soma_idade / 4
print (f'A média de idade do grupo é de {media_idade:.1f}')
print(f'Tem um total de {contador_mulher} mulheres com menos de 20 anos.')
print(f'O homem mais velho é {nome_velho} com {mais_velho} anos.')
