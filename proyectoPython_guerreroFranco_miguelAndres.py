import json

def abrirArchivo():
    jsonn=[]
    with open("estudiantes.json","r") as openfile:
        jsonn= json.load(openfile)
        return jsonn

def guardarDatos(miData):
    with open("estudiantes.json","w") as outfile:
        json.dump(miData,outfile)

postuIncritos=[]
postu=[]
contraCoordinador=["900"]
correoCoordinador=["stiven@gmail.com"]

jsonn=abrirArchivo()
for i in range (len(jsonn)):
    if(jsonn[i]["grupo"]=="T1"):
        postuIncritos.append(jsonn[i])

with open('aceptados.json',"w") as outfile:
    jsonn= json.dump(postuIncritos,outfile)

def abriraceptados():
    jsonn=[]
    with open("aceptados.json","r") as openfile:
        jsonn= json.load(openfile)
        return jsonn
    
def guardarAceptados(miData):
    with open("estudiantes.json","w") as outfile:
        json.dump(miData,outfile)

print("########################################################")
print("###BIENVENIDO AL DEPARTAMENTO ACADEMICO DE CAMPUSLAND###")
print("########################################################")
print("escriba en numero la opcion que desea escoger")
rol=input("que rol tienes dentro de campus :\n1.trainer\n2.camper\n3.coordinador :")
booleano=True

