def variacion_con_repeticion(n, k):
    return n ** k

n = int(input("Ingresa el número total de elementos (n): "))
k = int(input("Ingresa la cantidad de elementos a elegir (k): "))

if n < 0 or k < 0:
    print("Error: n y k deben ser números no negativos.")
else:
    v = variacion_con_repeticion(n, k)
    print("V(", n, ",", k, ") =", v)