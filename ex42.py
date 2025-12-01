# Refaça o ex 35 dos triangulos, acrescentando o recurso de mostrar que tipo de triangulo sera formado:
# equilatero: todos os lados iguais
# isosceles: dois lados iguais
# escaleno: todos os lados diferentes
print('TRIANGULO')
a = (float(input('Valor A: ')))
b = (float(input('Valor B: ')))
c = (float(input('Valor C: ')))

if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print('TRIANGULO EQUILATERO')
    elif a == b or a == c or b == c:
        print('TRIANGULO ISOSCELES')
    elif a != b and a != c and b != c:
        print('TRIANGULO ESCALENO')
else:
    print('Não forma um triangulo')