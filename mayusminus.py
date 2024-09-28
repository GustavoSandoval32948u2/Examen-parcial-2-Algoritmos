def mayus_minus():
    total = 0
    valor = input("Ingrese un texto en mayusculas o minusculas > ")
    for i in valor:
        if i == "A":
            total =+ 1
        elif i == "a":
            total=+1
    return total

print(mayus_minus())
            
            
