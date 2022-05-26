import OpenGL.GL as gl
import glfw
import numpy as np
from Nave import Nave
from Shader import *
from Modelo import *
from Triangulo import Triangulo
from Rana import *
from Fondo import *
from Lineas import *
from Carros import *
from Carros2 import *
from Nube import *
from Decoracion import *

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 700

modelo = None
rana = None
fondo = None
window = None
lineas = None
carros = None
carros2 = None
nube = None
decoracion = None

tiempo_anterior = 0.0

carros = []
carros2 = []

valores_carros = [
    [0.3, -0.85, 0.0, 0.9, 2.0],
    [-0.8, -0.55, 0.0, 0.9, 2.0],
    [-0.3, -0.25, 0.0, 0.7, 2.0],
    [-0.6, -0.15, 0.0, 0.9, 2.0],
    [-0.2, -0.05, 0.0, 1.5, 2.0],
    [0.7, 0.25, 0.0, 0.4, 2.0], 
    [-0.4, 0.55, 0.0, 0.9, 2.0],
    [0.5, 0.75, 0.0, 0.5, 2.0], 
    [0.5, -0.85, 0.0, 0.4, 2.0], 
    [0.8, -0.55, 0.0, 0.5, 2.0], 
    [-0.2, -0.15, 0.0, 0.5, 2.0],
    [-0.5, -0.05, 0.0, 0.9, 2.0],
    [0.9, 0.05, 0.0, 0.3, 2.0],
    [0.7, 0.65, 0.0, 0.5, 2.0],
    [-0.3, 0.65, 0.0, 0.6, 2.0],
    [0.8, 0.75, 0.0, 0.5, 2.0]
]

valores_carros2 = [
    [0.8, -0.75, 0.0, 0.4, 3.0],
    [-0.4, -0.65, 0.0, 0.6, 3.0],
    [0.7, -0.45, 0.0, 0.5, 3.0],
    [-0.2, -0.55, 0.0, 1.0, 3.0],
    [0.5, 0.05, 0.0, 0.7, 3.0],
    [0.3, 0.15, 0.0, 0.9, 3.0],
    [0.9, 0.75, 0.0, 0.5, 3.0],
    [0.2, 0.45, 0.0, 0.8, 3.0],
    [0.2, 0.85, 0.0, 1.9, 3.0],
    [0.5, -0.75, 0.0, 0.6, 3.0],
    [-0.9, -0.65, 0.0, 1.4, 3.0],
    [0.9, -0.45, 0.0, 0.6, 3.0],
    [-0.8, -0.85, 0.0, 0.7, 3.0],
    [0.7, 0.15, 0.0, 0.8, 3.0],
    [0.2, 0.25, 0.0, 0.9, 3.0],
     [0.5, 0.45, 0.0, 0.8, 3.0],
    [-0.5, 0.55, 0.0, 0.9, 3.0],
    [0.1, 0.85, 0.0, 0.9, 3.0]
    ]

vertex_shader_source = ""
with open('vertex_shader.glsl') as archivo:
    vertex_shader_source = archivo.readlines()

fragment_shader_source = ""
with open('fragment_shader.glsl') as archivo:
    fragment_shader_source = archivo.readlines()

def inicializar_carros(shader, 
            posicion_id, color_id, transformaciones_id):
    for i in range (16):
        posicion_x=valores_carros[i][0]
        posicion_y=valores_carros[i][1]
        posicion_z=valores_carros[i][2]
        velocidad=valores_carros[i][3]
        direccion=valores_carros[i][4]
        #print(posicion_x, posicion_y, posicion_z, velocidad, direccion)
        carros.append(Carros(shader,posicion_id, color_id, transformaciones_id, posicion_x, posicion_y, posicion_z, velocidad, direccion))
    
