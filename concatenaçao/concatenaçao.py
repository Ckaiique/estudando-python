x = "####"
res = x * 10


print ('priemro jeito posso concatetenar entradas  assim')
print (res) 
nome ='tiao'
idade = 10
grana = 51.34

print ('%-5s  %d'%(nome, idade)) 
print (res)


print('segundo jeito ou assim') 
print (res)
print ("{} tem {} anos  R${} no bolso".format(nome,idade, grana))
print ("{:12} tem {:03} anos  R${:5.2f} no bolso".format(nome,idade, grana))
print ("{:12} tem {:03} anos  R${:5.2f} no bolso".format(nome,idade, grana))
print ("{:<12} tem {:<3} anos  R${:5.2f} no bolso".format(nome,idade, grana))
print (res)


print ('terceiro  jeito')
print (res)
print(f'{nome} tem {idade} anos e R${grana} no bolso.')
print(f'{nome:12} tem {idade:3} anos e R${grana:5.2f} no bolso.')
print(f'{nome:12} tem {idade:03} anos e R${grana:5.2f} no bolso.')
print(f'{nome:<12s} tem {idade:<3} anos e R${grana:5.2f} no bolso.')
