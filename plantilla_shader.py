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

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 700

modelo = None
rana = None
fondo = None
window = None
lineas = None
carros = None

vertex_shader_source = ""
with open('vertex_shader.glsl') as archivo:
    vertex_shader_source = archivo.readlines()

fragment_shader_source = ""
with open('fragment_shader.glsl') as archivo:
    fragment_shader_source = archivo.readlines()

def actualizar():
    global window
    #rana.actualizar(window)


def dibujar():
    global modelo
    global rana
    global fondo
    global lineas
    global carros
    #modelo.dibujar()
    fondo.dibujar()
    lineas.dibujar()
    carros.dibujar()
    rana.dibujar()
    

def main():
    global modelo
    global window
    global rana
    global fondo
    global lineas
    global carros
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
    
    carros = Carros(shader,
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
    modelo.borrar()
    shader.borrar()
    fondo.borrar()
    rana.borrar()
    lineas.borrar()
    carros.borrar()
    


    glfw.terminate()
    return 0

def framebuffer_size_callbak(window, width, height):
    gl.glViewport(0,0,width,height)


if __name__ == '__main__':
    main()

