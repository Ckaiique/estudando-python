#Aprovaçao de  emprestimo.
valor_casa = float(input('Digite  o valor da casa:'))
salario=  float(input('Digite  o seu salario:'))
anos_pagar= float(input('Digite a quantidade de anos que você deseja pagar :'))

meses_pagar= anos_pagar * 12
calculo_prestaçao =  ((30 * salario)/100)

if (calculo_prestaçao <= salario ):
    resultado = calculo_prestaçao + valor_casa / meses_pagar
    print('O emprestimo foi aprovado !')
else:
    print('Infelismente não pode ser  aprovado !')



