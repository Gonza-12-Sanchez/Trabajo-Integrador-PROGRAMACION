#                               FUNCIONES
#----------FUNCION GENERAL----------
def matriz_info_archivo():
    info_archivo = []
    #Creamos una matriz con la informacion del archivo.
    with open("DataSetPaises.csv","r") as archivo:
        for linea in archivo:
            linea = linea.strip()
            info_pais = linea.split(",")
            info_archivo.append(info_pais)
    return info_archivo


#----------OPCION BUSCAR----------
def buscar_pais(nombre,info_archivo):
    #Inicializamos la variable a utilizar.
    existe = False
    paises_encontrados = []
    #Buscamos el país ingresado en la matriz que contiene la informacion del archivo.
    for pais in info_archivo:
        if pais[0].lower() == nombre.lower() or nombre.lower() in pais[0].lower() :
            existe = True
            #Si existe, agregamos la informacion a la lista.
            paises_encontrados.append(pais)
    if existe == False:
        print("País no encontrado!")
    elif len(paises_encontrados) > 1:
        print("Paises encontrados!")
        print("----Informacion----")
        for pais in paises_encontrados:
            print(f"Nombre: {pais[0]} | Población: {pais[1]} | Superficie: {pais[2]} | Continente: {pais[3]}") 
    else:
        print("País Encontrado!")
        print("----Informacion----")
        print(f"Nombre: {paises_encontrados[0][0]} | Población: {paises_encontrados[0][1]} | Superficie: {paises_encontrados[0][2]} | Continente: {paises_encontrados[0][3]}")


#----------OPCIONES FILTRAR----------
def filtrar_pais_continente(continente,info_archivo):
    #Inicializamos variables a utilizar.
    paises_encontrados = []
    existe = False
    #Filtramos paises por el continente ingresado.
    for pais in info_archivo:
        #Verificamos si el continente ingresado coincide con el de algun país.
        if pais[3].lower() == continente.lower():
            existe = True
            #Si coinciden, guardamos el nombre del pais en la lista.
            paises_encontrados.append(pais[0])
    #Mostramos los paises encontrados (si los hay).
    if existe and len(paises_encontrados) > 1:
        print("Países encontrados!")
        print(f"Los países encontrados en el continente {continente} son:")
        for pais in paises_encontrados:
            print(pais)
    elif existe:
        print("País encontrado!")
        print(f"El país encontrado en el continente {continente} es: {paises_encontrados[0]}")
    else:
        print(f"No se encontro ningun país en el continente {continente}!")

def filtrar_pais_poblacion(min,max,info_archivo):
    #Inicializamos las variables a utilizar.
    existe = False
    paises_encontrados = []
    #Realizamos la filtracion de paises por el rango dado.
    for pais in info_archivo:
        #Verificamos si el rango ingresado coincide con el de algún país.
        if int(pais[1]) >= int(min) and int(pais[1]) <= int(max):
            existe = True
            paises_encontrados.append(pais[0])
            paises_encontrados.append(pais[1])
    #Mostramos los paises encontrados (si los hay)
    if existe and len(paises_encontrados) > 2:
        print("Países encontrados!")
        print(f"Los países econtrados con un rango de poblacion de entre {min}-{max} son:")
        for i in range(0,len(paises_encontrados),2):
            print(f"País: {paises_encontrados[i]} | Población: {paises_encontrados[i + 1]}")
    elif existe:
        print("País encontrado!")
        print(f"El país encontrado con un rango de población de entre {min}-{max} es:")
        print(f"País: {paises_encontrados[0]} | Población: {paises_encontrados[1]}")
    else:
        print(f"No se encontro ningún país con un rango de población de entre {min}-{max}")        

def filtrar_pais_superficie(min, max,info_archivo):
    #Inicializamos las variables a utilizar.
    existe = False
    paises_encontrados = []
    #Realizamos la filtracion de paises por el rango de superficie dado.
    for pais in info_archivo:
        #Verificamos si el rango de superficie ingresado coincide con el de algún país.
        if int(pais[2]) >= int(min) and int(pais[2]) <= int(max):
            existe = True
            paises_encontrados.append(pais[0])
            paises_encontrados.append(pais[2])
    #Mostramos los paises encontrados (si los hay)
    if existe and len(paises_encontrados) > 2:
        print("Países encontrados!")
        print(f"Los países econtrados con un rango de superficie de entre {min}-{max} son:")
        for i in range(0,len(paises_encontrados),2):
            print(f"País: {paises_encontrados[i]} | Superficie: {paises_encontrados[i + 1]}")
    elif existe:
        print("País encontrado!")
        print(f"El país encontrado con un rango de superficie de entre {min}-{max} es:")
        print(f"País: {paises_encontrados[0]} | Superficie: {paises_encontrados[1]}")
    else:
        print(f"No se encontro ningún país con un rango de superficie de entre {min}-{max}")


