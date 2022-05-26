import math
from Modelo import *
import glm
import glfw

class Decoracion(Modelo):
    

    def __init__(self,shader, posicion_id, color_id, transformaciones_id):
        
        self.vertices = np.array(
            [

            ], dtype="float32"
        )

        for angulo in range(0, 359, 5):
            componente_x = 0.025 * math.cos(angulo * math.pi / 180) + 0.2
            componente_y =  0.025 * math.sin(angulo * math.pi / 180) - 0.35

            self.vertices = np.append(self.vertices, np.array([componente_x, componente_y, 0.0 , 1.0, 
                                                        125/255, 100/255, 70/255, 1.0 ], dtype="float32")),
        for angulo in range(0, 359, 5):
            componente_x = 0.025 * math.cos(angulo * math.pi / 180) + -0.35
            componente_y =  0.025 * math.sin(angulo * math.pi / 180) - 0.35

            self.vertices = np.append(self.vertices, np.array([componente_x, componente_y, 0.0 , 1.0, 
                                                        125/255, 125/255, 70/255, 1.0 ], dtype="float32"))
        for angulo in range(0, 359, 5):
            componente_x = 0.025 * math.cos(angulo * math.pi / 180) + -0.7
            componente_y =  0.025 * math.sin(angulo * math.pi / 180) - 0.35

            self.vertices = np.append(self.vertices, np.array([componente_x, componente_y, 0.0 , 1.0, 
                                                        125/255, 80/255, 70/255, 1.0 ], dtype="float32"))
        
        ###

        for angulo in range(0, 359, 5):
            componente_x = 0.025 * math.cos(angulo * math.pi / 180) + 0.79
            componente_y =  0.025 * math.sin(angulo * math.pi / 180) + 0.35

            self.vertices = np.append(self.vertices, np.array([componente_x, componente_y, 0.0 , 1.0, 
                                                       100/255, 80/255, 70/255, 1.0 ], dtype="float32")),
        for angulo in range(0, 359, 5):
            componente_x = 0.025 * math.cos(angulo * math.pi / 180) + -0.12
            componente_y =  0.025 * math.sin(angulo * math.pi / 180) + 0.35

            self.vertices = np.append(self.vertices, np.array([componente_x, componente_y, 0.0 , 1.0, 
                                                        150/255, 80/255, 70/255, 1.0 ], dtype="float32"))
        for angulo in range(0, 359, 5):
            componente_x = 0.025 * math.cos(angulo * math.pi / 180) + -0.6
            componente_y =  0.025 * math.sin(angulo * math.pi / 180) + 0.35

            self.vertices = np.append(self.vertices, np.array([componente_x, componente_y, 0.0 , 1.0, 
                                                        125/255, 80/255, 70/255, 1.0 ], dtype="float32"))

        

        self.posicion = glm.vec3(0,0,0)
        self.transformaciones = glm.mat4(1.0)

        super().__init__(shader, posicion_id, color_id, transformaciones_id)

        # self.transformaciones = glm.mat4(1.0)
        # self.transformaciones = glm.scale(self.transformaciones,
        #         (1.0, 0.5, 0.0))


        self.transformaciones = glm.mat4(1.0)
        self.transformaciones = glm.translate(self.transformaciones,
                self.posicion)
    
    def dibujar(self):
        self.shader.usar_programa()
        gl.glBindVertexArray(self.VAO)

        gl.glUniformMatrix4fv(self.transformaciones_id,
                1, gl.GL_FALSE, glm.value_ptr(self.transformaciones))

        gl.glDrawArrays(gl.GL_TRIANGLE_FAN, 0, 72)
        gl.glDrawArrays(gl.GL_TRIANGLE_FAN, 72, 72)
        gl.glDrawArrays(gl.GL_TRIANGLE_FAN, 144, 72)
        gl.glDrawArrays(gl.GL_TRIANGLE_FAN, 216, 72)
        gl.glDrawArrays(gl.GL_TRIANGLE_FAN, 288, 72)
        gl.glDrawArrays(gl.GL_TRIANGLE_FAN, 360, 72)



        gl.glBindVertexArray(0)
        self.shader.liberar_programa()