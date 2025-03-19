import numpy as np

def obtener_datos():
    n = int(input("Ingrese la cantidad de elementos: "))
    datos = []
    for i in range(n):
        valor = float(input(f"Ingrese el valor {i+1}: "))
        datos.append(valor)
    return np.array(datos)

def calcular_tabla_frecuencia(datos, num_clases):
    min_val = datos.min()
    max_val = datos.max()
    rango = max_val - min_val
    ancho_clase = rango / num_clases
   
    intervalos = []
    frecuencia_absoluta = []
   
    for i in range(num_clases):
        lim_inf = min_val + i * ancho_clase
        lim_sup = lim_inf + ancho_clase
        intervalos.append((lim_inf, lim_sup))
        frecuencia_absoluta.append(((datos >= lim_inf) & (datos < lim_sup)).sum())

    frecuencia_absoluta[-1] += (datos == max_val).sum()

    total_datos = len(datos)
    frecuencia_relativa = [f / total_datos for f in frecuencia_absoluta]

    frecuencia_acumulada = np.cumsum(frecuencia_absoluta).tolist()

    return frecuencia_absoluta, frecuencia_relativa, frecuencia_acumulada

def imprimir_tabla(frecuencia_absoluta, frecuencia_relativa, frecuencia_acumulada):
    print("\nTabla de Frecuencia")
    print("-" * 40)
    print(f"{'Frec. Absoluta':<15} {'Frec. Relativa':<15} {'Frec. Acumulada':<15}")
    print("-" * 40)
   
    for i in range(len(frecuencia_absoluta)):
        print(f"{frecuencia_absoluta[i]:<15} {frecuencia_relativa[i]:<15.4f} {frecuencia_acumulada[i]:<15}")

def main():
    datos = obtener_datos()
    num_clases = int(input("Ingrese el número de clases: "))
    frecuencia_absoluta, frecuencia_relativa, frecuencia_acumulada = calcular_tabla_frecuencia(datos, num_clases)
    imprimir_tabla(frecuencia_absoluta, frecuencia_relativa, frecuencia_acumulada)

if __name__ == "__main__":
    main()