#----------OPCIONES ORDENAR----------
def ordenar_pais_nombre(info_archivo):
    #Definimos la lista a utilizar.
    paises_ordenados=[]
    #Ordenamos los paises de la A a la Z.
    for pais in info_archivo:
        #Agregamos los nombres de los paises a una lista.
        paises_ordenados.append(pais[0])
    #Ordenamos los países.
    for i in range(0,len(paises_ordenados)):
        for j in range(i+1,len(paises_ordenados)):
            if paises_ordenados[i].lower() > paises_ordenados[j].lower():
                paises_ordenados[i], paises_ordenados[j] = paises_ordenados[j], paises_ordenados[i]
    #Mostramos los paises ordenados.
    print("Se ordenaron alfabéticamente los países!")
    for pais in paises_ordenados:
        print(pais)

def ordenar_pais_poblacion(eleccion,info_archivo):
    #Definimos la lista a utilizar.
    paises_ordenados=[]
    #Ordenamos los paises por poblacion de manera ascendente o descendente, segun la eleccion del usuario.
    if eleccion == "1":
        #Si la eleccion es igual la 1, ordenamos los paises de manera descendente.
        for pais in info_archivo:
            #Agregamos los nombres y poblaciones de los paises a una lista.
            paises_ordenados.append([pais[0],pais[1]])
        #Ordenamos los países.
        for i in range(0,len(paises_ordenados)):
            for j in range(i+1,len(paises_ordenados)):
                if int(paises_ordenados[i][1]) < int(paises_ordenados[j][1]):
                    paises_ordenados[i], paises_ordenados[j] = paises_ordenados[j], paises_ordenados[i]
        #Mostramos los paises ordenados.
        print("Se ordenaron los países por poblacion de manera descendente!")
        for pais in paises_ordenados:
            print(f"País: {pais[0]} | Población: {pais[1]}")
    else:
        #Si la opcion es 2, ordenamos los paises de manera ascendente
        for pais in info_archivo:
            #Agregamos los nombres y poblaciones de los paises a una lista.
            paises_ordenados.append([pais[0],pais[1]])
        #Ordenamos los países.
        for i in range(0,len(paises_ordenados)):
            for j in range(i+1,len(paises_ordenados)):
                if int(paises_ordenados[i][1]) > int(paises_ordenados[j][1]):
                    paises_ordenados[i], paises_ordenados[j] = paises_ordenados[j], paises_ordenados[i]
        #Mostramos los paises ordenados.
        print("Se ordenaron los países por poblacion de manera ascendente!")
        for pais in paises_ordenados:
            print(f"País: {pais[0]} | Población: {pais[1]}")

def ordenar_pais_superficie(eleccion,info_archivo):
    #Definimos la lista a utilizar.
    paises_ordenados=[]
    #Ordenamos los paises por superficie de manera ascendente o descendente, segun la eleccion del usuario.
    if eleccion == "1":
        #Si la eleccion es igual la 1, ordenamos los paises de manera descendente.
        for pais in info_archivo:
            #Agregamos los nombres y superficies de los paises a una lista.
            paises_ordenados.append([pais[0],pais[2]])
        #Ordenamos los países.
        for i in range(0,len(paises_ordenados)):
            for j in range(i+1,len(paises_ordenados)):
                if int(paises_ordenados[i][1]) < int(paises_ordenados[j][1]):
                    paises_ordenados[i], paises_ordenados[j] = paises_ordenados[j], paises_ordenados[i]
        #Mostramos los paises ordenados.
        print("Se ordenaron los países por superficie de manera descendente!")
        for pais in paises_ordenados:
            print(f"País: {pais[0]} | Superficie: {pais[1]}")
    else:
        #Si la opcion es 2, ordenamos los paises de manera ascendente
        for pais in info_archivo:
            #Agregamos los nombres y superficies de los paises a una lista.
            paises_ordenados.append([pais[0],pais[2]])
        #Ordenamos los países.
        for i in range(0,len(paises_ordenados)):
            for j in range(i+1,len(paises_ordenados)):
                if int(paises_ordenados[i][1]) > int(paises_ordenados[j][1]):
                    paises_ordenados[i], paises_ordenados[j] = paises_ordenados[j], paises_ordenados[i]
        #Mostramos los paises ordenados.
        print("Se ordenaron los países por superficie de manera ascendente!")
        for pais in paises_ordenados:
            print(f"País: {pais[0]} | Superficie: {pais[1]}")


