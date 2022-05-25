import math
from Modelo import *
import glm
import glfw

class Rana(Modelo):
    #x=0.37
    #y=-0.85
    x=0.0
    y=-0.95
    z=0.0
    velocidad = 0.1
    direccion = 0.0

    def __init__(self,shader, posicion_id, color_id, transformaciones_id):
        self.ARRIBA = 1
        self.ABAJO = 2
        self.IZQUIERDA = 3
        self.DERECHA = 4
        self.extremo_izquierdo = 0.05*0.5
        self.extremo_derecho = 0.05*0.5
        self.extremo_inferior = 0.04*0.5
        self.extremo_superior =0.04*0.5
        
        self.vertices = np.array(
            [
                #Rana cabeza
                (-0.76*0.5) + 0.37, (-0.11*0.5) + 0.1,0.0,1.0, 13/255,255/255,0/255,1.0,  #izquierda arriba
                (-0.76*0.5) + 0.37, (-0.15*0.5) + 0.1,0.0,1.0,    13/255,255/255,0/255,1.0,  #izquierda abajo
                (-0.80*0.5) + 0.37, (-0.11*0.5) + 0.1,0.0,1.0,     13/255,255/255,0/255,1.0, #derecha arriba
                (-0.80*0.5) + 0.37, (-0.15*0.5) + 0.1,0.0,1.0,    13/255,255/255,0/255,1.0, # derecha abajo

                #Cuerpo
                (-0.73*0.5) + 0.37, (-0.25*0.5) + 0.1,0.0,1.0, 13/255,255/255,0/255,1.0,  #izquierda arriba
                (-0.73*0.5) + 0.37, (-0.15*0.5) + 0.1,0.0,1.0,    13/255,255/255,0/255,1.0,  #izquierda abajo
                (-0.83*0.5) + 0.37, (-0.25*0.5) + 0.1,0.0,1.0,     13/255,255/255,0/255,1.0, #derecha arriba
                (-0.83*0.5) + 0.37, (-0.15*0.5) + 0.1,0.0,1.0,    13/255,255/255,0/255,1.0, # derecha abajo

                # #pata 1
                (-0.84*0.5) + 0.37, (-0.13*0.5) + 0.1,0.0,1.0, 13/255,255/255,0/255,1.0,  #izquierda arriba
                (-0.84*0.5) + 0.37, (-0.15*0.5) + 0.1,0.0,1.0,    13/255,255/255,0/255,1.0,  #izquierda abajo
                (-0.82*0.5) + 0.37, (-0.13*0.5) + 0.1,0.0,1.0,     13/255,255/255,0/255,1.0, #derecha arriba
                (-0.82*0.5) + 0.37, (-0.15*0.5) + 0.1,0.0,1.0,    13/255,255/255,0/255,1.0,

                # #cuadrado arriba
                (-0.84*0.5) + 0.37, (-0.15*0.5) + 0.1,0.0,1.0, 13/255,255/255,0/255,1.0,  #izquierda arriba
                (-0.84*0.5) + 0.37, (-0.18*0.5) + 0.1,0.0,1.0,    13/255,255/255,0/255,1.0,  #izquierda abajo
                (-0.72*0.5) + 0.37, (-0.15*0.5) + 0.1,0.0,1.0,     13/255,255/255,0/255,1.0, #derecha arriba
                (-0.72*0.5) + 0.37, (-0.18*0.5) + 0.1,0.0,1.0,    13/255,255/255,0/255,1.0, 

                # #pata 
                (-0.84*0.5) + 0.37, (-0.22*0.5) + 0.1,0.0,1.0, 13/255,255/255,0/255,1.0,  #izquierda arriba
                (-0.84*0.5) + 0.37, (-0.27*0.5) + 0.1,0.0,1.0,    13/255,255/255,0/255,1.0,  #izquierda abajo
                (-0.82*0.5) + 0.37, (-0.22*0.5) + 0.1,0.0,1.0,     13/255,255/255,0/255,1.0, #derecha arriba
                (-0.82*0.5) + 0.37, (-0.27*0.5) + 0.1,0.0,1.0,    13/255,255/255,0/255,1.0,
                
                # #rectangulo abajo
                (-0.84*0.5) + 0.37, (-0.22*0.5) + 0.1,0.0,1.0, 13/255,255/255,0/255,1.0,  #izquierda arriba
                (-0.84*0.5) + 0.37, (-0.25*0.5) + 0.1,0.0,1.0,    13/255,255/255,0/255,1.0,  #izquierda abajo
                (-0.72*0.5) + 0.37, (-0.22*0.5) + 0.1,0.0,1.0,     13/255,255/255,0/255,1.0, #derecha arriba
                (-0.72*0.5) + 0.37, (-0.25*0.5) + 0.1,0.0,1.0,    13/255,255/255,0/255,1.0,

                # #pata 3
                (-0.74*0.5) + 0.37, (-0.13*0.5) + 0.1,0.0,1.0, 13/255,255/255,0/255,1.0,  #izquierda arriba
                (-0.74*0.5) + 0.37, (-0.15*0.5) + 0.1,0.0,1.0,    13/255,255/255,0/255,1.0,  #izquierda abajo
                (-0.72*0.5) + 0.37, (-0.13*0.5) + 0.1,0.0,1.0,     13/255,255/255,0/255,1.0, #derecha arriba
                (-0.72*0.5) + 0.37, (-0.15*0.5) + 0.1,0.0,1.0,    13/255,255/255,0/255,1.0,

                # #pata 4
                (-0.74*0.5) + 0.37, (-0.22*0.5) + 0.1,0.0,1.0, 13/255,255/255,0/255,1.0,  #izquierda arriba
                (-0.74*0.5) + 0.37, (-0.27*0.5) + 0.1,0.0,1.0,    13/255,255/255,0/255,1.0,  #izquierda abajo
                (-0.72*0.5) + 0.37, (-0.22*0.5) + 0.1,0.0,1.0,     13/255,255/255,0/255,1.0, #derecha arriba
                (-0.72*0.5) + 0.37, (-0.27*0.5) + 0.1,0.0,1.0,    13/255,255/255,0/255,1.0

            ], dtype="float32"
        )
        self.posicion = glm.vec3(0,0,0)
        self.transformaciones = glm.mat4(1.0)
        #self.transformaciones = glm.translate(self.transformaciones,
        #            glm.vec3(0.5,-0.2,0.0))
        #self.transformaciones = glm.rotate(self.transformaciones,
        #            45.0, glm.vec3(0.0,0.0,1.0))
        super().__init__(shader, posicion_id, color_id, transformaciones_id, self.x, self.y, self.z, self.velocidad, self.direccion)
        
        self.transformaciones = glm.mat4(1.0)
        self.transformaciones = glm.translate(self.transformaciones,
                   self.posicion)
        
    def mover(self, direccion):
        # cantidad_movimiento = glm.vec3(0,0,0)
        if direccion == self.ARRIBA:
            self.posicion.y = self.posicion.y + 0.1
        elif direccion == self.ABAJO:
            self.posicion.y = self.posicion.y - 0.1
        elif direccion == self.DERECHA:
            self.posicion.x = self.posicion.x + 0.1
        elif direccion == self.IZQUIERDA:
            self.posicion.x = self.posicion.x - 0.1

        self.transformaciones = glm.mat4(1.0)
        self.transformaciones = glm.translate(self.transformaciones,
                self.posicion)
        # self.transformaciones = glm.scale(self.transformaciones,
        #         (0.5, 0.5, 0.0))
        
    def dibujar(self):

        self.shader.usar_programa()
        gl.glBindVertexArray(self.VAO)

        gl.glUniformMatrix4fv(self.transformaciones_id,
                1, gl.GL_FALSE, glm.value_ptr(self.transformaciones))

        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 0, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 4, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 8, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 12, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 16, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 20, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 24, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 28, 4)


        gl.glBindVertexArray(0)
        self.shader.liberar_programa()

    def actualizar(self,window, key, scancode, action, mods):

        # estado_arriba = glfw.get_key(window, glfw.KEY_UP)
        # estado_abajo = glfw.get_key(window, glfw.KEY_DOWN)
        # estado_derecha = glfw.get_key(window, glfw.KEY_RIGHT)
        # estado_izquierda = glfw.get_key(window, glfw.KEY_LEFT)

        # if estado_arriba == glfw.PRESS:
        #     self.mover(self.ARRIBA)
        # if estado_abajo == glfw.PRESS:
        #     self.mover(self.ABAJO)
        # if estado_derecha == glfw.PRESS:
        #     self.mover(self.DERECHA)
        # if estado_izquierda == glfw.PRESS:
        #     self.mover(self.IZQUIERDA)

        #IZQUIERDA CON flecha
        if key == glfw.KEY_LEFT and (action == glfw.PRESS):
            self.mover(self.IZQUIERDA)
        #DERECHA CON flecha
        if key == glfw.KEY_RIGHT and (action == glfw.PRESS):
            self.mover(self.DERECHA)
        #ARRIBA CON flecha
        if key == glfw.KEY_UP and (action == glfw.PRESS):
            self.mover(self.ARRIBA)
        #ABAJO CON flecha
        if key == glfw.KEY_DOWN and (action == glfw.PRESS):
            self.mover(self.ABAJO)

