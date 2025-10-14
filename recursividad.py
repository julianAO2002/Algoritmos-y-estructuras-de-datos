#3 Implementar una función para calcular el producto de dos números enteros dados.

#Prod(n,m) = n + prod(n, m - 1)

def prod(n, m):
    if m ==0:
        return 0
    elif m > 0:
        return n + prod(n, m - 1)
    
# resultado = prod(8,8) 
# print(resultado)

#4 Implementar una función para calcular la potencia dado dos números enteros, el primero re-
#presenta la base y segundo el exponente.

# pot(n, m) = n * pot(n, m-1)
def prod(n, m):
    if m ==0:
        return 1
    elif m > 0:
        return n * prod(n, m - 1)
    
# resultado = prod(8,4) 
# print(resultado)


#5 Desarrollar una función que permita convertir un número romano en un número decimal.
def romano_a_decimal(romano):
    valores = {
        'I': 1, 'V': 5, 'X': 10,
        'L': 50, 'C': 100,
        'D': 500, 'M': 1000
    }

    def convertir(s):
        if not s:
            return 0
        if len(s) == 1:
            return valores[s]
        if valores[s[0]] < valores[s[1]]:
            return valores[s[1]] - valores[s[0]] + convertir(s[2:])
        else:
            return valores[s[0]] + convertir(s[1:])

    return convertir(romano)

#print(romano_a_decimal("XII"))


#6  Dada una secuencia de caracteres, obtener dicha secuencia invertida.

def invertir_secuencia(secuencia):
    if len(secuencia) <= 1:
        return secuencia
    return secuencia[-1] + invertir_secuencia(secuencia[:-1])


# texto = "Hola mundo"
# invertido = invertir_secuencia(texto)
# print(invertido)  

#7 desarrollar un algoritmo que permita calcular la siguiente serie:
#h(n)=1/n

def serie(n):
    if n == 1:
        return 1
    return 1/n + serie(n-1)

# resut = serie(10)
# print(resut)