#----------OPCIONES MOSTRAR----------
def mostrar_pais_mayor_y_menor_población(info_archivo):
    #Definimos las listas a utilizar.
    mayor_poblacion = []
    menor_poblacion = []
    #Mostramos los paises con mayor y menor poblacion del archivo.
    #Inicializamos las listas "mayor_poblacion" y "menor_poblacion".
    mayor_poblacion.append([info_archivo[0][0],info_archivo[0][1]])
    menor_poblacion.append([info_archivo[0][0],info_archivo[0][1]])
    #Buscamos el pais con mayor y menor poblacion.
    for i in range(1,len(info_archivo)):
        if int(mayor_poblacion[0][1]) <= int(info_archivo[i][1]):
            mayor_poblacion[0] = [info_archivo[i][0],info_archivo[i][1]]
        elif int(menor_poblacion[0][1]) >= int(info_archivo[i][1]):
            menor_poblacion[0] = [info_archivo[i][0],info_archivo[i][1]]
    #Buscamos si hay otro pais con la misma poblacion del mayor o menor.
    for i in range(0,len(info_archivo)):
        if int(mayor_poblacion[0][1]) == int(info_archivo[i][1]) and mayor_poblacion[0][0] != info_archivo[i][0]:
            mayor_poblacion.append([info_archivo[i][0],info_archivo[i][1]])
        elif int(menor_poblacion[0][1]) == int(info_archivo[i][1]) and menor_poblacion[0][0] != info_archivo[i][0]:
            menor_poblacion.append([info_archivo[i][0],info_archivo[i][1]])
    #Mostramos el país con mayor y menor población.
    if len(mayor_poblacion) > 1 and len(menor_poblacion) > 1:
        print("-- Paises con mayor población --")
        for paisMayor in mayor_poblacion:
            print(f"Nombre: {paisMayor[0]} | Población: {paisMayor[1]}")
        print("-- Paises con menor población --")
        for paisMenor in menor_poblacion:
            print(f"Nombre: {paisMenor[0]} | Población: {paisMenor[1]}")
    elif len(mayor_poblacion) > 1:
        print("-- Paises con mayor población --")
        for paisMayor in mayor_poblacion:
            print(f"Nombre: {paisMayor[0]} | Población: {paisMayor[1]}")
        print("-- País con menor población --")
        print(f"Nombre: {menor_poblacion[0][0]} | Población: {menor_poblacion[0][1]}")
    elif len(menor_poblacion) > 1:
        print("-- País con mayor población --")
        print(f"Nombre: {mayor_poblacion[0][0]} | Población: {mayor_poblacion[0][1]}")
        print("-- Paises con menor población --")
        for paisMenor in menor_poblacion:
            print(f"Nombre: {paisMenor[0]} | Población: {paisMenor[1]}")
    else:
        print("-- País con mayor población --")
        print(f"Nombre: {mayor_poblacion[0][0]} | Población: {mayor_poblacion[0][1]}")
        print("-- País con menor población --")
        print(f"Nombre: {menor_poblacion[0][0]} | Población: {menor_poblacion[0][1]}")

def mostrar_promedio_poblacion(info_archivo):
    #Inicializamos la variable a utilizar.
    suma_total_poblacion = 0
    #Mostramos el promedio de poblacion entre todos los países.
    for pais in info_archivo:
        #Hacemos una suma total de la poblacion de los paises en el archivo.
        suma_total_poblacion += int(pais[1])
    #Despues de tener la suma total de la poblacion de los paises, mostramos el promedio por pantalla.
    print(f"El PROMEDIO DE POBLACIÓN entre los distintos países es de {suma_total_poblacion/len(info_archivo)}")

def mostrar_promedio_superficie(info_archivo):
    #Inicializamos la variable a utilizar.
    suma_total_superficie = 0
    #Mostramos el promedio de poblacion entre todos los países.
    for pais in info_archivo:
        #Hacemos una suma total de la poblacion de los paises en el archivo.
        suma_total_superficie += int(pais[2])
    #Despues de tener la suma total de la poblacion de los paises, mostramos el promedio por pantalla.
    print(f"El PROMEDIO DE SUPERFICIE entre los distintos países es de {suma_total_superficie/len(info_archivo)}")

