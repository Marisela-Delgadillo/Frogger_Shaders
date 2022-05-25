import math
from Modelo import *
import glm
import glfw

class Carros2(Modelo):
    
    def __init__(self,shader, posicion_id, color_id, transformaciones_id,  posicion_x, posicion_y, posicion_z, velocidad, direccion):
        self.ARRIBA = 1
        self.ABAJO = 2
        self.IZQUIERDA = 3
        self.DERECHA = 4
        self.posicion = glm.vec3(0.0, 0.0, 0.0)
        self.posicion.x = posicion_x
        self.posicion.y = posicion_y
        self.posicion.z = posicion_z
        self.velocidad = velocidad
        self.direccion = direccion
        self.extremo_izquierdo = 0.05
        self.extremo_derecho = 0.05
        self.extremo_inferior = 0.05
        self.extremo_superior =0.05
        


   
        self.vertices = np.array([],dtype="float32")

        self.vertices = np.append(self.vertices, np.array(
            [


                #Carro
                -0.03,0.04,0.0, 1.0,       0,122/255,255/255, 1.0, #izq. arriba
                -0.03,-0.04,0.0,1.0,       0,122/255,255/255, 1.0, #izq. abajo
                0.05,0.04,0.0,1.0,         0,122/255,255/255, 1.0, #der. arriba
                0.05,-0.04,0.0,1.0,       0,122/255,255/255, 1.0,  #der. abajo

                -0.05,0.04,0.0, 1.0,       13/255,92/255,165/255, 1.0, #izq. arriba
                -0.05,-0.04,0.0,1.0,       13/255,92/255,165/255, 1.0, #izq. abajo
                0.01,0.04,0.0,1.0,         13/255,92/255,165/255, 1.0, #der. arriba
                0.01,-0.04,0.0,1.0,       13/255,92/255,165/255, 1.0,  #der. abajo

                -0.05,0.05,0.0, 1.0,       0.0, 0.0, 0.0, 1.0, #izq. arriba
                -0.05,0.04,0.0,1.0,       0.0, 0.0, 0.0, 1.0, #izq. abajo
                -0.03,0.05,0.0,1.0,         0.0, 0.0, 0.0, 1.0, #der. arriba
                -0.03,0.04,0.0, 1.0,       0.0, 0.0, 0.0, 1.0,  #der. abajo

                0.03,0.05,0.0, 1.0,       0.0, 0.0, 0.0, 1.0, #izq. arriba
                0.03,0.04,0.0,1.0,       0.0, 0.0, 0.0, 1.0, #izq. abajo
                0.05,0.05,0.0,1.0,         0.0, 0.0, 0.0, 1.0, #der. arriba
                0.05,0.04,0.0,1.0,       0.0, 0.0, 0.0, 1.0,  #der. abajo
                
                0.03,-0.04,0.0, 1.0,       0.0, 0.0, 0.0, 1.0, #izq. arriba
                0.03,-0.05,0.0,1.0,       0.0, 0.0, 0.0, 1.0, #izq. abajo
                0.05,-0.04,0.0,1.0,         0.0, 0.0, 0.0, 1.0, #der. arriba
                0.05,-0.05,0.0,1.0,       0.0, 0.0, 0.0, 1.0,  #der. abajo

                -0.05,-0.04,0.0, 1.0,       0.0, 0.0, 0.0, 1.0, #izq. arriba
                -0.05,-0.05,0.0,1.0,       0.0, 0.0, 0.0, 1.0, #izq. abajo
                -0.03,-0.04,0.0,1.0,         0.0, 0.0, 0.0, 1.0, #der. arriba
                -0.03,-0.05,0.0,1.0,       0.0, 0.0, 0.0, 1.0,  #der. abajo

               
            ], dtype="float32"

            
        ))

        self.posicion = glm.vec3(0,0,0)
        self.transformaciones = glm.mat4(1.0)

        super().__init__(shader, posicion_id, color_id, transformaciones_id, posicion_x, posicion_y, posicion_z, velocidad, direccion)

        #self.transformaciones = glm.mat4(1.0)
        # self.transformaciones = glm.scale(self.transformaciones,
        #         (0.5, 0.5, 0.0))

    def actualizar(self, tiempo_delta):
        #global window
        
        cantidad_movimiento = self.velocidad * tiempo_delta
        if self.direccion == 3.0:
            self.posicion.x = self.posicion.x + cantidad_movimiento
            if self.posicion.x >= 1:
                self.posicion.x = -1
        self.transformaciones = glm.mat4(1.0)
        self.transformaciones = glm.translate(self.transformaciones,
                self.posicion)
    
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


        gl.glBindVertexArray(0)
        self.shader.liberar_programa()

