n1 = int(input("n1  numero : "))
n2 = int(input("n2 o segundo numero :"))
n3 = int(input("n3 o terceiro :"))

if (n1 > n2 > n3):
    print(f"n1  maior {n1} ")

if(n2 > n1 > n3):
    print(f"n2  maior {n2} ")
if(n3 > n2 > n1):
    print (f"n3  maior  {n3}")

if (n1< n2 < n3):
    print(f"o valor do n1 menor {n1}")

if(n2 < n1 < n3):
    print(f"o valor do n2 menor {n2}")

if ( n3 < n2 < n1):
    print( f"o valor do n3 menor {n3}")