def inicializar_carros2(shader, 
            posicion_id, color_id, transformaciones_id):
    for i in range (18):
        posicion_x=valores_carros2[i][0]
        posicion_y=valores_carros2[i][1]
        posicion_z=valores_carros2[i][2]
        velocidad=valores_carros2[i][3]
        direccion=valores_carros2[i][4]
        #print(posicion_x, posicion_y, posicion_z, velocidad, direccion)
        carros2.append(Carros2(shader,posicion_id, color_id, transformaciones_id, posicion_x, posicion_y, posicion_z, velocidad, direccion))

def actualizar():
    global window
    global tiempo_anterior
    tiempo_actual = glfw.get_time()
    tiempo_delta = tiempo_actual - tiempo_anterior

    for carro in carros:
        carro.actualizar(tiempo_delta)
        if carro.colisionando(rana):
            glfw.set_window_should_close(window, 1)
    for carro2 in carros2:
        carro2.actualizar(tiempo_delta)
        if carro2.colisionando(rana):
            glfw.set_window_should_close(window, 1)
    #rana.actualizar(window)
    nube.actualizar(tiempo_delta)
    tiempo_anterior = tiempo_actual

    


def dibujar():
    global modelo
    global rana
    global fondo
    global lineas
    global carros
    global carros2
    global nube
    global decoracion
    #modelo.dibujar()
    fondo.dibujar()
    lineas.dibujar()
    #carros.dibujar()
    for carro in carros:
        carro.dibujar()
    for carro2 in carros2:
        carro2.dibujar()
    decoracion.dibujar()
    rana.dibujar()
    nube.dibujar()

    

def main():
    global modelo
    global window
    global rana
    global fondo
    global lineas
    global carros
    global carros2
    global nube
    global decoracion
    glfw.init()

    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR,3)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR,3)
    glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)

    glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, gl.GL_TRUE)

    window = glfw.create_window(SCREEN_WIDTH, SCREEN_HEIGHT, 
        "Plantilla Shaders",None,None)
    if window is None:
        glfw.terminate()
        raise Exception("No se pudo crear ventana")
    
    glfw.make_context_current(window)
    glfw.set_framebuffer_size_callback(window, framebuffer_size_callbak)

   
    shader = Shader(vertex_shader_source, fragment_shader_source)

    posicion_id = gl.glGetAttribLocation(shader.shader_program, "position")
    color_id = gl.glGetAttribLocation(shader.shader_program, "color")
    
    transformaciones_id = gl.glGetUniformLocation(
            shader.shader_program, "transformations")
    
    modelo = Triangulo(shader, 
            posicion_id, color_id, transformaciones_id)

    rana = Rana(shader, 
        posicion_id, color_id, transformaciones_id)

    fondo = Fondo(shader, 
        posicion_id, color_id, transformaciones_id)

    lineas = Lineas(shader,
            posicion_id, color_id, transformaciones_id)
    
    nube = Nube(shader,
            posicion_id, color_id, transformaciones_id)
    
    decoracion = Decoracion(shader,
            posicion_id, color_id, transformaciones_id)
    
    # carros = Carros(shader,
    #         posicion_id, color_id, transformaciones_id)

    inicializar_carros(shader,
            posicion_id, color_id, transformaciones_id)
    inicializar_carros2(shader,
            posicion_id, color_id, transformaciones_id)

    glfw.set_key_callback(window, rana.actualizar)
    #draw loop
    while not glfw.window_should_close(window):
        gl.glClearColor(0.3,0.3,0.3,1.0)
        gl.glClear(gl.GL_COLOR_BUFFER_BIT)

        #dibujar
        dibujar()
        actualizar()

        glfw.swap_buffers(window)
        glfw.poll_events()

    #Liberar memoria
    #modelo.borrar()
    shader.borrar()
    fondo.borrar()
    decoracion.borrar()
    rana.borrar()
    lineas.borrar()
    carros.borrar()
    carros2.borrar()
    


    glfw.terminate()
    return 0

def framebuffer_size_callbak(window, width, height):
    gl.glViewport(0,0,width,height)


if __name__ == '__main__':
    main()

