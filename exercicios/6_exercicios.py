#Distancia que um passageiro pretende percorrer e cobrar  dele em KM

n1= float(input("Digite o KM que  você vai percorrer  ate o seu destino:")) 
km = 200
preço = 0


if (n1 <= km):
    preço = preço +(km * 0.50)
    print(f'A pertinho, sua passagem ira custar apenas {preço:6.2f}')
else:
    preço = preço +(km * 0.45)
    print(f'você vai longe em , sua passagem ira custar apenas {preço:6.2f}')