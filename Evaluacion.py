numeros = []
contador = 10
suma=0

while len(numeros) < 10:
    numero = int(input("Ingrese un número: "))
    suma += numero
    numeros.append(numero)
    contador -= 1
    print(f"Números restantes: {contador}")

promedio=suma / len(numeros)

print(suma)
print(len(numeros))
print(promedio)
