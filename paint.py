from turtle import *
from freegames import vector

# Función para dibujar una línea
def line(start, end):
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)

# Función para dibujar un cuadrado
def square(start, end):
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for _ in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()

# Función para dibujar un círculo
def circle_shape(start, end):
    up()
    goto(start.x, start.y)
    down()
    begin_fill()
    radius = (end.x - start.x) / 2
    abs_radius = abs(radius)  # Ajuste para asegurar que el radio sea positivo
    circle(abs_radius)
    end_fill()

# Función para dibujar un rectángulo
def rectangle(start, end):
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for _ in range(2):
        forward(end.x - start.x)
        left(90)
        forward((end.x - start.x) / 2)
        left(90)

    end_fill()

# Función para dibujar un triángulo
def triangle(start, end):
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    forward(end.x - start.x)
    left(90)
    forward(end.x - start.x)
    left(135)
    forward(end.x - start.x)
    left(135)

    end_fill()

# Función para dibujar un pentágono
def pentagon(start, end):
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for _ in range(5):
        forward(end.x - start.x)
        left(72)

    end_fill()

# Función para manejar los clics de la pantalla
def tap(x, y):
    start_point = state['start']

    if start_point is None:
        state['start'] = vector(x, y)
    else:
        shape_func = state['shape']
        end_point = vector(x, y)
        shape_func(start_point, end_point)
        state['start'] = None

# Función para almacenar el estado
def store(key, value):
    state[key] = value

# Estado inicial del programa
state = {'start': None, 'shape': line}

# Configuración de la pantalla
setup(420, 420, 370, 0)
onscreenclick(tap)
listen()

# Configuración de los controles de teclado
onkey(undo, 'u')
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
onkey(lambda: color('yellow'), 'Y')

# Selección de formas
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circle_shape), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
onkey(lambda: store('shape', pentagon), 'p')

done()
