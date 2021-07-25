 #aumento de salario 

n1 = int(input("digite  o seu salario:"))
salario_base=1250
resultado = 0

if(n1>salario_base):
    resultado = resultado + ((10 * n1) / 100)
    print(f'você teve um auemnto de  R${resultado}')

if(n1 <= salario_base):
    resultado = resultado + ((15 * n1) / 100)
    print(f'você teve um auemnto de  R${resultado}')