def mostrar_cantidad_paises_por_continente(info_archivo):
    #Definimos las listas a utilizar.
    continentes = []
    cant_paises = []
    #Mostramos la cantidad de países por continente.
    #Identificamos los distintos continentes.
    for i in range(0,len(info_archivo)):
        if i == 0:
            #Si es la primera vuelta, agregamos el continente a la lista.
            continentes.append(info_archivo[i][3])
        else:
            #Sino es la primera vuelta, verificamos si el continente ya se encuentra dentro de la lista.
            #Inicializamos la variable a utilizar.
            repetido = False
            #Verificamos si el continente ya está en la lista.
            for j in range(0,len(continentes)):
                if continentes[j].lower() == info_archivo[i][3].lower():
                    #Si el continente ya esta en la lista, cambiamos el valor de la variable "repetido".
                    repetido = True
                    break
            #Si el continente no está repetido en la lista, la agregamos.
            if repetido == False:
                continentes.append(info_archivo[i][3])
    #Identificamos la cantidad de paises por continente.
    for continente in continentes:
        #Inicializamos la variable a utilizar.
        paises = 0
        for pais in info_archivo:
            if continente.lower() == pais[3].lower():
                paises += 1
        #Guardamos la cantidad de paises en una lista.
        cant_paises.append(paises)
    #Mostramos la cantidad de paises por continente.
    for i in range(0,len(continentes)):
        print(f"Continente: {continentes[i]} | Cantidad de paises: {cant_paises[i]}")


#----------OPCION AGREGAR PAISES----------
def leer_y_validar_datos_pais(info_archivo):
    #Inicializamos las variables a utilizar.
    nombre_paises = []
    volver = ""
    #Solicitamos y verificamos los datos del país.
    print("---- DATOS NUEVO PAÍS ----")
    #Antes que nada, creamos una lista con todos los nombres de los paises en el archivo, para tener una ayuda con la verificacion.
    for pais in info_archivo:
        nombre_paises.append(pais[0].lower())
    #Ingreso y verificacion nombre país.
    print("**** NOMBRE ****")
    nombre = input("Ingrese el nombre del país: ")
    while nombre == "" or nombre.isdigit() or nombre.lower() in nombre_paises:
        print("Nombre inválido o ya existente. ¿Desea volver al menu o ingresar otro nombre? (Volver = s /Ingresar otro nombre = cualquier otra tecla)")
        volver = input("Ingrese una opcion: ").lower()
        #Verificamos si el usuario desea volver.
        if volver == "s":
            return "","","","",volver
        #Si no desea volver, solicitamos que ingrese de nuevo el nombre del país. 
        nombre = input("Ingrese el nombre del país: ")
    #Ingreso y verificacion poblacion.
    print("**** POBLACIÓN ****")
    poblacion = input("Ingrese la población del país: ")
    while poblacion == "" or not poblacion.isdigit() or int(poblacion) < 1:
        print("Población inválida. ¿Desea volver al menu o ingresar otra población? (Volver = s /Ingresar otra población = cualquier otra tecla)")
        volver = input("Ingrese una opcion: ").lower()
        #Verificamos si el usuario desea volver.
        if volver == "s":
            return "","","","",volver
        #Si no desea volver, solicitamos que ingrese de nuevo la poblacion del país.
        poblacion = input("Ingrese la población del país: ")
    #Ingreso y verificacion de superficie.
    print("**** SUPERFICIE ****")
    superficie = input("Ingrese la superficie del país: ")
    while superficie == "" or not superficie.isdigit() or int(superficie) < 1:
        print("Superficie inválida. ¿Desea volver al menu o ingresar otra superficie? (Volver = s /Ingresar otra superficie = cualquier otra tecla)")
        volver = input("Ingrese una opcion: ").lower()
        #Verificamos si el usuario desea volver.
        if volver == "s":
            return "","","","",volver
        #Si no desea volver, solicitamos que ingrese de nuevo la superficie del país.
        superficie = input("Ingrese la superficie del país: ")
    #Ingreso y verificacion de continente.
    print("**** CONTINENTE ****")
    continente = input("Ingrese el continente del país: ")
    while continente == "" or continente.isdigit():
        print("Continente inválido. ¿Desea volver al menu o ingresar otro continente? (Volver = s /Ingresar otro continente = cualquier otra tecla)")
        volver = input("Ingrese una opcion: ").lower()
        #Verificamos si el usuario desea volver.
        if volver == "s":
            return "","","","",volver
        #Si no desea volver, solicitamos que ingrese de nuevo el nombre del país.
        continente = input("Ingrese el continente del país: ")
    #Retornamos los datos validados.
    return nombre,poblacion,superficie,continente,volver

def agregar_pais(nombre,poblacion,superficie,continente):
    #Agregamos la informacion del nuevo pais al archivo.
    #Juntamos toda la informacion en una variable.
    info_nuevo_pais = nombre + "," + poblacion + "," + superficie + "," + continente + "\n"
    #Agregamos dicha variable al archivo.
    with open("DataSetPaises.csv","a") as archivo:
        archivo.write(info_nuevo_pais)