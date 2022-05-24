import math
from Modelo import *
import glm
import glfw

class Lineas(Modelo):
    
    def __init__(self,shader, posicion_id, color_id, transformaciones_id):
        self.ARRIBA = 1
        self.ABAJO = 2
        self.IZQUIERDA = 3
        self.DERECHA = 4
        
        self.vertices = np.array([],dtype="float32")

        self.vertices = np.append(self.vertices, np.array(
            [


                #Lineas Blancas Calle 1
                -1.1,0.7+0.65,0.0, 1.0,       1.0, 1.0, 1.0, 1.0, #izq. arriba
                -1.1,0.6+0.65,0.0,1.0,       1.0, 1.0, 1.0, 1.0, #izq. abajo
                -0.6,0.7+0.65,0.0,1.0,         1.0, 1.0, 1.0, 1.0, #der. arriba
                -0.6,0.6+0.65,0.0,1.0,       1.0, 1.0, 1.0, 1.0,  #der. abajo

                -0.5,0.7+0.65,0.0, 1.0,       1.0, 1.0, 1.0, 1.0, #izq. arriba
                -0.5,0.6+0.65,0.0,1.0,       1.0, 1.0, 1.0, 1.0, #izq. abajo
                0.1,0.7+0.65,0.0,1.0,         1.0, 1.0, 1.0, 1.0, #der. arriba
                0.1,0.6+0.65,0.0,1.0,       1.0, 1.0, 1.0, 1.0,  #der. abajo

                0.2,0.7+0.65,0.0, 1.0,       1.0, 1.0, 1.0, 1.0, #izq. arriba
                0.2,0.6+0.65,0.0,1.0,       1.0, 1.0, 1.0, 1.0, #izq. abajo
                0.8,0.7+0.65,0.0,1.0,         1.0, 1.0, 1.0, 1.0, #der. arriba
                0.8,0.6+0.65,0.0,1.0,       1.0, 1.0, 1.0, 1.0,  #der. abajo

                0.9,0.7+0.65,0.0, 1.0,       1.0, 1.0, 1.0, 1.0, #izq. arriba
                0.9,0.6+0.65,0.0,1.0,       1.0, 1.0, 1.0, 1.0, #izq. abajo
                1.0,0.7+0.65,0.0,1.0,         1.0, 1.0, 1.0, 1.0, #der. arriba
                1.0,0.6+0.65,0.0,1.0,       1.0, 1.0, 1.0, 1.0,  #der. abajo

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
                -1.1,-0.7-0.65,0.0, 1.0,       1.0, 1.0, 1.0, 1.0, #izq. arriba
                -1.1,-0.6-0.65,0.0,1.0,       1.0, 1.0, 1.0, 1.0, #izq. abajo
                -0.6,-0.7-0.65,0.0,1.0,         1.0, 1.0, 1.0, 1.0, #der. arriba
                -0.6,-0.6-0.65,0.0,1.0,       1.0, 1.0, 1.0, 1.0,  #der. abajo

                -0.5,-0.7-0.65,0.0, 1.0,       1.0, 1.0, 1.0, 1.0, #izq. arriba
                -0.5,-0.6-0.65,0.0,1.0,       1.0, 1.0, 1.0, 1.0, #izq. abajo
                0.1,-0.7-0.65,0.0,1.0,         1.0, 1.0, 1.0, 1.0, #der. arriba
                0.1,-0.6-0.65,0.0,1.0,       1.0, 1.0, 1.0, 1.0,  #der. abajo

                0.2,-0.7-0.65,0.0, 1.0,       1.0, 1.0, 1.0, 1.0, #izq. arriba
                0.2,-0.6-0.65,0.0,1.0,       1.0, 1.0, 1.0, 1.0, #izq. abajo
                0.8,-0.7-0.65,0.0,1.0,         1.0, 1.0, 1.0, 1.0, #der. arriba
                0.8,-0.6-0.65,0.0,1.0,       1.0, 1.0, 1.0, 1.0,  #der. abajo

                0.9,-0.7-0.65,0.0, 1.0,       1.0, 1.0, 1.0, 1.0, #izq. arriba
                0.9,-0.6-0.65,0.0,1.0,       1.0, 1.0, 1.0, 1.0, #izq. abajo
                1.0,-0.7-0.65,0.0,1.0,         1.0, 1.0, 1.0, 1.0, #der. arriba
                1.0,-0.6-0.65,0.0,1.0,       1.0, 1.0, 1.0, 1.0,  #der. abajo

               
            ], dtype="float32"

            
        ))

        self.posicion = glm.vec3(0,0,0)
        self.transformaciones = glm.mat4(1.0)

        super().__init__(shader, posicion_id, color_id, transformaciones_id)

        self.transformaciones = glm.mat4(1.0)
        self.transformaciones = glm.scale(self.transformaciones,
                (1.0, 0.5, 0.0))

    
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

        gl.glBindVertexArray(0)
        self.shader.liberar_programa()

