import simpy
import random
import numpy as np
import statistics

RAM_TOTAL = 100
InstruccionesPorCiclo = 3
CantidadCPU = 1
InstruccionAzar = 0
EspacioAzar = 0
ID = 0
Intervalo = 10
generacion_Pro_Azar = 0
Tiempo_Fuera = 0.5
desviacion = []
media = []

class Proceso():
    def __init__(self, env, Cantidad_Instrucciones, Cantidad_Espacio,ID):
        self.env = env
        self.Cantidad_Instrucciones = InstruccionAzar
        self.Cantidad_Espacio = EspacioAzar
        self.ID = ID

        
    def prueba(self):
        yield self.env.timeout(generacion_Pro_Azar)
        print("")
        print("Tiempo inicial del proceso; "+str(self.env.now))
        print("Se ha creado un proceso con el id: "+str(ID))
        yield self.env.timeout(Tiempo_Fuera)
        print("Este proceso ocupa un espacio de: "+str(EspacioAzar))
        print("Este proceso tiene: "+str(InstruccionAzar)+" instrucciones")

def Iniciar(env, Pro,RAM):
    global times
    yield env.process(Pro.prueba())
    if Pro.Cantidad_Espacio < RAM:
        RAM = RAM - Pro.Cantidad_Espacio
    yield env.timeout(Tiempo_Fuera)
    while (True):
        yield env.timeout(Tiempo_Fuera)
        Pro.Cantidad_Instrucciones = Pro.Cantidad_Instrucciones - InstruccionesPorCiclo
        yield env.timeout(Tiempo_Fuera)
        if Pro.Cantidad_Instrucciones <= 0:
            media.append(env.now)
            print("El proceso ha sido procesado con exito")
            print("Tiempo de salida: "+str(env.now))
            break
        




env = simpy.Environment()
for i in range(50):
    generacion_Pro_Azar = random.expovariate(1.0 / Intervalo)
    InstruccionAzar = random.randint(1,10)
    EspacioAzar = random.randint(1,10)
    Pro = Proceso(env,InstruccionAzar,EspacioAzar,ID)
    env.process(Iniciar(env,Pro,RAM_TOTAL))
    env.run()
    process_time = env.now - generacion_Pro_Azar
    desviacion.append(process_time)
    ID= ID+1
    


std_dev = np.std(desviacion)
print('\n')
print("La media de los tiempos de finalización es: ", statistics.mean(media))
print('\n')
print("Desviacion estandar de las corridas:", std_dev) 
print('\n')
