x = 1 
soma = 0

while True: 
    n =int(input(" Digite o numero:"))
    if n == 0:
        break
   
    soma = soma + n
    x = x + 1


print(f"Media : {soma / 5:5.2f}")
print(f"foram digitados {x} numeros")
