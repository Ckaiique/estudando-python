n1 = float(input("Digite o primeiro numero:"))
op = input("Digite o operador que você deseja usar:")
n2 = float(input("Digite o segundo numero:"))
result = 0
if op == "+":
    result = n1 + n2
elif op =="-":
    result =  n1 - n2
elif op == "*":
    result = n1 * n2 
elif op == "/":
    result == n1 / n2
else:
    print("Digite um operador  Valido igual á esses (+), (-), (*), (/)")
print (f"O resultado da Sua Operaçao é {result}")
    
    