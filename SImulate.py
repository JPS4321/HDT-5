import simpy
import random as rand

Cantidad_Procesos = 25
Intervalos = 10
Solicitud_Memoria = rand.expovariate(1.0/Intervalos)
Cantidad_Memoria_RAM = 100
Capacidad = 1


class Computadora:
    def __init__(self, env, Cantidad_Procesos, Intervalos, Cantidad_Memoria_RAM, Capacidad):
        self.env = env
        self.Cantidad_Procesos = Cantidad_Procesos
        self.Intervalos = Intervalos
        self.Cantidad_Memoria_RAM = Cantidad_Memoria_RAM
        self.Capacidad = simpy.Resource(env,Capacidad)