#8 Desarrollar un algoritmo que permita convertir un número entero en sistema decimal a siste-
# ma binario.
def decimal_a_binario(n: int) -> str:
    if n == 0:
        return "0"
    if n == 1:
        return "1"
    return decimal_a_binario(n // 2) + str(n % 2)

#print(decimal_a_binario(54))

#9. Implementar una función para calcular el logaritmo entero de número n en una base b. Re-
#cuerde que: 
#MAL

def logaritmo_entero(n:int, b:int) ->int:
    if n < b:
        return 0
    return 1 + logaritmo_entero(n // b, b)

#print(logaritmo_entero(12,3))


#10. Desarrollar un algoritmo que cuente la cantidad de dígitos de un número entero.
def contar_digitos(n: int) -> int:
    if n < 10:
        return 1
    return 1 + contar_digitos(n // 10)

#print(contar_digitos(22131))

#11. Desarrollar un algoritmo que invierta un número entero sin convertirlo a cadena.
def invertir_numero(n, invertido=0):
    if n == 0:
        return invertido
    else:
        return invertir_numero(n // 10, invertido * 10 + n % 10)

#print(invertir_numero(12345))

#12. Desarrollar el algoritmo de Euclides para calcular el máximo común divisor (MCD) de dos
#número entero.

def mcd(a, b):
    if b == 0:
        return a
    else:
        return mcd(b, a % b)

#print(mcd(48, 18))

#13. Desarrollar el algoritmo de Euclides para calcular también el mínimo común múltiplo (MCM)
#de dos número entero.

def mcm(a, b):
    if a == 0 or b == 0:
        return 0  
    else:
        return abs(a * b) // mcd(a, b)
    
#print(mcm(12,6))    

def suma_digitos(n):
    n = abs(n)  
    if n == 0:
        return 0
    else:
        return (n % 10) + suma_digitos(n // 10)
    
#print(suma_digitos(123))    

def raiz_cuadrada_entera(n):
    def auxiliar(x, candidato=0):
        if candidato * candidato > x:
            return candidato - 1
        else:
            return auxiliar(x, candidato + 1)
    
    if n < 0:
        raise ValueError("El número no puede ser negativo.")
    return auxiliar(n)

#print(raiz_cuadrada_entera(26))

# 16. Implementar un función recursiva que permita obtener el valor de an en una sucesión geomé-
# trica (o progresión geométrica) con un valor a1= 2 y una razón r = -3. Además desarrollar un
# algoritmo que permita visualizar todos los valores de dicha sucesión desde a1 hasta an.

def sucesion_geometrica(n):
    if n == 1:
        return 2  
    else:
        return (-3) * sucesion_geometrica(n - 1)

def mostrar_sucesion(n, actual=1):
    if actual > n:
        return
    else:
        print(f"a{actual} =", sucesion_geometrica(actual))
        mostrar_sucesion(n, actual + 1)

#mostrar_sucesion(5)

#17. Escribir una función recursiva que permita mostrar los valores de un vector de atrás hacia adelante.

def mostrar_reversa(vector, indice=None):
    if indice is None:
        indice = len(vector) - 1  # Comenzamos desde el último índice
    if indice < 0:
        return
    else:
        print(vector[indice])
        mostrar_reversa(vector, indice - 1)

# mi_vector = [10, 20, 30, 40, 50]
# mostrar_reversa(mi_vector)

# 18. Implementar una función recursiva que permita recorrer una matriz y mostrar sus valores.      

def recorrer_matriz(matriz, fila=0, columna=0):
    if fila >= len(matriz):
        return
    if columna >= len(matriz[fila]):
        print()  
        recorrer_matriz(matriz, fila + 1, 0)  
    else:
        print(matriz[fila][columna], end=" ")
        recorrer_matriz(matriz, fila, columna + 1)  

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
    ]

# recorrer_matriz(matriz)

# 19. Dada la siguiente definición de sucesión recursiva, realizar una función recursiva que permita
# calcular el valor de un determinado número en dicha sucesión.

def sucesion(n):
    if n == 1:
        return 2
    else:
        return n + 1 / sucesion(n - 1)
    
# print(sucesion(12))

# 20. Desarrollar un algoritmo que permita implementar la búsqueda secuencial con centinela de
# manera recursiva, y permita determinar si un valor dado está o no en dicha lista.

def busqueda_secuencial_con_centinela(lista, valor, indice=0):
    if indice == 0:
        lista.append(valor)
    if lista[indice] == valor:
        if indice == len(lista) - 1:
            lista.pop()
        return indice != len(lista) - 1
    return busqueda_secuencial_con_centinela(lista, valor, indice + 1)

lista = [3, 5, 7, 2, 8, 1]

# encontrado = busqueda_secuencial_con_centinela(lista, 7)
# print(f"¿Valor encontrado? {encontrado}")

# 21. Dada una lista de valores ordenadas, desarrollar un algoritmo que modifique el método de
# búsqueda binaria para que funcione de forma recursiva, y permita determinar si un valor dado
# está o no en dicha lista.

def busqueda_binaria(lista, valor, bajo=0, alto=None):
    if alto is None:
        alto = len(lista) - 1

    if bajo > alto:
        return False

    medio = (bajo + alto) // 2
    if lista[medio] == valor:
        return True
    elif lista[medio] > valor:
        return busqueda_binaria(lista, valor, bajo, medio - 1)
    else:
        return busqueda_binaria(lista, valor, medio + 1, alto)
    
lista = [1, 3, 5, 7, 8, 10, 12]
valor_buscado = 9

# encontrado = busqueda_binaria(lista, valor_buscado)
# print(f"¿Valor encontrado? {encontrado}")


# 22. El problema de la mochila Jedi. Suponga que un Jedi (Luke Skywalker, Obi-Wan Kenobi, Rey u
# otro, el que más le guste) está atrapado, pero muy cerca está su mochila que contiene muchos
# objetos. Implementar una función recursiva llamada “usar la fuerza” que le permita al Jedi “con
# ayuda de la fuerza” realizar las siguientes actividades:
# a. sacar los objetos de la mochila de a uno a la vez hasta encontrar un sable de luz o que no
# queden más objetos en la mochila;

# b. determinar si la mochila contiene un sable de luz y cuantos objetos fueron necesarios sa-
# car para encontrarlo;

# c. Utilizar un vector para representar la mochila.

def usar_la_fuerza(mochila, indice=0, contador=0):
    if indice >= len(mochila):
        return False, contador  

    if mochila[indice] == "sable de luz":
        return True, contador + 1  

    
    return usar_la_fuerza(mochila, indice + 1, contador + 1)

mochila = ["pocion", "comida", "sable de luz", "blaster", "comunicador"]

encontrado, objetos_sacados = usar_la_fuerza(mochila)

if encontrado:
    print(f"Se encontró el sable de luz después de sacar {objetos_sacados} objetos.")
else:
    print("No se encontró el sable de luz en la mochila.")

