import json

def abrirArchivo():
    jsonn=[]
    with open("estudiantes.json","r") as openfile:
        jsonn= json.load(openfile)
        return jsonn

def guardarDatos(miData):
    with open("estudiantes.json","w") as outfile:
        json.dump(miData,outfile)

def abrirmodulo():
    miJsi=[]
    with open("modulos.json","r") as openfile:
        miJsi= json.load(openfile)
        return miJsi
    
def guardarModulo(miData):
    with open("modulos.json","w") as outfile:
        json.dump(miData,outfile)

print("##############")
print("bienvenido al departamento academico de campusland")
print("escriba en numero la opcion que desea escoger")
rol=input("que rol tienes dentro de campus :\n1.trainer\n2.camper\n3.coordinador :")
print("###############")
booleano=True

##punto 3
while booleano:
    contador=0
    jsonn=[]

    if rol=="3":
        jsonn=abrirArchivo()
        print("bienvenido coordinador")
        QueDesea=input("1.inscribir postulados\n2.ingresar nota a campers que finalizaron modulo\nque funcion va a realizar ")
        if QueDesea=="1":
            for i in jsonn[0]["estudiantes"]:
                contador= contador+1
                print("")
                print("###############")
                print("ESTUDIANTES QUE PRESENTARON LA PRUEBA DE INGRESO")
                print("###############")
                print("id",i["id"])
                print("nombre",i["nombre"])
                print("apellido",i["apellido"])
                print("cedula",i["cedula"])
                print("acudiente",i["acudiente"])
                print("direcccion",i["direccion"])
                print("estado",i["estado"])
                print("ruta ",i["ruta"])
                print("trainer ",i["trainer"])
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
            print("#######################################")
            print("######inscribir notas de campers#######")
            print("#######################################")
            print("")
            print("los grupos que terminaro modulo son :")
            print("1.grupo M1")
            print("2.grupo t2")
            print("")
            print("ingrese la opcion enumerada")
            queGrupo=input("A que grupo le va a revisar el rendimiento :")

            if queGrupo=="1":
                abrirArchivo(jsonn)
                print("se le va a actualizar el rendiminto a cada camper que esta en el grupo M1")
                contador=0
                for i in jsonn[1]["estudiantes"]:
                    contador= contador+1
                    print("")
                    print("###############")
                    print("ESTUDIANTES QUE PRESENTARON LA PRUEBA DE INGRESO")
                    print("###############")
                    print("id",i["id"])
                    print("nombre",i["nombre"])
                    print("apellido",i["apellido"])
                    print("cedula",i["cedula"])
                    print("acudiente",i["acudiente"])
                    print("direcccion",i["direccion"])
                    print("estado",i["estado"])
                    print("ruta ",i["ruta"])
                    print("trainer ",i["trainer"])
                    print("")
                    print("se le va a revisar la prueba a cada uno de los que postularon la prueba")
                    estudiante=int(input("ingrese el id que identifica al postulado :"))
                    riesgoNuevo=input("que promedio tuvo el camper\n*alto\n*bajo\n :")

                    if riesgoNuevo=="alto":
                        jsonn[0]["estudiantes"][estudiante-1]["riesgo"] = riesgoNuevo
                        print("el estudiante ",i["nombre"])
                        guardarDatos(jsonn)
                        print("")







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

