import math
def calcular_lado_faltante():
    print("Introduce los valores de dos lados de un triangulo")
    print("Deja en blanco el valor del lado que deseas ")

    a=input("Lado a (cateto):")
    b=input("Lado b (cateto):")
    c=input("Lado c (hipotenusa):")

    # convertir las entradas a numeros, si 
    a=float(a) if a else None 
    b=float(b) if b else None 
    c=float(c) if c else None 

    #calcula el lado faltante usando el teorema
    if a is None and b is not None and c is not None
    a=math.sqrt(c**2-b**2)
    lado_calculado="a(cateto)"
    elif b is None and a is not None and c is not None
    b=math.sqrt(c**2-a**2)
    elif c is None and a is not None and b is not None
    c=math.sqrt(a**2+b**2)
    lado_calculado="c(hipotenusa)"
else:
return "Error:Debe proporcionar exactamente dos lados."
return f "El lado faltante es{lado_calculado} y su valor es: 
{a if lado_calculado=='a(cateto)' else b if lado_calculado=='b(cateto)'else c:.2f}"

resultado = calcular_lado_faltante()
printf(resultado)



