#solicitar un numero
numero1=float(input("ingresa el primer numero "))
#solicita al usuario el segundo numero
numero2=float(input("ingresa tu segundo numero "))

#operaciones
multo=numero1*numero2
suma=numero1+numero2
resta=numero1-numero2
division=numero1//numero2


#muesta el resultado de la multiplicacion y su tipo
if multo.is_integer():
    resultado1="entero"
else:
    resultado1="racional"
print() #linea en blanco para separar el resultada
print("el resultado de la multiplicacion es ",multo) 
print("tu resultado es ",resultado1)

if suma.is_integer():
    resultado2="entero"
else:
    resultado2="racional"
print()
print("el resultado de la suma es ",suma)
print("tu resultado es ",resultado2)
if resta.is_integer():
    resultado3="entero"
else:
    resultado3="racional"

print()
print("el resultado de la resta es ",resta)
print("tu resultado es ",resultado3)
print()
10
if division.is_integer():
    resultado4="entero"
else:
    resultado4="racional"
print("el resultado de la division es",division)
print("tu resultado es ",resultado4)