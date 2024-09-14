# Documentación de la Aplicación de Dibujo con Turtle

Este código implementa una sencilla aplicación de dibujo en Python utilizando la biblioteca `turtle`. Los usuarios pueden dibujar diferentes formas geométricas, como líneas, cuadrados, círculos, rectángulos, triángulos y pentágonos, y seleccionar colores a través de comandos de teclado.

## Estructura del Código

### Importación de Módulos

```python
from turtle import *
from freegames import vector
```

- **`turtle`**: Biblioteca gráfica para dibujar formas.
- **`freegames.vector`**: Se utiliza para manejar las coordenadas (posiciones) en la pantalla.

### Funciones para Dibujar Formas

#### `line(start, end)`

```python
def line(start, end):
    """
    Dibuja una línea desde `start` hasta `end`.
    """
```

- **Descripción**: Dibuja una línea desde un punto inicial (`start`) hasta un punto final (`end`).

#### `square(start, end)`

```python
def square(start, end):
    """
    Dibuja un cuadrado. La distancia entre `start` y `end` define el tamaño del cuadrado.
    """
```

- **Descripción**: Dibuja un cuadrado basado en los puntos `start` y `end`, donde el tamaño del cuadrado es definido por la distancia entre ambos puntos.

#### `circle_shape(start, end)`

```python
def circle_shape(start, end):
    """
    Dibuja un círculo con centro en `start` y radio basado en la distancia entre `start` y `end`.
    """
```

- **Descripción**: Dibuja un círculo, donde el radio se calcula en función de la distancia entre los puntos `start` y `end`.

#### `rectangle(start, end)`

```python
def rectangle(start, end):
    """
    Dibuja un rectángulo con `start` como esquina superior izquierda.
    """
```

- **Descripción**: Dibuja un rectángulo, con la anchura y altura definidas por la distancia entre los puntos `start` y `end`.

#### `triangle(start, end)`

```python
def triangle(start, end):
    """
    Dibuja un triángulo equilátero basado en los puntos `start` y `end`.
    """
```

- **Descripción**: Dibuja un triángulo equilátero usando la distancia entre `start` y `end` para determinar el tamaño del triángulo.

#### `pentagon(start, end)`

```python
def pentagon(start, end):
    """
    Dibuja un pentágono regular. El tamaño se basa en la distancia entre los puntos `start` y `end`.
    """
```

- **Descripción**: Dibuja un pentágono regular, con cinco lados del mismo tamaño basado en la distancia entre `start` y `end`.

### Funciones para Manejo de Eventos

#### `tap(x, y)`

```python
def tap(x, y):
    """
    Maneja los clics en la pantalla. Guarda el punto inicial `start` y, cuando se hace clic nuevamente, dibuja la forma seleccionada.
    """
```

- **Descripción**: Registra la primera posición clicada como el punto de inicio. Cuando se hace clic una segunda vez, dibuja la forma seleccionada entre los puntos `start` y `end`.

#### `store(key, value)`

```python
def store(key, value):
    """
    Almacena un valor en el diccionario `state`. Se usa para cambiar la forma seleccionada.
    """
```

- **Descripción**: Almacena el estado del programa, como la forma actual seleccionada para dibujar.

### Estado Inicial del Programa

```python
state = {'start': None, 'shape': line}
```

- **`state`**: Diccionario que guarda el estado actual del programa. Contiene:
  - **`start`**: Coordenadas del primer clic.
  - **`shape`**: Función de dibujo seleccionada, inicialmente configurada para dibujar líneas.

### Configuración de la Pantalla

```python
setup(420, 420, 370, 0)
onscreenclick(tap)
listen()
```

- **`setup(420, 420, 370, 0)`**: Configura el tamaño y posición de la ventana gráfica.
- **`onscreenclick(tap)`**: Asocia la función `tap` para manejar los clics en la pantalla.
- **`listen()`**: Activa la escucha de eventos de teclado.

### Controles de Teclado

#### Deshacer Dibujos

```python
onkey(undo, 'u')
```

- **`u`**: Deshace el último dibujo realizado.

#### Selección de Colores

```python
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
onkey(lambda: color('yellow'), 'Y')
```

- **`K`**: Cambia el color de dibujo a negro.
- **`W`**: Cambia el color de dibujo a blanco.
- **`G`**: Cambia el color de dibujo a verde.
- **`B`**: Cambia el color de dibujo a azul.
- **`R`**: Cambia el color de dibujo a rojo.
- **`Y`**: Cambia el color de dibujo a amarillo.

#### Selección de Formas

```python
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circle_shape), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
onkey(lambda: store('shape', pentagon), 'p')
```

- **`l`**: Selecciona la función para dibujar líneas.
- **`s`**: Selecciona la función para dibujar cuadrados.
- **`c`**: Selecciona la función para dibujar círculos.
- **`r`**: Selecciona la función para dibujar rectángulos.
- **`t`**: Selecciona la función para dibujar triángulos.
- **`p`**: Selecciona la función para dibujar pentágonos.

### Iniciar el Programa

```python
done()
```

- **`done()`**: Finaliza la configuración de la ventana y mantiene el programa corriendo hasta que el usuario lo cierre.

---

¡Utiliza las teclas y el mouse para crear diferentes formas y cambiar los colores en tiempo real!
