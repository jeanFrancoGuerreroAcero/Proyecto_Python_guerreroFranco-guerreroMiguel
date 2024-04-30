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
print("escribe en palabra")
rol=input("que rol tienes dentro de campus :\n1.trainer\n2.camper\n3.coordinador\n4.supervisor :")
print("###############")
booleano=True

##punto 3
while booleano:
    contador=0
    jsonn=[]

    if rol=="coordinador":
        jsonn=abrirArchivo()

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
            print("salon",i["salon"])
            print("")
            print("se le va a revisar la prueba a cada uno de los que postularon la prueba")
            estudiante=int(input("a que estudiante le vas a revisar la prueba :"))

            prueba= input("el estudiante aprobo la prueba de ingreso :")
            if prueba=="aprobo":
              ##asignacion de estado en el que esta el camper
              nuevoEstado= input("En que estado estara el estudiante :")
              jsonn[0]["estudiantes"][estudiante-1]["estado"] = nuevoEstado
              guardarDatos(jsonn)

              ##asignacion de ruta del camper nuevo
              print("rutas \nnodeJs\njava\nNetcore")
              nuevaRuta= input("Que ruta tendra el camper :")
              jsonn[0]["estudiantes"][estudiante-1]["ruta"] = nuevaRuta
              guardarDatos(jsonn)

              ##asignacion de trainer del camper
              print("se le asigno la ruta al camper")
              trainerNuevo=input("que trainer le asignara al camper :")
              jsonn[0]["estudiantes"][estudiante-1]["trainer"] = trainerNuevo
              guardarDatos(jsonn)

              ##asignacion de fecha de inicio del camper
              nuevaFechaIni=input("En que fecha iniciara el periodo de curso del trainer :")
              jsonn[0]["estudiantes"][estudiante-1]["fechaIni"] = nuevaFechaIni
              guardarDatos(jsonn)

              ##fecha de finalizacion del camper
              nuevafechaFin=input("En que fecha finalizara el proceso el camper :")
              jsonn[0]["estudiantes"][estudiante-1]["fechaFin"] = nuevafechaFin
              guardarDatos(jsonn)

              ##salon que se le asignara al camper
              print("")
              print("los salones que estan disponobles son\n*apolo\n*artemis\n*sputnik")
              nuevoSalon=input("que salon se le asignara al camper :")
              jsonn[0]["estudiantes"][estudiante-1]["salon"] = nuevoSalon
              guardarDatos(jsonn)
            else:
                print("el postulante no podra estar en campus")
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

