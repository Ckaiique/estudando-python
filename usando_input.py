print('Primeiro exempolo usando input')
x = input('digite um numero:')
print(x)
print("#############################")
print('segundo exemplo')
nome =  input("Digite seu nome:")
print(f"Voce digitou {nome}")
print(f"Olá, {nome}")
print("#############################")
print('conversão da entrada de valores')
anos = int(input("Anos de serviços:"))
valor_por_ano = float(input("Valor por ano:"))
bonus = anos * valor_por_ano
print (f"Bonus de R${bonus:5.2f}")          