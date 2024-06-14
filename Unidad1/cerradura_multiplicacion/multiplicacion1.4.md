
numero1=float(input("ingresa el primer numero "))
numero2=float(input("ingresa tu segundo numero "))
multi=numero1*numero2

if multi.is_integer():
    resultado="entero"
else:
    resultado="racional"

#muesta el resultado de la multiplicacion y su tipo

print() #linea en blanco para separar el resultada
print("la suma es",multi) #mostrar suma
print()
print("el resultado de la suma es", resultado)