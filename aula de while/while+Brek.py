s = 0
while True:
    v  = int(input("Digite um numero a somar ou 0 para sair:"))
    if v == 0:
        print("Fim ")
        break
    s += v
    print(s)