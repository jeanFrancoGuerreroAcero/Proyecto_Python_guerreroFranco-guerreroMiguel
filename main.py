import json

def abrirArchivo():
    jsonn=[]
    with open("PROYECTO\estudiantes.json","r") as openfile:
        jsonn= json.load(openfile)
        return jsonn

def guardarDatos(miData):
    with open("PROYECTO\estudiantes.json","w") as outfile:
        json.dump(miData,outfile)
        
#Bienvenida al usuario
print("========================================================")
print("   BIENVENIDO AL DEPARTAMENTO ACADEMICO DE CAMPUSLAND   ")
print("========================================================")
rol=input("""Que rol tienes dentro de campus: 
          
          1. Coordinador
          2. Trainer
          3. Camper 
          
          """)
booleano=True

while booleano:
    contador=0
    jsonn=[]
    
#Bienvenida del cordinador
    if rol=="1":
        jsonn=abrirArchivo()
        print("============================")
        print("   BIENVENIDO COORDINADOR   ")
        print("============================")
        QueDesea=input("""
                       que funcion vas a realizar: 
                       
                       1. Inscribir postulados
                       2. Ingresar nota a campers que finalizaron modulo 
                       3. Campers en peligro
                       
                       """)
        
        if QueDesea=="1":
            for i in jsonn[0]["estudiantes"]:
                jsonn=abrirArchivo()
                contador= contador+1
                print("")
                print("================================================")
                print("POSTULANTES QUE PRESENTARON LA PRUEBA DE INGRESO")
                print("================================================")
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
                    #asignacion de estado en el que esta el camper
                    nuevoEstado= input("En que estado estara el estudiante :")
                    jsonn[0]["estudiantes"][estudiante-1]["estado"] = nuevoEstado
                    guardarDatos(jsonn)
                    print("")

                    #asignacion de ruta del camper nuevo
                    print("rutas \nnodeJs\njava\nNetcore")
                    nuevaRuta= input("Que ruta tendra el camper :")
                    jsonn[0]["estudiantes"][estudiante-1]["ruta"] = nuevaRuta
                    guardarDatos(jsonn)
                    print("")

                    #asignacion de trainer del camper
                    print("se le asigno la ruta al camper")
                    trainerNuevo=input("que trainer le asignara al camper :")
                    jsonn[0]["estudiantes"][estudiante-1]["trainer"] = trainerNuevo
                    guardarDatos(jsonn)
                    print("")

                    #asignacion de fecha de inicio del camper
                    nuevaFechaIni=input("En que fecha iniciara el periodo de curso del trainer :")
                    jsonn[0]["estudiantes"][estudiante-1]["fechaIni"] = nuevaFechaIni
                    guardarDatos(jsonn)
                    print("")

                    #fecha de finalizacion del camper
                    nuevafechaFin=input("En que fecha finalizara el proceso el camper :")
                    jsonn[0]["estudiantes"][estudiante-1]["fechaFin"] = nuevafechaFin
                    guardarDatos(jsonn)
                    print("")

                    #salon que se le asignara al camper
                    print("")
                    print("los salones que estan disponobles son\n*apolo\n*artemis\n*sputnik")
                    nuevoSalon=input("que salon se le asignara al camper :")
                    jsonn[0]["estudiantes"][estudiante-1]["salon"] = nuevoSalon
                    guardarDatos(jsonn)
                else:
                    print("")
                    print("El postulante, no fue apto para asistir a Campuslads ")
                    break
            print("")
            
        if QueDesea=="2":
            jsonn=abrirArchivo()
            print("==================================")
            print("    INSCRIBIR NOTAS DE CAMPERS    ")
            print("==================================")
            print("")
            print("los grupos que finalizaron modulo son: ")
            print("""
                1. Grupo M1
                2. Grupo P1
                3. Grupo T1
                4. Grupo T2
                  """)
            print("Ingresa la opcion en numero (1-3)")
            queGrupo=input("A que grupo le va a revisar el rendimiento: ")

            if queGrupo=="1":
                print("===============================================================================")
                print("   se le va a actualizar el rendiminto a cada camper que esta en el grupo M1   ")
                print("===============================================================================")
                contador=0
                for i in jsonn[1]["estudiantes"]:
                    jsonn=abrirArchivo()
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
                    print("ruta ",i["ruta"])
                    print("trainer ",i["trainer"])
                    print("")
                    
                    print("se le va a revisar la prueba a cada uno de los que postularon la prueba")
                    estudiante=int((input("ingrese el id que identifica al camper: ")))
                    riesgoNuevo=input("que promedio tuvo el camper\n*alto\n*bajo\n: ")

                    if riesgoNuevo=="alto":
                        jsonn[1]["Estudiantes"][estudiante-1]["riesgo"] = riesgoNuevo
                        print("El estudiante",i["nombre"],"tuvo un rendimiento alto en el modulo ",i["ruta"])
                        guardarDatos(jsonn)
                        print("")
                    if riesgoNuevo=="bajo":
                        jsonn[1]["estudiantes"][estudiante-1]["riesgo"] = riesgoNuevo
                        guardarDatos(jsonn)
                        print("el estudiante",i["nombre"],"tuvo un rendimiento bajo en el modulo ",i["ruta"])
                        print("")
                        
            if queGrupo=="2":
                print("===============================================================================")
                print("   se le va a actualizar el rendiminto a cada camper que esta en el grupo P1   ")
                print("===============================================================================")
                contador=0
                for i in jsonn[1]["estudiantes"]:
                    jsonn=abrirArchivo()
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
                    print("ruta ",i["ruta"])
                    print("trainer ",i["trainer"])
                    print("")
                    
                    print("se le va a revisar la prueba a cada uno de los que postularon la prueba")
                    estudiante=int((input("ingrese el id que identifica al camper: ")))
                    riesgoNuevo=input("que promedio tuvo el camper\n*alto\n*bajo\n: ")

                    if riesgoNuevo=="alto":
                        jsonn[1]["Estudiantes"][estudiante-1]["riesgo"] = riesgoNuevo
                        print("El estudiante",i["nombre"],"tuvo un rendimiento alto en el modulo ",i["ruta"])
                        guardarDatos(jsonn)
                        print("")
                    if riesgoNuevo=="bajo":
                        jsonn[1]["estudiantes"][estudiante-1]["riesgo"] = riesgoNuevo
                        guardarDatos(jsonn)
                        print("el estudiante",i["nombre"],"tuvo un rendimiento bajo en el modulo ",i["ruta"])
                        print("")
                        
            if queGrupo=="3":
                print("===============================================================================")
                print("   se le va a actualizar el rendiminto a cada camper que esta en el grupo T1   ")
                print("===============================================================================")
                contador=0
                for i in jsonn[1]["estudiantes"]:
                    jsonn=abrirArchivo()
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
                    print("ruta ",i["ruta"])
                    print("trainer ",i["trainer"])
                    print("")
                    
                    print("se le va a revisar la prueba a cada uno de los que postularon la prueba")
                    estudiante=int((input("ingrese el id que identifica al camper: ")))
                    riesgoNuevo=input("que promedio tuvo el camper\n*alto\n*bajo\n: ")

                    if riesgoNuevo=="alto":
                        jsonn[1]["Estudiantes"][estudiante-1]["riesgo"] = riesgoNuevo
                        print("El estudiante",i["nombre"],"tuvo un rendimiento alto en el modulo ",i["ruta"])
                        guardarDatos(jsonn)
                        print("")
                        
                    if riesgoNuevo=="bajo":
                        jsonn[1]["estudiantes"][estudiante-1]["riesgo"] = riesgoNuevo
                        guardarDatos(jsonn)
                        print("el estudiante",i["nombre"],"tuvo un rendimiento bajo en el modulo ",i["ruta"])
                        print("")
            
            if queGrupo=="4":
                print("===============================================================================")
                print("   se le va a actualizar el rendiminto a cada camper que esta en el grupo T2   ")
                print("===============================================================================")
                
                contador=0
                for i in jsonn[1]["estudiantes"]:
                    jsonn=abrirArchivo()
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
                    print("ruta ",i["ruta"])
                    print("trainer ",i["trainer"])
                    print("")
                    
                    print("se le va a revisar la prueba a cada uno de los que postularon la prueba")
                    estudiante=int((input("ingrese el id que identifica al camper: ")))
                    riesgoNuevo=input("que promedio tuvo el camper\n*alto\n*bajo\n: ")

                    if riesgoNuevo=="alto":
                        jsonn[1]["Estudiantes"][estudiante-1]["riesgo"] = riesgoNuevo
                        print("El estudiante",i["nombre"],"tuvo un rendimiento alto en el modulo ",i["ruta"])
                        guardarDatos(jsonn)
                        print("")
                    if riesgoNuevo=="bajo":
                        jsonn[1]["estudiantes"][estudiante-1]["riesgo"] = riesgoNuevo
                        guardarDatos(jsonn)
                        print("el estudiante",i["nombre"],"tuvo un rendimiento bajo en el modulo ",i["ruta"])
                        print("") 
                        
                        
        if QueDesea=="3":
            print("Estos son los campers en riesgo ")
            
            if riesgoNuevo==0:
                print(f"Estas en riesgo alto",["estudiantes"])
            
            if riesgoNuevo==29:
                print(f"Estas en riesgo alto",["estudiantes"])
                
            if riesgoNuevo==30:
                print(f"estas en riesgo bajo",["estudiantes"])
                
            if riesgoNuevo==49:
                print(f"Estas en riesgo bajo",["estudiantes"])
                            
    if rol=="2":
      print("bienvenido trainer")






