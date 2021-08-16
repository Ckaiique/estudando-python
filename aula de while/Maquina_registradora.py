print("Digite o codigo  produto")
n= int(input("Codigo: "))
print('Digite a quantitade: ')
n2= int(input("Quantidade: "))

if n == 1:
   preço =n2 * 0.50  
elif n == 2:
    preço = n2 * 1.00
elif n == 3 :
    preço = n2 * 4.00

print('Digite 0 para  finalizar a compra:')
n3 = int(input("Finalizar:"))
if n3 == 0 :
    print('Obrigado pela compra!')
    print(preço)
else:
    print('Codigo invalido')