while booleano:
    contador=0
    jsonn=[]

    if rol=="3":
        jsonn=abrirArchivo()
        print("############################")
        print("###BIENVENIDO COORDINADOR###")
        print("############################")
        QueDesea=input("1.inscribir postulados\n2.ingresar nota a campers que finalizaron modulo\n3.ver lista de reportes\n4:regresar al menu de inicio \nque funcion va a realizar :")
        if QueDesea=="1":
            jsonn=abrirArchivo()
            for i in jsonn[0]["postulados"]:
                jsonn=abrirArchivo()
                contador= contador+1
                print("")
                print("###############")
                print("POSTULANTES QUE PRESENTARON LA PRUEBA DE INGRESO")
                print("###############")
                print("id:",i["id"])
                print("nombre:",i["nombre"])
                print("apellido:",i["apellido"])
                print("cedula:",i["cedula"])
                print("acudiente:",i["acudiente"])
                print("direcccion:",i["direccion"])
                print("estado:",i["estado"])
                print("")
                print("se le va a revisar la prueba a cada uno de los que postularon la prueba")
                estudiante=int(input("ingrese el id que identifica al postulado :"))
                
                print("valor prueba teorica=30%")
                print("valor prueba practica=60%")
                parteTeorica=int(input("que promedio saco el postulado en la prueba teorica :"))
                partePractica=int(input("que promedio saco el postulado en la prueba practica :"))
                prueba=parteTeorica+partePractica/2

                if prueba >=60:
                    ##asignacion de estado en el que esta el camper
                    nuevoEstado= "isncrito"
                    jsonn[0]["postulados"][estudiante-1]["estado"] = nuevoEstado
                    guardarDatos(jsonn)
                    print("")

                    ##asignacion de ruta del camper nuevo
                    print("ingrese la opcion en numero")
                    print("rutas \n1.nodeJs\n2.java\n3.Netcore")
                    opcioRuta=input("que ruta tendra el camper")
                    print("")
                    if opcioRuta=="2":
                        nuevaRuta= "java"
                        jsonn[0]["postulados"][estudiante-1]["ruta"] = nuevaRuta
                        guardarDatos(jsonn)
                        print("")
                    ##asignacion de trainer del camper
                        print("se le asigno la ruta al camper")
                        print("java")
                        nuevoEstado="cursando"
                        guardarDatos(jsonn)
                        trainerNuevo="jholver"
                        print("El trainer jholver es el encargado de la ruta java")
                        jsonn[0]["postulados"][estudiante-1]["trainer"] = trainerNuevo
                        guardarDatos(jsonn)
                        print("")

                        ##asignacion de fecha de inicio del camper
                        nuevaFechaIni="12-06-2024"
                        print("iniciara el curso el 12-06-2024")
                        jsonn[0]["postulados"][estudiante-1]["fechaIni"] = nuevaFechaIni
                        guardarDatos(jsonn)
                        print("")

                        ##fecha de finalizacion del camper
                        nuevafechaFin="30-06-2025"
                        print("Finalizara el curso el 30-06-2025")
                        jsonn[0]["postulados"][estudiante-1]["fechaFin"] = nuevafechaFin
                        guardarDatos(jsonn)
                        print("")

                        ##salon que se le asignara al camper
                        print("")
                        nuevoSalon="apolo"
                        print("estara en el salon apolo")
                        print("tendra clase de 6-10 de la manaña")
                        jsonn[0]["postulados"][estudiante-1]["salon"] = nuevoSalon
                        guardarDatos(jsonn)
                        nuevoGrupo="M1"
                        print("el camper estara en el grupo M1")
                        jsonn[0]["postulados"][estudiante-1]["grupo"] = nuevoGrupo
                        guardarDatos(jsonn)
                        nuevoOcupado="6-10"
                        jsonn[0]["postulados"][estudiante-1]["ocupado"] = nuevoOcupado
                        guardarDatos(jsonn)
                        print("el camper vera: \n*fundamentos de programacion\n*programacion web")
                        print("")
                        print("programacion formal")
                        print("bases de datos")
                        print("backend")
                        queModulo=input("que otro modulo vera el camper :")
                        jsonn[0]["postulados"][estudiante-1]["modulo"] = queModulo
                        guardarDatos(jsonn)

                    elif opcioRuta=="1":
                        nuevaRuta= "nodeJs"
                        jsonn[0]["postulados"][estudiante-1]["ruta"] = nuevaRuta
                        guardarDatos(jsonn)
                        print("")
                        ##asignacion de trainer del camper
                        print("se le asigno la ruta al camper")
                        print("nodeJs")
                        trainerNuevo="miguel"
                        print("El trainer miguel es el encargado de la ruta java")
                        jsonn[0]["postulados"][estudiante-1]["trainer"] = trainerNuevo
                        guardarDatos(jsonn)
                        print("")

                        ##asignacion de fecha de inicio del camper
                        nuevaFechaIni="18-07-2024"
                        print("iniciara el curso el 18-07-2024")
                        jsonn[0]["postulados"][estudiante-1]["fechaIni"] = nuevaFechaIni
                        guardarDatos(jsonn)
                        print("")

                        ##fecha de finalizacion del camper
                        nuevafechaFin="18-07-2025"
                        print("Finalizara el curso el 18-07-2025")
                        jsonn[0]["postulados"][estudiante-1]["fechaFin"] = nuevafechaFin
                        guardarDatos(jsonn)
                        print("")

                        ##salon que se le asignara al camper
                        print("")
                        nuevoSalon="sputnik"
                        print("estara en el salon sputnik")
                        print("tendra clase de 11-3 de la tarde")
                        jsonn[0]["postulados"][estudiante-1]["salon"] = nuevoSalon
                        guardarDatos(jsonn)
                        nuevoOcupado="11-3"
                        jsonn[0]["postulados"][estudiante-1]["ocupado"] = nuevoOcupado
                        guardarDatos(jsonn)
                        print("el camper vera: \n*fundamentos de programacion\n*programacion web")
                        print("")
                        print("programacion formal")
                        print("bases de datos")
                        print("backend")
                        queModulo=input("que otro modulo vera el camper :")
                        jsonn[0]["postulados"][estudiante-1]["modulo"] = queModulo
                        guardarDatos(jsonn)
                    
                    elif opcioRuta=="3":
                        nuevaRuta= "nodeJs"
                        jsonn[0]["postulados"][estudiante-1]["ruta"] = nuevaRuta
                        guardarDatos(jsonn)
                        print("")######################################################
                        ##asignacion de trainer del camper
                        print("se le asigno la ruta al camper")
                        print("nodeJs")
                        trainerNuevo="juanca"
                        print("El trainer juanca es el encargado de la ruta java")
                        jsonn[0]["postulados"][estudiante-1]["trainer"] = trainerNuevo
                        guardarDatos(jsonn)
                        print("")

                        ##asignacion de fecha de inicio del camper
                        nuevaFechaIni="20-08-2024"
                        print("iniciara el curso el 20-08-2024")
                        jsonn[0]["postulados"][estudiante-1]["fechaIni"] = nuevaFechaIni
                        guardarDatos(jsonn)
                        print("")

                        ##fecha de finalizacion del camper
                        nuevafechaFin="20-08-2025"
                        print("Finalizara el curso el 20-08-2025")
                        jsonn[0]["postulados"][estudiante-1]["fechaFin"] = nuevafechaFin
                        guardarDatos(jsonn)
                        print("")

                        ##salon que se le asignara al camper
                        print("")
                        nuevoSalon="artemis"
                        print("estara en el salon artemis")
                        print("tendra clase de 3-7 de la noche")
                        jsonn[0]["postulados"][estudiante-1]["salon"] = nuevoSalon
                        guardarDatos(jsonn)
                        nuevoOcupado="3-7"
                        jsonn[0]["postulados"][estudiante-1]["ocupado"] = nuevoOcupado
                        guardarDatos(jsonn)
                
                else:
                    print("")
                    print("el postulante no podra estar en campus")
                    break
            print("")
        if QueDesea=="2":
            jsonn=abrirArchivo()
            print("##################################")
            print("### INSCRIBIR NOTAS DE CAMPERS ###")
            print("##################################")
            print("")
            print("los grupos que finalizaron modulo son :")
            print("1.grupo M1")
            print("")
            print("ingrese la opcion enumerada")
            queGrupo=input("Ingrese 1 para actualizar rendimiento de campers de este salon :")

            if queGrupo=="1":
                print("###############################################################################")
                print("###se le va a actualizar el rendiminto a cada camper que esta en el grupo M1###")
                print("################################################################################")
                contador=0
                for i in jsonn[1]["estudiantes"]:
                    jsonn=abrirArchivo()
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
                        jsonn[1]["estudiantes"][estudiante-1]["riesgo"] = riesgoNuevo
                        print("el estudiante",i["nombre"],"tuvo un rendimiento alto en el modulo java")###cambiar
                        guardarDatos(jsonn)
                        print("")

                    elif promedio<= 59:
                            riesgoNuevo="bajo"
                            jsonn[1]["estudiantes"][estudiante-1]["riesgo"] = riesgoNuevo
                            guardarDatos(jsonn)
                            print("el estudiante",i["nombre"],"tuvo un rendimiento bajo en el modulo java")
                            print("")
        elif QueDesea=="3":
            print("###########################")
            print("### REPORTES DE CAMPERS ###")
            print("###########################")

            listaDE=input("Que reporte desea revisar\n1.campers que se encuentran en estado inscrito\n2.campers que aprobaron el examen inicial\n3.entrenadores que se encuentran trabajando con campuslands\n.4campers que se encuentran con bajo rendimiento\n5.campers y trainers que se encuentran a una ruta asociados a una ruta de entrenamiento\n6.campers que perdieron y aprobaron cada uno de los modulos por su ruta de entrenamiento y entrenador encargado")

            if listaDE=="1":
                print("################################################")
                print("lista de campers que estan esn estado inscritos")
                print("################################################")
                print("")
                print(postu)

            elif listaDE=="2":
                print("#########################")
                print("CAMPERS QUE APROBARON EL EXAMEN INICIAL")
                print("###########################")
                ##HACER UN FILTRO QUE ME MUESTRE SOLO LOS QUE APROBARON EL EXAMEN INICIAL
            
            elif listaDE=="3":
                print("################################################")
                print("TRAINER QUE SE ENCUENTRAN TRABAJANDO CON CAMPUSLANDS")
                print("########################################")     
                print("")
                print("TRAINERS")
                print("*pedro")
                print("*jholver")
                print("*juanca")
                print("*miguel")
            elif listaDE=="4":
                print("#######################")
                print("CAMPERS QUE SE ENCUENTRAN CON RENDIMIENTO BAJO")
                print("######################################")
                print("")

            elif listaDE=="5":
                print("#############################")
                print("CAMPERS Y TRAINERS ASOCIADOS A UNA RUTA DE ENTRENAMIENTO")
                print("#####################################")
                print("")
                for i in jsonn[0]["estudiantes"]:
                    print("RUTA JAVA")
                    print("jholver:",i["ruta"])
                    print("camper:",i["id"],"",["nombre"])
            elif listaDE=="6":
                print("#############################")
                print("CAMPERS QUE APROBARON Y CAMPERS QUE DESAPROBARON MODULOS")
                print("#####################################")
                print("")
                aprob=input("desea ver los campers que aprobraron un modulo en especifico o campers que que reprobaron un modulo en especifico")
                if aprob=="aprobaron":
                    print("que modulo desea revisar")
                    print("java")
                    print("")

    if rol=="trainer":
      print("bienvenido trainer")
      print("")
      


