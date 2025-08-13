#Ejercicio Numero 1
print("·Ejercicio Número 1")
# Solicitar dos números al usuario
num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))

# Realizar operaciones
suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2 if num2 != 0 else "No se puede dividir por cero"

# Imprimir resultados
print(f"\nResultados:")
print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicación: {multiplicacion}")
print(f"División: {division}")



#Ejercicio Numero 2
print(" ")
print(" ")
print("·Ejercicio Número 2")
# Crear lista vacía
lista_compras = []

# Añadir tres artículos
lista_compras.append("Leche")
lista_compras.append("Pan")
lista_compras.append("Huevos")

# Imprimir lista final y total de artículos
print("\nLista de Compras:")
for articulo in lista_compras:
    print("-", articulo)

print(f"\nTotal de artículos: {len(lista_compras)}")



#Ejercicio Numero 3
print(" ")
print(" ")
print("·Ejercicio Número 3")
# Solicitar datos al usuario
nombre = input("Introduce tu nombre: ")
edad = input("Introduce tu edad: ")
ciudad = input("Introduce tu ciudad de nacimiento: ")

# Crear tupla con los datos
informacion = (nombre, edad, ciudad)

# Desempaquetar la tupla
nombre_usuario, edad_usuario, ciudad_usuario = informacion

# Imprimir mensaje formateado
print(f"\nEl usuario {nombre_usuario}, de {edad_usuario} años, nació en {ciudad_usuario}.")



#Ejercicio Numero 4
print(" ")
print(" ")
print("·Ejercicio Número 4")
# Inicializar diccionario con contactos
agenda = {
    "Juan": "555-1234",
    "María": "555-5678"
}

# Pedir al usuario un nombre para buscar
nombre_buscar = input("\nIntroduce el nombre del contacto a buscar: ")

# Verificar si el contacto existe
if nombre_buscar in agenda:
    print(f"Teléfono de {nombre_buscar}: {agenda[nombre_buscar]}")
else:
    print("Contacto no encontrado.")



#Ejercicio Numero 5
print(" ")
print(" ")
print("·Ejercicio Número 5")
# Crear lista de calificaciones
calificaciones = [85, 90, 78, 92, 88]

# Calcular promedio y encontrar notas más alta y baja
suma_calificaciones = sum(calificaciones)
promedio = suma_calificaciones / len(calificaciones)
nota_mas_alta = max(calificaciones)
nota_mas_baja = min(calificaciones)

# Imprimir resultados
print("\nAnálisis de Calificaciones:")
print(f"Promedio: {promedio:.2f}")
print(f"Nota más alta: {nota_mas_alta}")
print(f"Nota más baja: {nota_mas_baja}")