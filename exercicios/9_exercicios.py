#calcular o preço a pagar pelo consumo de energia eletrica.
quantidade =  float(input('Digite a quantidade de kWh Consumida: '))
print("Digite sua categoria: (r = Residências), (i = indústrias) e (c = Comércios):")
categoria = input()
preço =0
if (categoria ==  "r" and quantidade <= 500):
    preço = quantidade * 0.40
elif (categoria ==  "r" and quantidade > 500):
    preço = quantidade * 0.65
elif(categoria == "c" and quantidade <= 1000):
    preço = quantidade * 0.55
elif(categoria == "c" and quantidade > 1000):
    preço = quantidade * 0,60
elif (categoria == "i" and quantidade <=5000):
    preço = quantidade * 0.55
elif (categoria =="i" and quantidade > 5000):
    preço = quantidade * 0.60
else:
    print("Opção invalida digite as primeiras letras em minusculas ex: (r),(i),(c)")
    
print(f"O valor que voce deve pagar  é R${preço:6.2f}")
