

#este codigo crea un grafo dirigido con 4 variables
#creamos un grafo vacio

grafo={}

#agregamos vertices al grafo

grafo["A"] = ["B","C"]
grafo["B"] = ["D"]
grafo["C"] = ["D"]
grafo["D"] = []

# imprimimos el grafo
print("grafo:")

for vertice, adyacentes in grafo.items():
    print(F"{vertice} -> {adyacentes}")
