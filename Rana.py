import math
from Modelo import *
import glm
import glfw

class Rana(Modelo):
    
    def __init__(self,shader, posicion_id, color_id, transformaciones_id):
        self.ARRIBA = 1
        self.ABAJO = 2
        self.IZQUIERDA = 3
        self.DERECHA = 4
        
        self.vertices = np.array(
            [
                # #Rana cabeza
                # -0.76+0.75, -0.11-0.75,0.0,1.0, 13/255,255/255,0/255,1.0,  #izquierda arriba
                # -0.76+0.75, -0.15-0.75,0.0,1.0,    13/255,255/255,0/255,1.0,  #izquierda abajo
                # -0.80+0.75, -0.11-0.75,0.0,1.0,     13/255,255/255,0/255,1.0, #derecha arriba
                # -0.80+0.75, -0.15-0.75,0.0,1.0,    13/255,255/255,0/255,1.0, # derecha abajo

                #Cuerpo
                -0.74+0.75, -0.25-0.75,0.0,1.0, 13/255,255/255,0/255,1.0,  #izquierda arriba
                -0.74+0.75, -0.15-0.75,0.0,1.0,    13/255,255/255,0/255,1.0,  #izquierda abajo
                -0.82+0.75, -0.25-0.75,0.0,1.0,     13/255,255/255,0/255,1.0, #derecha arriba
                -0.82+0.75, -0.15-0.75,0.0,1.0,    13/255,255/255,0/255,1.0, # derecha abajo

                # #pata 1
                # -0.84+0.75, -0.13-0.75,0.0,1.0, 13/255,255/255,0/255,1.0,  #izquierda arriba
                # -0.84+0.75, -0.15-0.75,0.0,1.0,    13/255,255/255,0/255,1.0,  #izquierda abajo
                # -0.82+0.75, -0.13-0.75,0.0,1.0,     13/255,255/255,0/255,1.0, #derecha arriba
                # -0.82+0.75, -0.15-0.75,0.0,1.0,    13/255,255/255,0/255,1.0,

                # #cuadrado arriba
                # -0.84+0.75, -0.15-0.75,0.0,1.0, 13/255,255/255,0/255,1.0,  #izquierda arriba
                # -0.84+0.75, -0.18-0.75,0.0,1.0,    13/255,255/255,0/255,1.0,  #izquierda abajo
                # -0.72+0.75, -0.15-0.75,0.0,1.0,     13/255,255/255,0/255,1.0, #derecha arriba
                # -0.72+0.75, -0.18-0.75,0.0,1.0,    13/255,255/255,0/255,1.0, 

                # #pata 
                # -0.84+0.75, -0.22-0.75,0.0,1.0, 13/255,255/255,0/255,1.0,  #izquierda arriba
                # -0.84+0.75, -0.27-0.75,0.0,1.0,    13/255,255/255,0/255,1.0,  #izquierda abajo
                # -0.82+0.75, -0.22-0.75,0.0,1.0,     13/255,255/255,0/255,1.0, #derecha arriba
                # -0.82+0.75, -0.27-0.75,0.0,1.0,    13/255,255/255,0/255,1.0,
                
                # #rectangulo abajo
                # -0.84+0.75, -0.22-0.75,0.0,1.0, 13/255,255/255,0/255,1.0,  #izquierda arriba
                # -0.84+0.75, -0.25-0.75,0.0,1.0,    13/255,255/255,0/255,1.0,  #izquierda abajo
                # -0.72+0.75, -0.22-0.75,0.0,1.0,     13/255,255/255,0/255,1.0, #derecha arriba
                # -0.72+0.75, -0.25-0.75,0.0,1.0,    13/255,255/255,0/255,1.0,

                # #pata 3
                # -0.74+0.75, -0.13-0.75,0.0,1.0, 13/255,255/255,0/255,1.0,  #izquierda arriba
                # -0.74+0.75, -0.15-0.75,0.0,1.0,    13/255,255/255,0/255,1.0,  #izquierda abajo
                # -0.72+0.75, -0.13-0.75,0.0,1.0,     13/255,255/255,0/255,1.0, #derecha arriba
                # -0.72+0.75, -0.15-0.75,0.0,1.0,    13/255,255/255,0/255,1.0

            ], dtype="float32"
        )
        self.posicion = glm.vec3(0,0,0)
        self.transformaciones = glm.mat4(1.0)
        #self.transformaciones = glm.translate(self.transformaciones,
        #            glm.vec3(0.5,-0.2,0.0))
        #self.transformaciones = glm.rotate(self.transformaciones,
        #            45.0, glm.vec3(0.0,0.0,1.0))
        super().__init__(shader, posicion_id, color_id, transformaciones_id)

    def mover(self, direccion):
        # cantidad_movimiento = glm.vec3(0,0,0)
        if direccion == self.ARRIBA:
            self.posicion.y = self.posicion.y + 0.001
        elif direccion == self.ABAJO:
            self.posicion.y = self.posicion.y - 0.001
        elif direccion == self.DERECHA:
            self.posicion.x = self.posicion.x + 0.001
        elif direccion == self.IZQUIERDA:
            self.posicion.x = self.posicion.x - 0.001

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
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 8, 14)

        gl.glBindVertexArray(0)
        self.shader.liberar_programa()

