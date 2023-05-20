# Parcial2
Diego Angarita - Parcial POO #2
# TrashCity

El código proporcionado representa la implementación de la clase `TrashCity` y otras clases relacionadas que modelan un sistema de gestión de una ciudad para la recolección de basura. A continuación se presenta una descripción detallada de cada clase y sus funcionalidades.

## Clase `TrashCity`

La clase `TrashCity` representa la ciudad de recolección de basura. Tiene los siguientes atributos:

- `Conductores`: una lista que almacena los conductores disponibles en la ciudad.
- `Asistentes`: una lista que almacena los asistentes disponibles en la ciudad.
- `Rutas`: una lista que almacena las rutas disponibles en la ciudad.
- `Camiones`: una lista que almacena los camiones disponibles en la ciudad.
- `totalVidrio`: un entero que representa la cantidad total de vidrio recolectado.

La clase `TrashCity` tiene los siguientes métodos:

- `agregarCamiones(Camion)`: agrega un objeto de la clase `Camion` a la lista de camiones de la ciudad. Verifica si el camión ya ha sido ingresado previamente.
- `agregarConductores(Personal)`: agrega un objeto de la clase `Personal` a la lista de conductores de la ciudad. Verifica si el conductor ya ha sido ingresado previamente.
- `agregarAsistentes(Personal)`: agrega un objeto de la clase `Personal` a la lista de asistentes de la ciudad. Verifica si el asistente ya ha sido ingresado previamente.
- `calcularVidrio(Turno, vidrio: int)`: calcula la cantidad total de vidrio recolectado en la ciudad. Recibe un objeto de la clase `Turno` y la cantidad de vidrio recolectado en ese turno. Actualiza el atributo `totalVidrio` y devuelve el nuevo valor.

## Clase `Personal`

La clase `Personal` representa al personal involucrado en la recolección de basura. Tiene los siguientes atributos:

- `nombre`: una cadena que representa el nombre del personal.
- `id`: un entero que representa el identificador del personal.

## Clase `Camion`

La clase `Camion` representa un camión utilizado en la recolección de basura. Tiene un único atributo:

- `id`: un entero que representa el identificador del camión.

## Clase `puntosGeograficos`

La clase `puntosGeograficos` representa un punto geográfico en términos de latitud y longitud. Tiene los siguientes atributos:

- `latitud`: un valor numérico que representa la latitud del punto.
- `longitud`: un valor numérico que representa la longitud del punto.

La clase también define un método especial `__repr__()` que devuelve una representación legible del punto geográfico.

## Clase `Rutas`

La clase `Rutas` representa las rutas de recolección en la ciudad. Tiene un único atributo:

- `rutas`: una lista que almacena los puntos geográficos que forman parte de la ruta.

La clase `Rutas` proporciona los siguientes métodos:

- `agregarPuntosGeograficos(latitud, longitud)`: agrega un punto geográfico a la lista de rutas. Verifica si el punto ya ha sido agregado previamente.
- `__iter__()`: devuelve un iterador para iterar sobre los puntos geográficos de la

 ruta.

## Clase `RutasIterator`

La clase `RutasIterator` es un iterador personalizado para la clase `Rutas`. Itera sobre los puntos geográficos de la ruta. Tiene los siguientes atributos:

- `rutas`: una lista de puntos geográficos.
- `index`: un entero que indica la posición actual del iterador.

La clase `RutasIterator` proporciona los siguientes métodos:

- `__iter__()`: devuelve el propio iterador.
- `__next__()`: devuelve el siguiente punto geográfico en la ruta. Si no hay más puntos, se lanza una excepción `StopIteration`.

## Clase `Turno`

La clase `Turno` representa un turno de recolección de basura. Tiene los siguientes atributos:

- `idCamion`: un entero que representa el identificador del camión asignado al turno.
- `idConductor`: un entero que representa el identificador del conductor asignado al turno.
- `idAsistente1`: un entero que representa el identificador del primer asistente asignado al turno.
- `idAsistente2`: un entero que representa el identificador del segundo asistente asignado al turno.

La clase `Turno` proporciona el método `generarRuta(rutas)` para generar una ruta basada en una lista de puntos geográficos. El método devuelve una lista de puntos geográficos que forman la ruta del turno.
