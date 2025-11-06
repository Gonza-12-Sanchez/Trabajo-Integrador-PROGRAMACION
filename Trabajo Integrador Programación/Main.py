from Funciones import *
#PROGRAMA PRINCIPAL.
#Obtenemos una matriz con la informacion del archivo.
info_archivo = matriz_info_archivo()
#Creamos un menu para el usuario.
while True:
    print("--" * 15)
    print("****       MENU         ****")
    print("1. Buscar un país por nombre")
    print("2. Filtrar países")
    print("3. Ordenar países")
    print("4. Mostrar estadísticas")
    print("5. Agregar país")
    print("6. Salir")
    #Leemos la opcion seleccionada.
    opcion = input("Ingrese una opcion: ")
    #Verificamos que la opcion sea válida.
    while opcion == "" or not opcion.isdigit() or opcion not in ("1","2","3","4","5","6"):
        opcion = input("Opción Inválida. Por favor ingrese otra: ")
    #Realizamos la opcion seleccionada.
    if opcion == "1":
        while True:
            print("--" * 15)
            #Solicitamos al usuario que ingrese el pais a buscar.
            nombre = input("Ingrese el nombre del país a buscar (Mínimo 3 letras): ")
            #Verificamos que el nombre ingresado sea válido.
            while nombre == "" or nombre.isdigit() or len(nombre) < 3:
                nombre = input("Nombre del país inválido. Ingrese otro nombre (o 's' para volver al menu): ")
                #Verificamos si el usuario desea volver.
                if nombre == "s":
                    break
            #Verificamos de nuevo si el usuario eligio volver, o seguir con la opcion.
            if nombre == "s":
                break
            #Si no eligio volver, realizamos la opcion.
            buscar_pais(nombre,info_archivo)
            #Preguntamos si desea seguir con la misma opcion.
            finalizar = input("¿Desea buscar otro pais? (si/no) ").lower()
            while finalizar not in ("si","no"):
                finalizar = input("Respuesta inválida. Ingrese si o no: ")
            if finalizar == "no":
                break
    elif opcion == "2":
        while True:
            print("--" * 15)
            #Solicitamos al usuario que ingrese que tipo de filtracion desea hacer.
            print("¿Qué tipo de filtracion desea hacer?")
            print("1) Por continente")
            print("2) Por rango de poblacion")
            print("3) Por rango de superficie")
            print("4) Volver al menu")
            opcion_filtrado = input("Ingrese una opcion: ")
            #Verificamos que la opcion ingresada sea válida.
            while opcion_filtrado == "" or not opcion_filtrado.isdigit() or opcion_filtrado not in ("1","2","3","4"):
                opcion_filtrado = input("Opción Inválida. Por favor ingrese otra: ")
            #Realizamos la opcion seleccionada.
            if opcion_filtrado == "1":
                #Solicitamos al usuario que ingrese un continente.
                continente = input("Ingrese el continente: ")
                #Verificamos que el continente ingresado sea válido.
                while continente == "" or continente.isdigit():
                    continente = input("Continente ingresado inválido. Por favor ingrese otro: ")
                #Realizamos la opcion.
                filtrar_pais_continente(continente,info_archivo)
            elif opcion_filtrado == "2":
                #Solicitamos al usuario que ingrese el rango minimo y máximo de la poblacion.
                print("-- Ingrese el rango de poblacion --")
                min = input("Rango mínimo: ")
                #Verificamos que el rango sea válido.
                while min == "" or not min.isdigit() or int(min) < 1:
                    min = input("Rango mínimo inválido. Por favor ingrese otro: ")
                #Solicitamos el rango máximo.
                max = input("Rango máximo: ")
                #Verificamos que el rango sea correcto.
                while max == "" or not max.isdigit() or int(max) <= int(min):
                    max = input("Rango máximo inválido. Por favor ingrese otro: ")
                #Despues de realizar las verificaciones realizamos la filtracion.
                filtrar_pais_poblacion(min,max,info_archivo)
            elif opcion_filtrado == "3":
                #Solicitamos al usuario que ingrese el rango minimo y máximo de la superficie.
                print("-- Ingrese el rango de superficie --")
                min = input("Rango mínimo: ")
                #Verificamos que el rango sea válido.
                while min == "" or not min.isdigit() or int(min) < 1: 
                    min = input("Rango mínimo inválido. Por favor ingrese otro: ")
                #Solicitamos el rango máximo.
                max = input("Rango máximo: ")
                #Verificamos que el rango sea correcto.
                while max == "" or not max.isdigit() or int(max) <= int(min):
                    max = input("Rango máximo inválido. Por favor ingrese otro: ")
                #Despues de realizar las verificaciones realizamos la filtracion.
                filtrar_pais_superficie(min,max,info_archivo)
            else:
                break
            #Preguntamos si desea seguir con la misma opcion.
            finalizar = input("¿Desea realizar algun otro tipo de filtracion? (si/no) ").lower()
            while finalizar not in ("si","no"):
                finalizar = input("Respuesta inválida. Ingrese si o no: ")
            if finalizar == "no":
                break
    elif opcion == "3":
        while True:
            print("--" * 15)
            #Solicitamos al usuario que ingrese que tipo de ordenamiento desea hacer.
            print("¿Qué tipo de ordenamiento desea hacer?")
            print("1) Por nombre (A-Z)")
            print("2) Por población")
            print("3) Por superficie")
            print("4) Volver al menu")
            opcion_ordenamiento = input("Ingrese una opcion: ")
            #Verificamos que la opcion ingresada sea válida.
            while opcion_ordenamiento == "" or not opcion_ordenamiento.isdigit() or opcion_ordenamiento not in ("1","2","3","4"):
                opcion_ordenamiento = input("Opción Inválida. Por favor ingrese otra: ")
            #Realizamos la opcion seleccionada.
            if opcion_ordenamiento == "1":
                #Realizamos la opcion seleccionada.
                ordenar_pais_nombre(info_archivo)
            elif opcion_ordenamiento == "2":
                #Solicitamos al usuario que ingrese una opcion.
                print("¿Desea un ordenamiento por poblacion Descendente o Ascendente?")
                print("1) Descendente")
                print("2) Ascendente")
                eleccion = input("Ingrese una opcion: ")
                #Verificamos que la opcion sea válida.
                while eleccion == "" or not eleccion.isdigit() or eleccion not in ("1","2"):
                    eleccion = input("Elección inválida. Ingrese otra: ")
                #Despues de realizar la verificación realizamos el ordenamiento.
                ordenar_pais_poblacion(eleccion,info_archivo)
            elif opcion_ordenamiento == "3":
                #Solicitamos al usuario que ingrese una opcion.
                print("¿Desea un ordenamiento por superficie Descendente o Ascendente?")
                print("1) Descendente")
                print("2) Ascendente")
                eleccion = input("Ingrese una opcion: ")
                #Verificamos que la opcion sea válida.
                while eleccion == "" or not eleccion.isdigit() or eleccion not in ("1","2"):
                    eleccion = input("Elección inválida. Ingrese otra: ")
                #Despues de realizar la verificación realizamos el ordenamiento.
                ordenar_pais_superficie(eleccion,info_archivo)
            else:
                break
            #Preguntamos si desea seguir con la misma opcion.
            finalizar = input("¿Desea realizar algun otro tipo de ordenamiento? (si/no) ").lower()
            while finalizar not in ("si","no"):
                finalizar = input("Respuesta inválida. Ingrese si o no: ")
            if finalizar == "no":
                break
    elif opcion == "4":
        while True:
            print("--" * 15)
            #Solicitamos al usuario que ingrese que estadística desea ver.
            print("¿Qué estadística desea ver?")
            print("1) País con mayor y menor población")
            print("2) Promedio de población")
            print("3) Promedio de superfice")
            print("4) Cantidad de países por continente")
            print("5) Volver al menu")
            opcion_estadística = input("Ingrese una opcion: ")
            #Verificamos que la opcion ingresada sea válida.
            while opcion_estadística == "" or not opcion_estadística.isdigit() or opcion_estadística not in ("1","2","3","4","5"):
                opcion_estadística = input("Opción Inválida. Por favor ingrese otra: ")
            #Realizamos la opcion seleccionada.
            if opcion_estadística == "1":
                mostrar_pais_mayor_y_menor_población(info_archivo)
            elif opcion_estadística == "2":
                mostrar_promedio_poblacion(info_archivo)
            elif opcion_estadística == "3":
                mostrar_promedio_superficie(info_archivo)
            elif opcion_estadística == "4":
                mostrar_cantidad_paises_por_continente(info_archivo)
            else:
                break
            #Preguntamos si desea seguir con la misma opcion.
            finalizar = input("¿Desea ver algun otro tipo de estadística? (si/no) ").lower()
            while finalizar not in ("si","no"):
                finalizar = input("Respuesta inválida. Ingrese si o no: ")
            if finalizar == "no":
                break
    elif opcion == "5":
        while True:
            #Solicitamos los distintos datos para agregar un nuevo país al archivo. Para esto usamos una funcion.
            nombre,poblacion,superficie,nombre_continente,volver = leer_y_validar_datos_pais(info_archivo)
            #Verificamos si el usuario desea seguir con la opcion.
            if volver == "s":
                break
            #Despues de leer y validar los datos del país, llamamos a una funcion para agregar dichos datos al archivo.
            agregar_pais(nombre,poblacion,superficie,nombre_continente) 
            #Actualizamos la matriz con la informacion del archivo.
            info_archivo = matriz_info_archivo()
            #Mostramos un mensaje de exito.
            print("Se registro el país correctamente!")
            #Preguntamos si desea seguir con la misma opcion.
            finalizar = input("¿Desea agregar otro país? (si/no) ").lower()
            while finalizar not in ("si","no"):
                finalizar = input("Respuesta inválida. Ingrese si o no: ")
            if finalizar == "no":
                break
    else:
        print("Hasta luego!")
        break