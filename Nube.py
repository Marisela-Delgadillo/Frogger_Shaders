import math
from Modelo import *
import glm
import glfw

class Nube(Modelo):
    
    angulo_nube = 0
    fase = 330.0

    def __init__(self,shader, posicion_id, color_id, transformaciones_id):
        
        self.vertices = np.array(
            [

            ], dtype="float32"
        )

        for angulo in range(0, 359, 5):
            componente_x = (0.1 * math.cos(angulo * math.pi / 180) -0.1)*0.5
            componente_y =  (0.12 * math.sin(angulo * math.pi / 180) + 0.65)*0.5

            self.vertices = np.append(self.vertices, np.array([componente_x, componente_y, 0.0 , 1.0, 
                                                        1.0, 1.0,1.0, 1.0 ], dtype="float32"))

        for angulo in range(0, 359, 5):
            componente_x = (0.15 * math.cos(angulo * math.pi / 180) -0.15)*0.5 
            componente_y =  (0.09 * math.sin(angulo * math.pi / 180) + 0.61)*0.5

            self.vertices = np.append(self.vertices, np.array([componente_x, componente_y, 0.0 , 1.0, 
                                                        1.0, 1.0,1.0, 1.0 ], dtype="float32"))

        for angulo in range(0, 359, 5):
            componente_x = (0.15 * math.cos(angulo * math.pi / 180) + 0.01)*0.5 
            componente_y =  (0.09 * math.sin(angulo * math.pi / 180) + 0.61)*0.5

            self.vertices = np.append(self.vertices, np.array([componente_x, componente_y, 0.0 , 1.0, 
                                                        1.0, 1.0,1.0, 1.0 ], dtype="float32"))

        self.posicion = glm.vec3(0,0,0)
        self.transformaciones = glm.mat4(1.0)

        super().__init__(shader, posicion_id, color_id, transformaciones_id)

        # self.transformaciones = glm.mat4(1.0)
        # self.transformaciones = glm.scale(self.transformaciones,
        #         (1.0, 0.5, 0.0))

    def actualizar(self, tiempo_delta):
        movimiento_nube = 0.2 * tiempo_delta
        self.posicion.x = self.posicion.x + (
                math.cos((self.angulo_nube + self.fase) * math.pi / 180.0) * movimiento_nube
            )
        self.posicion.y = self.posicion.y + (
                math.sin((self.angulo_nube + self.fase) * math.pi / 180.0) * movimiento_nube
            )

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



        gl.glBindVertexArray(0)
        self.shader.liberar_programa()

