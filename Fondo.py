import math
from Modelo import *
import glm
import glfw

class Fondo(Modelo):
    
    def __init__(self,shader, posicion_id, color_id, transformaciones_id):
        self.ARRIBA = 1
        self.ABAJO = 2
        self.IZQUIERDA = 3
        self.DERECHA = 4
        
        self.vertices = np.array(
            [
                #Calle
                -1.0, 1.0,0.0,1.0, 84/255,85/255,84/255,1.0,  #izquierda arriba
                -1.0, -1.0,0.0,1.0,    84/255,85/255,84/255,1.0,  #izquierda abajo
                1.0, 1.0,0.0,1.0,     84/255,85/255,84/255,1.0, #derecha arriba
                1.0, -1.0,0.0,1.0,    84/255,85/255,84/255,1.0, # derecha abajo
                
                #Agua
                -1.0, -0.9,0.0,1.0, 3/255, 153/255, 185/255,1.0,  #izquierda arriba
                -1.0, -1.0,0.0,1.0,    3/255, 153/255, 185/255,1.0,  #izquierda abajo
                1.0, -0.9,0.0,1.0,     3/255, 153/255, 185/255,1.0, #derecha arriba
                1.0, -1.0,0.0,1.0,    3/255, 153/255, 185/255,1.0, # derecha abajo

                #Cesped
                -1.0, -0.3,0.0,1.0, 125/255, 179/255, 70/255,1.0,  #izquierda arriba
                -1.0, -0.4,0.0,1.0,    125/255, 179/255, 70/255,1.0,  #izquierda abajo
                 1.0, -0.3,0.0,1.0,     125/255, 179/255, 70/255,1.0, #derecha arriba
                1.0, -0.4,0.0,1.0,    125/255, 179/255, 70/255,1.0, # derecha abajo

                #Tierra
                -1.0, 0.4,0.0,1.0, 179/255, 131/255, 70/255,1.0,  #izquierda arriba
                -1.0, 0.3,0.0,1.0,    179/255, 131/255, 70/255,1.0,  #izquierda abajo
                 1.0, 0.4,0.0,1.0,     179/255, 131/255, 70/255,1.0, #derecha arriba
                1.0, 0.3,0.0,1.0,    179/255, 131/255, 70/255,1.0, # derecha abajo

                #Meta
                -1.0, 1.0,0.0,1.0, 255/255, 243/255, 1/255,1.0,  #izquierda arriba
                -1.0, 0.9,0.0,1.0,    255/255, 243/255, 1/255,1.0,  #izquierda abajo
                1.0, 1.0,0.0,1.0,     255/255, 243/255, 1/255,1.0, #derecha arriba
                1.0, 0.9,0.0,1.0,    255/255, 243/255, 1/255,1.0, # derecha abajo       

                #Lineas calle
                -1.0, 1.0,0.0,1.0, 255/255, 243/255, 1/255,1.0,  #izquierda arriba
                -1.0, 0.9,0.0,1.0,    255/255, 243/255, 1/255,1.0,  #izquierda abajo
                1.0, 1.0,0.0,1.0,     255/255, 243/255, 1/255,1.0, #derecha arriba
                1.0, 0.9,0.0,1.0,    255/255, 243/255, 1/255,1.0, # derecha abajo 

                #Lineas Blancas Calle 1
                -1.1,0.7,0.0, 1.0,       1.0, 1.0, 1.0, 1.0, #izq. arriba
                -1.1,0.6,0.0,1.0,       1.0, 1.0, 1.0, 1.0, #izq. abajo
                -0.6,0.7,0.0,1.0,         1.0, 1.0, 1.0, 1.0, #der. arriba
                -0.6,0.6,0.0,1.0,       1.0, 1.0, 1.0, 1.0,  #der. abajo

                -0.5,0.7,0.0, 1.0,       1.0, 1.0, 1.0, 1.0, #izq. arriba
                -0.5,0.6,0.0,1.0,       1.0, 1.0, 1.0, 1.0, #izq. abajo
                0.1,0.7,0.0,1.0,         1.0, 1.0, 1.0, 1.0, #der. arriba
                0.1,0.6,0.0,1.0,       1.0, 1.0, 1.0, 1.0,  #der. abajo

                0.2,0.7,0.0, 1.0,       1.0, 1.0, 1.0, 1.0, #izq. arriba
                0.2,0.6,0.0,1.0,       1.0, 1.0, 1.0, 1.0, #izq. abajo
                0.8,0.7,0.0,1.0,         1.0, 1.0, 1.0, 1.0, #der. arriba
                0.8,0.6,0.0,1.0,       1.0, 1.0, 1.0, 1.0,  #der. abajo

                0.9,0.7,0.0, 1.0,       1.0, 1.0, 1.0, 1.0, #izq. arriba
                0.9,0.6,0.0,1.0,       1.0, 1.0, 1.0, 1.0, #izq. abajo
                1.0,0.7,0.0,1.0,         1.0, 1.0, 1.0, 1.0, #der. arriba
                1.0,0.6,0.0,1.0,       1.0, 1.0, 1.0, 1.0,  #der. abajo

                #Lineas Blancas Calle 2
                -1.5,0.05,0.0, 1.0,       1.0, 1.0, 1.0, 1.0, #izq. arriba
                -1.5,-0.05,0.0,1.0,       1.0, 1.0, 1.0, 1.0, #izq. abajo
                -0.9,0.05,0.0,1.0,         1.0, 1.0, 1.0, 1.0, #der. arriba
                -0.9,-0.05,0.0,1.0,       1.0, 1.0, 1.0, 1.0,  #der. abajo

                -0.8,0.05,0.0, 1.0,       1.0, 1.0, 1.0, 1.0, #izq. arriba
                -0.8,-0.05,0.0,1.0,       1.0, 1.0, 1.0, 1.0, #izq. abajo
                -0.2,0.05,0.0,1.0,         1.0, 1.0, 1.0, 1.0, #der. arriba
                -0.2,-0.05,0.0,1.0,       1.0, 1.0, 1.0, 1.0,  #der. abajo

                -0.1,0.05,0.0, 1.0,       1.0, 1.0, 1.0, 1.0, #izq. arriba
                -0.1,-0.05,0.0,1.0,       1.0, 1.0, 1.0, 1.0, #izq. abajo
                0.5,0.05,0.0,1.0,         1.0, 1.0, 1.0, 1.0, #der. arriba
                0.5,-0.05,0.0,1.0,       1.0, 1.0, 1.0, 1.0,  #der. abajo

                0.6,0.05,0.0, 1.0,       1.0, 1.0, 1.0, 1.0, #izq. arriba
                0.6,-0.05,0.0,1.0,       1.0, 1.0, 1.0, 1.0, #izq. abajo
                1.0,0.05,0.0,1.0,         1.0, 1.0, 1.0, 1.0, #der. arriba
                1.0,-0.05,0.0,1.0,       1.0, 1.0, 1.0, 1.0,  #der. abajo

                #Lineas Blancas Calle 3
                -1.1,-0.7,0.0, 1.0,       1.0, 1.0, 1.0, 1.0, #izq. arriba
                -1.1,-0.6,0.0,1.0,       1.0, 1.0, 1.0, 1.0, #izq. abajo
                -0.6,-0.7,0.0,1.0,         1.0, 1.0, 1.0, 1.0, #der. arriba
                -0.6,-0.6,0.0,1.0,       1.0, 1.0, 1.0, 1.0,  #der. abajo

                -0.5,-0.7,0.0, 1.0,       1.0, 1.0, 1.0, 1.0, #izq. arriba
                -0.5,-0.6,0.0,1.0,       1.0, 1.0, 1.0, 1.0, #izq. abajo
                0.1,-0.7,0.0,1.0,         1.0, 1.0, 1.0, 1.0, #der. arriba
                0.1,-0.6,0.0,1.0,       1.0, 1.0, 1.0, 1.0,  #der. abajo

                0.2,-0.7,0.0, 1.0,       1.0, 1.0, 1.0, 1.0, #izq. arriba
                0.2,-0.6,0.0,1.0,       1.0, 1.0, 1.0, 1.0, #izq. abajo
                0.8,-0.7,0.0,1.0,         1.0, 1.0, 1.0, 1.0, #der. arriba
                0.8,-0.6,0.0,1.0,       1.0, 1.0, 1.0, 1.0,  #der. abajo

                0.9,-0.7,0.0, 1.0,       1.0, 1.0, 1.0, 1.0, #izq. arriba
                0.9,-0.6,0.0,1.0,       1.0, 1.0, 1.0, 1.0, #izq. abajo
                1.0,-0.7,0.0,1.0,         1.0, 1.0, 1.0, 1.0, #der. arriba
                1.0,-0.6,0.0,1.0,       1.0, 1.0, 1.0, 1.0,  #der. abajo

            ], dtype="float32"
        )

        self.posicion = glm.vec3(0,0,0)
        self.transformaciones = glm.mat4(1.0)

        super().__init__(shader, posicion_id, color_id, transformaciones_id)

    
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
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 32, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 36, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 40, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 44, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 48, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 52, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 56, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 60, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 64, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 68, 4)



        gl.glBindVertexArray(0)
        self.shader.liberar_programa()