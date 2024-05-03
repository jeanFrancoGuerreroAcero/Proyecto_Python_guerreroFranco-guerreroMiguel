#PROYECTO\estudiantes.json => si se quiere ejecutar en cualquier equipo, se debe reemplazar esta parte del codigo por la ruta alternativa del archivo

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


aprobados=[]
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

    if rol=="1":
        jsonn=abrirArchivo()
        print("============================")
        print("   BIENVENIDO COORDINADOR   ")
        print("============================")
        
        QueDesea=input("""
    que funcion vas a realizar: 
                       
    1. Inscribir postulados
    2. Ingresar nota a campers que finalizaron modulo 
    3. lista de reportes
    """)

        if QueDesea=="1":
            
            for i in jsonn[0]["estudiantes"]:
                jsonn=abrirArchivo()
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
                print("")
                print("se le va a revisar la prueba a cada uno de los que postularon la prueba")
                estudiante=int(input("ingrese el id que identifica al postulado :"))


                parteTeorica=int(input("que promedio saco el postulado en la prueba teorica: "))
                partePractica=int(input("que promedio saco el postulado en la prueba practica: "))
                prueba=parteTeorica+partePractica/2

                if prueba >=60:
                    
                    ##asignacion de estado en el que esta el camper
                    nuevoEstado= "inscrito"
                    jsonn[0]["estudiantes"][estudiante-1]["estado"] = nuevoEstado
                    guardarDatos(jsonn)
                    print("")

                    ##asignacion de ruta del camper nuevo
                    print("rutas \nnodeJs\njava\nNetcore")
                    print("en el salon")
                    nuevaRuta= input("Que ruta tendra el camper :")
                    jsonn[0]["estudiantes"][estudiante-1]["ruta"] = nuevaRuta
                    guardarDatos(jsonn)
                    print("")

                    if nuevaRuta== "java":

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
                        nuevoSalon="apolo"
                        jsonn[0]["estudiantes"][estudiante-1]["salon"] = nuevoSalon
                        guardarDatos(jsonn)

                        print("")
                        nuevoModulo=input("Que modulo le asignara al camper")
                else:
                    nuevoEstado="eliminar"
                    print("El estudiante", i["nombre"], "tuvo un rendimiento bajo en el módulo java y será eliminado ")
                    jsonn=["eliminar"].pop(estudiante - 1)
                    guardarDatos(jsonn)
                    print("")
            
        if QueDesea=="2":
            jsonn=abrirArchivo()
            print("==================================")
            print("    INSCRIBIR NOTAS DE CAMPERS    ")
            print("==================================")
            
            print("los grupos que finalizaron modulo son :")
            print("1. Grupo M1")
            print("2. Grupo P1")
            print("3. Grupo T1")
            print("4. Grupo T2")
            
            print("ingrese la opcion enumerada")
            queGrupo=input("A que grupo le va a revisar el rendimiento :")

            if queGrupo=="1":
                print("===============================================================================")
                print("   se le va a actualizar el rendiminto a cada camper que esta en el grupo M1   ")
                print("===============================================================================")
                contador=0
                
                for i in jsonn[1]["estudiantes"]:
                    jsonn=abrirArchivo()
                    contador= contador+1
                    
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
                    print("======================================")
                    
                    print("se le revisara la prueba a cada uno de los postulados ")
                    estudiante=int((input("Ingrese el id del camper: ")))
                    pruebateorica=int(input("Ingrese el resultado obtenido en la prueba teorica: "))
                    pruebapractica=int(input("Ingrese el resultado obtenido en la prueba practica: "))
                    
                    teoric=0.30*pruebateorica
                    practic=0.60*pruebapractica
                    promedio=teoric+practic
                    print("Obtuvo un promedio de: ", promedio)

                    if promedio >= 60:
                        riesgoNuevo = "alto"
                        jsonn=["estudiantes"][estudiante - 1]["riesgo"] = riesgoNuevo
                        print("El estudiante", i["nombre"], "tuvo un rendimiento alto en el módulo java ")
                        guardarDatos(jsonn)
                        print("")
                        
                    else:
                        print("El estudiante", i["nombre"], "tuvo un rendimiento bajo en el módulo java y será eliminado ")
                        jsonn=["eliminar"].pop(estudiante - 1)
                        guardarDatos(jsonn)
                        print("")

        elif QueDesea=="3":
            print("==================================")
            print("       REPORTES DE CAMPERS        ")
            print("==================================")

            listaDE=input("""
                          Que reporte desea revisar
                          
                          1. Campers que se encuentran en estado inscrito
                          2. Campers que aprobaron el examen inicial
                          3. Entrenadores que se encuentran trabajando con campuslands
                          4. Campers que se encuentran con bajo rendimiento
                          5. Campers y trainers que se encuentran a una ruta asociados a una ruta de entrenamiento
                          6. Campers que perdieron y aprobaron cada uno de los modulos por su ruta de entrenamiento y entrenador encargado
                          """)

            if listaDE=="1":
                print("================================================")
                print(" lista de campers que estan en estado inscritos ")
                print("================================================")
                print("")
                print(postu)

            elif listaDE=="2":
                print("================================================")
                print("CAMPERS QUE APROBARON EL EXAMEN INICIAL")
                print("================================================")
                ##HACER UN FILTRO QUE ME MUESTRE SOLO LOS QUE APROBARON EL EXAMEN INICIAL
            
            elif listaDE=="3":
                print("================================================")
                print("TRAINER QUE SE ENCUENTRAN TRABAJANDO CON CAMPUSLANDS")
                print("================================================")     
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
            
    if rol=="2":
      print("bienvenido trainer")
