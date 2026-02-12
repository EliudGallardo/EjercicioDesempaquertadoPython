
datos = [1,2,3,4,5]
# Empaquetar el arreglo en una tupla
print(f"Lista original original: {datos}")

#for i in datos:
#    copia_datos.append(i)

#copia_datos = tuple(datos)


#FORMA ADECUADA DE HACER UNA COPIA DE UNA LISTA CON DESEMPEQUETADO
copia_datos = [*datos] # Otra forma de copiar una lista, usando el operador de desempaquetado

#IMPRESION DE UNA LISTA CON DESEMPEQUETADO
print(f"Lista 2: {copia_datos}")
copia_datos.append(6)
print(*datos) 
print(f"Lista original ID  {id(datos)}, contenido: {datos}")
print(f"Lista 2 ID {id(copia_datos)}, contenido: {copia_datos}")


# Ejemplo de función con argumentos variables
def impresion_nombres(*nombres):
    print(f"los nombres son:", *nombres)
impresion_nombres("Daniel", "Maria", "Juan") # Esto no funciona porque la función espera un solo argumento, no una lista de argumentos

def impresion_datos(**data):
    print(f"los datos son:{data}")
    
    #Argumentos independientes, no se pueden usar con el operador de desempaquetado
    impresion_datos(nombre="Diego",tel=5522817857,carrera= "ISC") # Esto no funciona porque la función espera un solo argumento, no una lista de argumentos
    diccionario_datos = {"marca":"Dell", "modelo":"Inspiron", "fecha":"2024"}
    copia_diccionario = {**diccionario_datos} # Otra forma de copiar un diccionario, usando el operador de desempaquetado
    impresion_datos(**copia_diccionario) # Esto funciona porque la función espera un solo argumento, y el operador de desempaquetado convierte el diccionario en argumentos independientes
    
    