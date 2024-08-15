import json
from datetime import datetime

def abrir_archivo(nombre_archivo="estudiantes.json"):
    try:
        with open(nombre_archivo, "r") as openfile:
            return json.load(openfile)
    except FileNotFoundError:
        return {}

def guardar_archivo(nombre_archivo="estudiantes.json", data=None):
    with open(nombre_archivo, "w") as outfile:
        json.dump(data, outfile, indent=4)



def abrirRegistro():
    miJson=[]
    with open("Registro.json","r")as openfile:
        miJson=json.load(openfile)
    return miJson

def guardararchivoRegistro():
    try:
        with open("Registro.json","r")as openfile:
            return json.load(openfile)
    except FileNotFoundError:
        return []

def guardaditoRegistro(miData):
    with open("Registro.json","w")as outfile:
        json.dump(miData,outfile)



postuIncritos=[]
postu=[]


#Bienvenida al usuario
print("========================================================")
print("   BIENVENIDO AL DEPARTAMENTO ACADEMICO DE CAMPUSLAND   ")
print("========================================================")


rol=input("""Que rol tienes dentro de campus: 
          
    1. Coordinador
    2. Trainer
    3. Camper 
    4. registro de entrada
    """)

booleano=True

registro=guardararchivoRegistro()

while booleano:
    contador=0
    jsonn=[]

    #####seccion de registro de ventas

    if rol=="4":
        RegistroAbrir=abrir_archivo()
        print("-------------------------------------")
        print("--BIENVENIDO A REGISTRO DE ENTRADAS--")
        print("-------------------------------------")
        Nombre=input("ingresa tu nombre: ")
        id=input("ingresa tu id: ")
        actividades=input("Que actividades se realizaron dentro de la jornada: ")
        print("En que estado esta la sesion")
        print("-Activa")
        print("-Inactiva")
        print("-Finalizada")
        secion=input("")

        entradas={
            "id": id,
            "Ingreso": "datetime",
            "Nombre": Nombre,
            "actividades_realizadas_durante_sesion ":actividades,
            "Estado_de_la_sesion":secion 
        }
        registro.append(entradas)
        guardaditoRegistro(registro)


    #el usuario entra como el coordinador
    if rol=="1":
        data = abrir_archivo("estudiantes.json")
        print("============================")
        print("   BIENVENIDO COORDINADOR   ")
        print("============================") 
        print("1. Inscribir postulados")
        print("2. Ingresar nota a campers que finalizaron modulo") 
        print("3. Campers en peligro")
    QueDesea=input("que funcion vas a realizar:")

    #opcion 1 de las acciones que puede realizar el coordinador
    if QueDesea=="1":
            jsonn = abrir_archivo()
            for i in jsonn[0]['postulados']:
                data = abrir_archivo("estudiantes.json")
                contador= contador+1
                print("")
                print("================================================")
                print("POSTULANTES QUE PRESENTARON LA PRUEBA DE INGRESO")
                print("================================================")
                print("id: ",i["id"])
                print("nombre: ",i["nombre"])
                print("apellido: ",i["apellido"])
                print("cedula: ",i["cedula"])
                print("acudiente: ",i["acudiente"])
                print("direcccion: ",i["direccion"])
                print("estado: ",i["estado"])
                print("ruta: ",i["ruta"])
                print("trainer: ",i["trainer"])
                print("")
                print("se le va a revisar la prueba a cada uno de los que postularon la prueba")
                estudiante=int(input("ingrese el id que identifica al postulado :"))

                parteTeorica=int(input("que promedio saco el postulado en la prueba teorica: "))
                partePractica=int(input("que promedio saco el postulado en la prueba practica: "))
                prueba=parteTeorica+partePractica/2

                if prueba >=60:
                    
                    #asignacion de estado en el que esta el camper
                    nuevoEstado= "isncrito"
                    jsonn[0]["postulados"][estudiante-1]["estado"] = nuevoEstado
                    guardar_archivo("estudiantes.json", data)
                    print("")

                    #asignacion de ruta del camper nuevo
                    print("ingrese la opcion en numero")
                    print("""rutas 
                          1.nodeJs
                          2.java
                          3.Netcore
                          """)
                    opcioRuta=input("que ruta tendra el camper")
                    print("")
                    
                    if opcioRuta=="2":
                        nuevaRuta= "java"
                        jsonn[0]["postulados"][estudiante-1]["ruta"] = nuevaRuta
                        guardar_archivo("estudiantes.json", data)
                        print("")
                        
                        #asignacion de trainer del camper
                        print("se le asigno la ruta al camper")
                        print("java")
                        nuevoEstado="cursando"
                        guardar_archivo("estudiantes.json", data)
                        
                        
                        trainerNuevo="jholver"
                        print("El trainer jholver es el encargado de la ruta java")
                        jsonn[0]["postulados"][estudiante-1]["trainer"] = trainerNuevo
                        guardar_archivo("estudiantes.json", data)
                        print("")

                        #asignacion de fecha de inicio del camper
                        nuevaFechaIni="12-06-2024"
                        print("iniciara el curso el 12-06-2024")
                        jsonn[0]["postulados"][estudiante-1]["fechaIni"] = nuevaFechaIni
                        guardar_archivo("estudiantes.json", data)
                        print("")

                        #fecha de finalizacion del camper
                        nuevafechaFin="30-06-2025"
                        print("Finalizara el curso el 30-06-2025")
                        jsonn[0]["postulados"][estudiante-1]["fechaFin"] = nuevafechaFin
                        guardar_archivo("estudiantes.json", data)
                        print("")

                        #salon que se le asignara al camper
                        print("")
                        nuevoSalon="apolo"
                        print("estara en el salon apolo")
                        print("tendra clase de 6-10 de la manaña")
                        jsonn[0]["postulados"][estudiante-1]["salon"] = nuevoSalon
                        guardar_archivo("estudiantes.json", data)
                        
                        nuevoGrupo="M1"
                        print("el camper estara en el grupo M1")
                        jsonn[0]["postulados"][estudiante-1]["grupo"] = nuevoGrupo
                        guardar_archivo("estudiantes.json", data)

                        nuevoOcupado="6-10"
                        jsonn[0]["postulados"][estudiante-1]["ocupado"] = nuevoOcupado
                        guardar_archivo("estudiantes.json", data)
                        
                        #temas o modulos que vera el camper
                        print("""el camper vera: 
                              fundamentos de programacion
                              programacion web
                              """)
                        print("")
                        print("programacion formal")
                        print("bases de datos")
                        print("backend")
                        queModulo=input("que otro modulo vera el camper :")
                        jsonn[0]["postulados"][estudiante-1]["modulo"] = queModulo
                        guardar_archivo("estudiantes.json", data)

                        #asignacion de una ruta al camper
                    elif nuevaRuta=="1":
                        nuevaRuta= "nodeJs"
                        jsonn[0]["postulados"][estudiante-1]["ruta"] = nuevaRuta
                        guardar_archivo("estudiantes.json", data)
                        print("")
                        
                        #asignacion de trainer del camper
                        print("se le asigno la ruta al camper")
                        print("nodeJs")
                        trainerNuevo="miguel"
                        print("El trainer miguel es el encargado de la ruta java")
                        jsonn[0]["postulados"][estudiante-1]["trainer"] = trainerNuevo
                        guardar_archivo("estudiantes.json", data)
                        print("")

                        #asignacion de fecha de inicio del camper
                        nuevaFechaIni="18-07-2024"
                        print("iniciara el curso el 18-07-2024")
                        jsonn[0]["postulados"][estudiante-1]["fechaIni"] = nuevaFechaIni
                        guardar_archivo("estudiantes.json", data)
                        print("")

                        #fecha de finalizacion del camper
                        nuevafechaFin="18-07-2025"
                        print("Finalizara el curso el 18-07-2025")
                        jsonn[0]["postulados"][estudiante-1]["fechaFin"] = nuevafechaFin
                        guardar_archivo("estudiantes.json", data)
                        print("")

                        #salon que se le asignara al camper
                        print("")
                        nuevoSalon="sputnik"
                        print("estara en el salon sputnik")
                        print("tendra clase de 11-3 de la tarde")
                        jsonn[0]["postulados"][estudiante-1]["salon"] = nuevoSalon
                        guardar_archivo("estudiantes.json", data)
                        
                        #si el camper no esta libre o el trainer esta ocuapdo con otro grupo
                        nuevoOcupado="11-3"
                        jsonn[0]["postulados"][estudiante-1]["ocupado"] = nuevoOcupado
                        guardar_archivo("estudiantes.json", data)
                        
                        print("el camper vera: \n*fundamentos de programacion\n*programacion web")
                        print("")
                        print("programacion formal")
                        print("bases de datos")
                        print("backend")
                        queModulo=input("que otro modulo vera el camper: ")
                        jsonn[0]["postulados"][estudiante-1]["modulo"] = queModulo
                        guardar_archivo("estudiantes.json", data)
                    
                    
                    elif nuevaRuta=="3":
                        nuevaRuta= "nodeJs"
                        jsonn[0]["postulados"][estudiante-1]["ruta"] = nuevaRuta
                        guardar_archivo("estudiantes.json", data)
                        print("")
                        
                        #asignacion de trainer del camper
                        print("se le asigno la ruta al camper")
                        print("nodeJs")
                        trainerNuevo="juanca"
                        print("El trainer juanca es el encargado de la ruta java")
                        jsonn[0]["postulados"][estudiante-1]["trainer"] = trainerNuevo
                        guardar_archivo("estudiantes.json", data)
                        print("")

                        #asignacion de fecha de inicio del camper
                        nuevaFechaIni="20-08-2024"
                        print("iniciara el curso el 20-08-2024")
                        jsonn[0]["postulados"][estudiante-1]["fechaIni"] = nuevaFechaIni
                        guardar_archivo("estudiantes.json", data)
                        print("")

                        #fecha de finalizacion del camper
                        nuevafechaFin="20-08-2025"
                        print("Finalizara el curso el 20-08-2025")
                        jsonn[0]["postulados"][estudiante-1]["fechaFin"] = nuevafechaFin
                        guardar_archivo("estudiantes.json", data)
                        print("")

                        #salon que se le asignara al camper
                        print("")
                        nuevoSalon="artemis"
                        print("estara en el salon artemis")
                        print("tendra clase de 3-7 de la noche")
                        jsonn[0]["postulados"][estudiante-1]["salon"] = nuevoSalon
                        guardar_archivo("estudiantes.json", data)
                        
                        nuevoOcupado="3-7"
                        jsonn[0]["postulados"][estudiante-1]["ocupado"] = nuevoOcupado
                        guardar_archivo("estudiantes.json", data)
                
                #eliminar camper si no pasa el filtro 
                else:
                    print("")
                    print("El postulante no podrá estar en el campus")
                    for camper in jsonn:
                        if camper.get("nombre")=="nombre del Camper" and camper.get("apellido")=="apellido del Camper" and camper.get("cedula")=="cedula del Camper":
                            jsonn.remove(camper)
                            print("Camper eliminado")
                            break
                
        #opcion 2 de lo que puede realizar el coordinador
    if QueDesea=="2":
            data = abrir_archivo("estudiantes.json")
            print("==================================")
            print("    INSCRIBIR NOTAS DE CAMPERS    ")
            print("==================================")
            print("")
            print("los grupos que finalizaron modulo son :")
            print("""
                  1. Grupo M1
                  2. Grupo P1
                  3. Grupo T1
                  4. Grupo T2
                  """)
            print("ingrese un de las opciones enumeradas")
            queGrupo=input("Ingrese 1 para actualizar rendimiento de campers de este salon: ")

            if queGrupo=="1":
                print("===============================================================================")
                print("   se le va a actualizar el rendiminto a cada camper que esta en el grupo M1   ")
                print("===============================================================================")
                contador=0
                
                #lista de los campers que finalizaron el modulo/filtro
                for i in estudiante[0]["postulados"]:
                    data = abrir_archivo("estudiantes.json")
                    contador= contador+1
                    print("")
                    print("======================================")
                    print("    CAMPERS QUE FINALIZARON MODULO    ")
                    print("======================================")
                    print("id",i["id"])
                    print("nombre",i["nombre"])
                    print("apellido",i["apellido"])
                    print("cedula",i["cedula"])
                    print("acudiente",i["acudiente"])
                    print("direcccion",i["direccion"])
                    print("estado",i["estado"])
                    print("")
                    print("se le va a revisar la prueba a cada uno de los que postularon la prueba")
                    estudiante=int((input("ingrese el id que identifica al camper: ")))
                    pruebateorica=int(input("ingrese el resultado obtenido en la prueba teorica: "))
                    pruebapractica=int(input("ingrese el resultado obtenido en la prueba practica: "))
                    
                    #promedio de las notas de las pruebas
                    teoric=0.30*pruebateorica
                    practic=0.60*pruebapractica
                    promedio=teoric+practic
                    
                    print("tuvo un promedio de ",promedio)
                    if promedio >= 60:
                        riesgoNuevo="alto"
                        jsonn["estudiantes"]["riesgo"] = riesgoNuevo
                        print("el estudiante",i["nombre"],"tuvo un rendimiento alto en el modulo java")
                        guardar_archivo("estudiantes.json", data)
                        print("")

                    elif promedio<= 59:
                            riesgoNuevo="bajo"
                            jsonn[1]["estudiantes"]["riesgo"] = riesgoNuevo
                            guardar_archivo("estudiantes.json", data)
                            print("el estudiante",i["nombre"],"tuvo un rendimiento bajo en el modulo java")
                            print("")
                            
                    if queGrupo=="2":
                        print("###############################################################################")
                        print("###se le va a actualizar el rendiminto a cada camper que esta en el grupo P1###")
                        print("################################################################################")
                        contador=0
                        
                        for i in jsonn[2]["estudiantes"]:
                            data = abrir_archivo("estudiantes.json")
                            contador= contador+1
                            print("")
                            print("######################################")
                            print("### CAMPERS QUE FINALIZARON MODULO ###")
                            print("######################################")
                            print("id",i["id"])
                            print("nombre",i["nombre"])
                            print("apellido",i["apellido"])
                            print("cedula",i["cedula"])
                            print("acudiente",i["acudiente"])
                            print("direcccion",i["direccion"])
                            print("estado",i["estado"])
                            print("")
                            print("se le va a revisar la prueba a cada uno de los que postularon la prueba")
                        estudiante=int((input("ingrese el id que identifica al camper: ")))
                        pruebateorica=int(input("ingrese el resultado obtenido en la prueba teorica: "))
                        pruebapractica=int(input("ingrese el resultado obtenido en la prueba practica: "))
                        teoric=0.30*pruebateorica
                        practic=0.60*pruebapractica
                        promedio=teoric+practic
                        print("tuvo un promedio de ",promedio)
                        
                        if promedio >= 60:
                            riesgoNuevo="alto"
                            jsonn[2]["estudiantes"][estudiante-1]["riesgo"] = riesgoNuevo
                            print("el estudiante",i["nombre"],"tuvo un rendimiento alto en la ruta nodjs")
                            guardar_archivo("estudiantes.json", data)
                            print("")
                            
                        elif promedio<= 59:
                                riesgoNuevo="bajo"
                                jsonn[2]["estudiantes"][estudiante-1]["riesgo"] = riesgoNuevo
                                guardar_archivo("estudiantes.json", data)
                                print("el estudiante",i["nombre"],"tuvo un rendimiento bajo en la ruta nodjs")
                                print("")
                    
                if queGrupo=="3":
                    print("###############################################################################")
                    print("######SE LE VA A ACTUALIZAR EL RENDIMINETO DE CADA CAMPER EN EL GRUPO T2######")
                    print("################################################################################")
                    contador=0
                    
                    for i in jsonn[3]["estudiantes"]:
                        data = abrir_archivo("estudiantes.json")
                        contador= contador+1
                        print("")
                        print("######################################")
                        print("### CAMPERS QUE FINALIZARON MODULO ###")
                        print("######################################")
                        print("id",i["id"])
                        print("nombre",i["nombre"])
                        print("apellido",i["apellido"])
                        print("cedula",i["cedula"])
                        print("acudiente",i["acudiente"])
                        print("direcccion",i["direccion"])
                        print("estado",i["estado"])
                        print("")
                        print("se le va a revisar la prueba a cada uno de los que postularon la prueba")
                        estudiante=int((input("ingrese el id que identifica al camper: ")))
                        pruebateorica=int(input("ingrese el resultado obtenido en la prueba teorica: "))
                        pruebapractica=int(input("ingrese el resultado obtenido en la prueba practica: "))
                        teoric=0.30*pruebateorica
                        practic=0.60*pruebapractica
                        promedio=teoric+practic
                        print("tuvo un promedio de ",promedio)
                        
                        if promedio >= 60:
                            riesgoNuevo="alto"
                            jsonn[3]["estudiantes"][estudiante-1]["riesgo"] = riesgoNuevo
                            print("el estudiante",i["nombre"],"tuvo un rendimiento alto en la ruta Netcore")
                            guardar_archivo("estudiantes.json", data)
                            print("")

                        elif promedio<= 59:
                                riesgoNuevo="bajo"
                                jsonn[3]["estudiantes"][estudiante-1]["riesgo"] = riesgoNuevo
                                guardar_archivo("estudiantes.json", data)
                                print("el estudiante",i["nombre"],"tuvo un rendimiento bajo en la ruta Netcore")
                                print("")
                            
        #opcion 3 del coordinador       
    if QueDesea=="3":
            print("===========================")
            print("    REPORTES DE CAMPERS    ")
            print("===========================")

            print("""Que reporte desea revisar
                          1.campers que se encuentran en estado inscrito
                          2.campers que aprobaron el examen inicial
                          3.entrenadores que se encuentran trabajando con campuslands
                          4campers que se encuentran con bajo rendimiento
                          5.campers y trainers que se encuentran a una ruta asociados a una ruta de entrenamiento
                          6.campers que perdieron y aprobaron cada uno de los modulos por su ruta de entrenamiento y entrenador encargado
                          """)
            listaDE=input("Que reporte desea revisar")

            if listaDE=="1":
                data = abrir_archivo("estudiantes.json")
                for i in jsonn[0]["postulados"]:
                 print("id:",i["id"])
                 print("nombre:",i["nombre"])
                 print("apellido:",i["apellido"])
                 print("estado",i["estado"])

            elif listaDE=="2":
                print("===========================================")
                print("  CAMPERS QUE APROBARON EL EXAMEN INICIAL  ")
                print("===========================================")
                data = abrir_archivo("estudiantes.json")

                for i in jsonn[0]["postulados"]:
                 print("id:",i["id"])
                 print("nombre:",i["nombre"])
                 print("apellido:",i["apellido"])
                 print("estado",i["estado"])
                
                #HACER UN FILTRO QUE ME MUESTRE SOLO LOS QUE APROBARON EL EXAMEN INICIAL
            elif listaDE=="3":
                print("============================================================")
                print("    TRAINER QUE SE ENCUENTRAN TRABAJANDO CON CAMPUSLANDS    ")
                print("============================================================")     
                print("")
                print("TRAINERS")
                print("Pedro")
                print("Jholver")
                print("uanca")
                print("iguel")

            elif listaDE=="4":
                print("======================================================")
                print("    CAMPERS QUE SE ENCUENTRAN CON RENDIMIENTO BAJO    ")
                print("======================================================")
                print("")
                print("""
                      1.M1
                      2.P1
                      3.T2
                      """)
                queGupoVer=input("en que grupo desea revisar")
                
                if queGupoVer=="1":
                    
                    for i in jsonn[1]["estudiantes"]:
                        data = abrir_archivo("estudiantes.json")
                        contador= contador+1
                        print("")
                        print("========================")
                        print("  CAMPERS DEL GRUPO T2  ")
                        print("========================")
                        print("id:",i["id"])
                        print("nombre:",i["nombre"])
                        print("apellido:",i["apellido"])
                        print("rendimiento:",i["riesgo"])
                        
                if queGupoVer=="2":
                    for i in jsonn[2]["estudiantes"]:
                        data = abrir_archivo("estudiantes.json")
                        contador= contador+1
                        print("")
                        print("========================")
                        print("  CAMPERS DEL GRUPO T2  ")
                        print("========================")
                        print("id:",i["id"])
                        print("nombre:",i["nombre"])
                        print("apellido:",i["apellido"])
                        print("rendimiento:",i["riesgo"])
                        
                if queGupoVer=="3":
                    for i in jsonn[3]["estudiantes"]:
                        data = abrir_archivo("estudiantes.json")
                        contador= contador+1
                        print("")
                        print("========================")
                        print("  CAMPERS DEL GRUPO T2  ")
                        print("========================")
                        print("id:",i["id"])
                        print("nombre:",i["nombre"])
                        print("apellido:",i["apellido"])
                        print("rendimiento:",i["riesgo"])

            elif listaDE=="5":
                data = abrir_archivo("estudiantes.json")
                print("============================================================")
                print("  CAMPERS Y TRAINERS ASOCIADOS A UNA RUTA DE ENTRENAMIENTO  ")
                print("============================================================")
                print("")
                print("""
                      1.java
                      2.nodejs
                      3. Netcore
                      """)
                queRutaVer=input("que ruta desea revisar: ")
                
                if queRutaVer=="1":
                    print("trainer encargado jholver")
                    
                    for i in jsonn[1]["estudiantes"]:
                        data = abrir_archivo("estudiantes.json")
                        contador= contador+1
                        print("")
                        print("===============")
                        print("   RUTA JAVA   ")
                        print("===============")
                        print("id:",i["id"])
                        print("nombre:",i["nombre"])
                        print("apellido:",i["apellido"])
                        print("cedula:",i["cedula"])
                        print("acudiente:",i["acudiente"])
                        print("direcccion:",i["direccion"])
                        print("estado:",i["estado"])
                        
                if queRutaVer=="2":
                    print("trainer encargado miguel")
                    
                    for i in jsonn[2]["estudiantes"]:
                        data = abrir_archivo("estudiantes.json")
                        contador= contador+1
                        print("")
                        print("===============")
                        print("  RUTA NODEJS  ")
                        print("===============")
                        print("id:",i["id"])
                        print("nombre:",i["nombre"])
                        print("apellido:",i["apellido"])
                        print("cedula:",i["cedula"])
                        print("acudiente:",i["acudiente"])
                        print("direcccion:",i["direccion"])
                        print("estado:",i["estado"])
                
                if queRutaVer=="3":
                    print("trainer encargado juanca")
                    for i in jsonn[3]["estudiantes"]:
                        
                        data = abrir_archivo("estudiantes.json")
                        contador= contador+1
                        print("")
                        print("================")
                        print("  RUTA NETcore  ")
                        print("================")
                        print("id:",i["id"])
                        print("nombre:",i["nombre"])
                        print("apellido:",i["apellido"])
                        print("cedula:",i["cedula"])
                        print("acudiente:",i["acudiente"])
                        print("direcccion:",i["direccion"])
                        print("estado:",i["estado"])
                
            elif listaDE=="6":
                print("==============================================================")
                print("   CAMPERS QUE APROBARON Y CAMPERS QUE DESAPROBARON MODULOS   ")
                print("==============================================================")
                print("")
                print("""
                      1.M1
                      2.P1
                      3.T2
                      """)
                queGupoVer=input("en que grupo desea revisar")
                
                if queGupoVer=="1":
                    
                    for i in jsonn[1]["estudiantes"]:
                        data = abrir_archivo("estudiantes.json")
                        contador= contador+1
                        print("")
                        print("============================")
                        print("   CAMPERS DEL GRUPO M1     ")
                        print("============================")
                        print("id:",i["id"])
                        print("nombre:",i["nombre"])
                        print("apellido:",i["apellido"])
                        print("estado:",i["estado"])
                        
                if queGupoVer=="2":
                    
                    for i in jsonn[2]["estudiantes"]:
                        data = abrir_archivo("estudiantes.json")
                        contador= contador+1
                        print("")
                        print("=========================")
                        print("   CAMPERS DEL GRUPO P1  ")
                        print("=========================")
                        print("id:",i["id"])
                        print("nombre:",i["nombre"])
                        print("apellido:",i["apellido"])
                        print("estado:",i["estado"])
                        
                if queGupoVer=="3":
                    
                    for i in jsonn[3]["estudiantes"]:
                        data = abrir_archivo("estudiantes.json")
                        contador= contador+1
                        print("")
                        print("==========================")
                        print("   CAMPERS DEL GRUPO T2   ")
                        print("==========================")
                        print("id:",i["id"])
                        print("nombre:",i["nombre"])
                        print("apellido:",i["apellido"])
                        print("estado:",i["estado"])
                    
    #el usuario ingreso como trainer
    if rol=="2":
        print("")
        print("¡Bienvenido, Trainer!")
        print("")
    
    # Menú de acciones del Trainer
        print("""¿Qué desea hacer?
          1. Subir notas de los Campers
          """)
    
    opcion=input("Ingrese el número de la acción que desea realizar: ")
    
    if opcion=="1":
        #salon
        cantidad_notas=int(input("¿Cuántas notas desea agregar? "))
        notas=[]
        
        #Almacenamiento de las notas que ingrese el trainer
        for i in range(cantidad_notas):
            nota = float(input(f"Ingrese la nota {i + 1}: "))
            notas.append(nota)
        
    else:
        print("seleccione una opción válida (1-3)")

#Proyecto Miguel Guerrero & Franco Guerrero C.C 1090381839 C.C 