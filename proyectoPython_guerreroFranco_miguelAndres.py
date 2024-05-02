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

with open('estudiantes.json', encoding= "utf-8") as openfile:
    jsonn= json.load(openfile)

for i in range (len(jsonn)):
    if(jsonn[i]["grupo"]=="postulados"):
        postuIncritos.append(jsonn[i])


with open('aceptados.json', encoding= "utf-8") as openfile:
    jsonn= json.load(openfile)

for i in range (len(jsonn)):
    if(jsonn[i]["estudiantes"]=="estado"):
        postu.append(jsonn[i])

with open("inscritos.json","w") as outfile:
    json.dump(postu,outfile)


print("########################################################")
print("###BIENVENIDO AL DEPARTAMENTO ACADEMICO DE CAMPUSLAND###")
print("########################################################")
print("escriba en numero la opcion que desea escoger")
rol=input("que rol tienes dentro de campus :\n1.trainer\n2.camper\n3.coordinador :")
booleano=True

##punto 3
while booleano:
    contador=0
    jsonn=[]

    if rol=="3":
        jsonn=abrirArchivo()
        print("############################")
        print("###BIENVENIDO COORDINADOR###")
        print("############################")
        QueDesea=input("1.inscribir postulados\n2.ingresar nota a campers que finalizaron modulo\n3.ver lista de reportes\nque funcion va a realizar :")
        if QueDesea=="1":
            for i in jsonn[0]["estudiantes"]:
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
                print("ruta :",i["ruta"])
                print("trainer:",i["trainer"])
                print("")
                print("se le va a revisar la prueba a cada uno de los que postularon la prueba")
                estudiante=int(input("ingrese el id que identifica al postulado :"))

                parteTeorica=int(input("que promedio saco el postulado en la prueba teorica :"))
                partePractica=int(input("que promedio saco el postulado en la prueba practica :"))
                prueba=parteTeorica+partePractica/2

                if prueba >=60:
                    ##asignacion de estado en el que esta el camper
                    nuevoEstado= input("En que estado estara el estudiante :")
                    jsonn[0]["estudiantes"][estudiante-1]["estado"] = nuevoEstado
                    guardarDatos(jsonn)
                    print("")

                    ##asignacion de ruta del camper nuevo
                    print("rutas \nnodeJs\njava\nNetcore")
                    nuevaRuta= input("Que ruta tendra el camper :")
                    jsonn[0]["estudiantes"][estudiante-1]["ruta"] = nuevaRuta
                    guardarDatos(jsonn)
                    print("")

                    ##asignacion de trainer del camper
                    print("se le asigno la ruta al camper")
                    trainerNuevo=input("que trainer le asignara al camper :")
                    jsonn[0]["estudiantes"][estudiante-1]["trainer"] = trainerNuevo
                    guardarDatos(jsonn)
                    print("")

                    ##asignacion de fecha de inicio del camper
                    nuevaFechaIni=input("En que fecha iniciara el periodo de curso del trainer :")
                    jsonn[0]["estudiantes"][estudiante-1]["fechaIni"] = nuevaFechaIni
                    guardarDatos(jsonn)
                    print("")

                    ##fecha de finalizacion del camper
                    nuevafechaFin=input("En que fecha finalizara el proceso el camper :")
                    jsonn[0]["estudiantes"][estudiante-1]["fechaFin"] = nuevafechaFin
                    guardarDatos(jsonn)
                    print("")

                    ##salon que se le asignara al camper
                    print("")
                    print("los salones que estan disponobles son\n*apolo\n*artemis\n*sputnik")
                    nuevoSalon=input("que salon se le asignara al camper :")
                    jsonn[0]["estudiantes"][estudiante-1]["salon"] = nuevoSalon
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
            print("2.grupo t2")
            print("")
            print("ingrese la opcion enumerada")
            queGrupo=input("A que grupo le va a revisar el rendimiento :")

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
                        
    if rol=="trainer":
      print("bienvenido trainer")


      

""""
salones
    apolo
   trainer:pedro
   temas=intro,finalie
   rutas=java
   ocupado=10-2 - 6-10

"""

