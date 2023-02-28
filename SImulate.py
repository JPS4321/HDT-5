import simpy
import random as rand





class Sistema():
    def __init__(self,Cantidad_Ram,Cantidad_Instrucciones):
        self.Cantidad_Ram = Cantidad_Ram
        self.Cantidad_Instrucciones = Cantidad_Instrucciones
        
class Proceso:
    def __init__(self):
        self.Numero_Instrucciones = rand.randint(1,10)
        self.Espacio_Memoria = rand.randint(1,10)


def run(env,Procesos,Sistema):
    print("RAM incial: " + str(Sistema.Cantidad_Ram))
    while True:
        print("Ha llegado un nuevo proceso en " + str(env.now))
        ProcesoNuevo = Proceso()
        print("Cantidad de instrucciones: "+str(ProcesoNuevo.Numero_Instrucciones))
        print("Espacio a utilizar: "+str(ProcesoNuevo.Espacio_Memoria))
        print("Cantidad de Ram actual: "+str(Sistema.Cantidad_Ram))

        


hola = Sistema(100,10)
env = simpy.Environment()
env.process(run(env,10,hola))

        
#KOU
#Esteban 