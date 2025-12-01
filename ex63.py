print('FIBONACCI')
first_value = 0
second_value = 1
n  = int(input('Fibonacci sequence number: '))
cont = 3
print(first_value, end = ' ')
print(second_value, end = ' ')
while cont <= n:
    next_value = first_value + second_value
    print(next_value, end=' ')
    first_value = second_value
    second_value = next_value
    cont = cont + 1
