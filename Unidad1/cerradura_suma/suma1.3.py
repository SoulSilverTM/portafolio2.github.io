#solicita al usuario que ingrese el primer numero
numero1=float(input("ingresa el primer numero "))
#solicita al usuario el segundo numero
numero2=float(input("ingresa tu segundo numero "))

if numero1 > numero2:
    print("el primero numero es mayor")
elif numero1< numero2:
    print("el segundo numero es mas grande")
else:
    print("ambos numeros son iguales")