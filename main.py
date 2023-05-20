import random as rd


class TrashCity:

    def __init__(self):
        self.Conductores = []
        self.Asistentes = []
        self.Rutas = []
        self.Camiones = []
        self.totalVidrio = 0

    def agregarCamiones(self, Camion):

        for i in self.Camiones:
            if i.id == Camion.id:
                print("El camion ya ha sido ingresado")
                return
        self.Camiones.append(Camion)

    def agregarConductores(self, Personal):
        print(self.Conductores)
        for i in self.Conductores:
            if i.id == Personal.id:
                return print("Este conductor ya ha sido ingresado")
        self.Conductores.append(Personal)
        print(self.Conductores)

    def agregarAsistentes(self, Personal):
        for i in self.Asistentes:
            if i.id == Personal.id:
                print("Este asistente ya ha sido ingresado")
                return
        self.Asistentes.append(Personal)

    def calcularVidrio(self, Turno, vidrio : int):
        totalV = vidrio
        self.totalVidrio += totalV
        return self.totalVidrio
class Personal:
    def __init__(self, nombre, id):
        self.nombre = nombre
        self.id = id

class Camion:
    def __init__(self, id):
        self.id = id

class puntosGeograficos:
    def __init__(self, latitud, longitud):
        self.latitud = latitud
        self.longitud = longitud

    def __repr__(self):
        return f'({self.latitud}, {self.longitud})'
class Rutas:
    def __init__(self):
        self.rutas = []
    def agregarPuntosGeograficos(self, latitud, longitud):
        for i in self.rutas:
            if i.latitud == latitud and i.longitud == longitud:
                print("El punto ya ha sido agregado")
                return
        self.rutas.append(puntosGeograficos(latitud, longitud))

    def __iter__(self):
        return RutasIterator(self.rutas)
class RutasIterator:
    def __init__(self, rutas):
        self.rutas = rutas
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.rutas):
            punto = self.rutas[self.index]
            self.index += 1
            return punto
        else:
            raise StopIteration

class Turno:
    def __init__(self, idCamion: int, idConductor: int, idAsistente1: int, idAsistente2: int):
        generarRuta = ()
    def generarRuta(self, rutas):
        ruta = []
        rutas_iterator = iter(rutas)
        for i in range(0, 2):
            temp = next(rutas_iterator)
            if temp.latitud != ruta[0].latitud or temp.longitud != ruta[0].longitud:
                ruta.append(temp)
        return ruta


Empresa = TrashCity()
turnosCreados = 0
VidrioTotal = 0
while True:
    print("¿Que desea hacer?")
    print("1. Ingresar Asistentes/Conductores")
    print("2. Ingresar Camiones")
    print("3. Agregar puntos geograficos")
    print("4. Comenzar un turno")
    print("5. Finalizar dia y mostrar total de residuos de vidrio")
    o = int(input("Digita tu opción: "))

    if o == 1:
        print("¿Que deseas agregar?")
        print("1. Asistentes")
        print("2. Conductores")
        f = int(input("Digita tu opción: "))

        if f == 1:
            nombre = input("Digita el nombre del Asistente: ")
            id = int(input("Digita el id del Asistente: "))
            Empresa.agregarAsistentes(nombre, id)
        elif f == 2:
            nombre = input("Digita el nombre del Conductor: ")
            id = int(input("Digita el id del Conductor: "))
            Empresa.agregarConductores(nombre, id)
    elif o == 2:
        id = int(input("Digite el id del camión: "))
        Empresa.agregarCamiones(id)
    elif o == 3:
        latitud = int(input("Digita la latitud: "))
        longitud = int(input("Digita la longitud: "))
        punto = puntosGeograficos(latitud, longitud)
        rutas = Rutas()
        rutas.agregarPuntosGeograficos(latitud, longitud)
        pass
    elif o == 4 and turnosCreados <= 5:
        turnosCreados += 1
        idCamion = int(input("Digita la id del camión: "))
        idConductor = int(input("Digita la id del conductor: "))
        idAsistente1 = int(input("Digita la id del asistente 1: "))
        idAsistente2 = int(input("Digita la id del asistente 2: "))
        Turno = Turno(idCamion, idConductor, idAsistente1, idAsistente2)
        while True:
            f = int(input("Digiste 1 para finalizar el turno: "))
            if f == 1:
                vidrio = int(input("Digita la cantidad de vidrios: "))
                papel = int(input("Digite la cantidad de papel: "))
                plástico = int(input("Digita la cantidad plastico: "))
                metal = int(input("Digita la cantidad de metal: "))
                rOrganicos = int(input("Digita la cantidad de residuos organicos: "))
                VidrioTotal += Empresa.calcularVidrio(Turno, vidrio)
                break
            elif f > 1 or f < 1:
                print("Opcion invalida o los turnos agregados superan el limite")

    elif o == 5:
        print(VidrioTotal)
        break
    elif o > 5 or o < 1:
        print("Opción invalida")