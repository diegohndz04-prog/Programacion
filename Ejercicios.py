#Ejercicio Numero 1
print("�Ejercicio N�mero 1")
# Solicitar dos n�meros al usuario
num1 = float(input("Introduce el primer n�mero: "))
num2 = float(input("Introduce el segundo n�mero: "))

# Realizar operaciones
suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2 if num2 != 0 else "No se puede dividir por cero"

# Imprimir resultados
print(f"\nResultados:")
print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicaci�n: {multiplicacion}")
print(f"Divisi�n: {division}")



#Ejercicio Numero 2
print(" ")
print(" ")
print("�Ejercicio N�mero 2")
# Crear lista vac�a
lista_compras = []

# A�adir tres art�culos
lista_compras.append("Leche")
lista_compras.append("Pan")
lista_compras.append("Huevos")

# Imprimir lista final y total de art�culos
print("\nLista de Compras:")
for articulo in lista_compras:
    print("-", articulo)

print(f"\nTotal de art�culos: {len(lista_compras)}")



#Ejercicio Numero 3
print(" ")
print(" ")
print("�Ejercicio N�mero 3")
# Solicitar datos al usuario
nombre = input("Introduce tu nombre: ")
edad = input("Introduce tu edad: ")
ciudad = input("Introduce tu ciudad de nacimiento: ")

# Crear tupla con los datos
informacion = (nombre, edad, ciudad)

# Desempaquetar la tupla
nombre_usuario, edad_usuario, ciudad_usuario = informacion

# Imprimir mensaje formateado
print(f"\nEl usuario {nombre_usuario}, de {edad_usuario} a�os, naci� en {ciudad_usuario}.")



#Ejercicio Numero 4
print(" ")
print(" ")
print("�Ejercicio N�mero 4")
# Inicializar diccionario con contactos
agenda = {
    "Juan": "555-1234",
    "Mar�a": "555-5678"
}

# Pedir al usuario un nombre para buscar
nombre_buscar = input("\nIntroduce el nombre del contacto a buscar: ")

# Verificar si el contacto existe
if nombre_buscar in agenda:
    print(f"Tel�fono de {nombre_buscar}: {agenda[nombre_buscar]}")
else:
    print("Contacto no encontrado.")



#Ejercicio Numero 5
print(" ")
print(" ")
print("�Ejercicio N�mero 5")
# Crear lista de calificaciones
calificaciones = [85, 90, 78, 92, 88]

# Calcular promedio y encontrar notas m�s alta y baja
suma_calificaciones = sum(calificaciones)
promedio = suma_calificaciones / len(calificaciones)
nota_mas_alta = max(calificaciones)
nota_mas_baja = min(calificaciones)

# Imprimir resultados
print("\nAn�lisis de Calificaciones:")
print(f"Promedio: {promedio:.2f}")
print(f"Nota m�s alta: {nota_mas_alta}")
print(f"Nota m�s baja: {nota_mas_baja}")