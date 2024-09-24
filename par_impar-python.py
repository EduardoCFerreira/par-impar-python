numero_max = input('Digite um número máximo: ')

if numero_max.isdigit():
    numero_max_int = int(numero_max)
else:
    print("Você não digitou um número")
    
numero = input('Digite um número: ')

if numero.isdigit():
    numero_int = int(numero)
else:
    print("Você não digitou um número")

while numero_int <= numero_max_int:
    if numero_int % 2 == 0:
        print(numero_int)
        numero_int += 2
        continue
    while numero_int <= numero_max_int:
        if numero_int % 3 == 0:
            print(numero_int)
            numero_int += 3
print("Acabou")