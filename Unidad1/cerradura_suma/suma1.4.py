print("cerradura: la suma de dos numeros reales siempre da como resultado otro numero real.")
print()
print("a + b pertenece r")
print()#imprime el mendaje que indica que el programa demostrara la propiedad de la cerradura
print("el siguiente programa realiza la propiedad de cerradura")
print() #linea en blanco para separar la introduccion de la siguiente seccion
#solicita al usuario que ingrese el primer numero
numero1=float(input("ingresa el primer numero "))
#solicita al usuario el segundo numero
numero2=float(input("ingresa tu segundo numero "))
suma=numero1+numero2

if suma.is_integer():
    resultado="entero"
else:
    resultado="racional"

#muesta el resultado de la suma y su tipo

print() #linea en blanco para separar el resultada
print("la suma es",suma) #mostrar suma
print("el resultado de la suma es", resultado)