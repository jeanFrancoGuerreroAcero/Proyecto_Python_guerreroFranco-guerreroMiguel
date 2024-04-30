import json
"""
def abrirArchivo():
    miJson=[]
    with open("json","r") as openfile:
        miJson= json.load(openfile)
        return miJson

def guardarDatos(miData):
    with open("json,""w") as outfile:
        json.dump(miData,outfile)
"""


print("bienvenido al departamento academico de campusland")
rol=input("que rol tienes dentro de campus :\n.trainer\n.camper\n.coordinador :")
booleano=True

##punto 3
while booleano:
    guardado=[100]
    if rol=="coordinador":
        ##abrirArchivo()
        idCamper=input("ingrese el ID del camper :")
        for i in guardado:
                notaCamper=int(input("que nota le registrara al camper"))
                if notaCamper >= 60:
                    print("el camper esta aprobado")
                else:
                    if notaCamper <60:
                        print("el camper reprobo")
                ##guardarDatos()
        print("hola")

        booleano=False



        
