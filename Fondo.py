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
        
        self.vertices = np.array([],dtype="float32")

        self.vertices = np.append(self.vertices, np.array(
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
                -1.1,0.7*0.5,0.0, 1.0,       1.0, 1.0, 1.0, 1.0, #izq. arriba
                -1.1,0.6*0.5,0.0,1.0,       1.0, 1.0, 1.0, 1.0, #izq. abajo
                -0.6,0.7*0.5,0.0,1.0,         1.0, 1.0, 1.0, 1.0, #der. arriba
                -0.6,0.6*0.5,0.0,1.0,       1.0, 1.0, 1.0, 1.0,  #der. abajo

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

                -0.3,0.05,0.0, 1.0,       1.0, 1.0, 1.0, 1.0, #izq. arriba
                -0.3,-0.05,0.0,1.0,       1.0, 1.0, 1.0, 1.0, #izq. abajo
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

                #tronco
                -0.3,-1,0.0, 1.0,       0.6, 0.3, 0.3, 1.0, #izq. arriba
                -0.3,-0.9,0.0,1.0,       0.6, 0.3, 0.3, 1.0, #izq. abajo
                0.2,-1,0.0,1.0,         0.6, 0.3, 0.3, 1.0, #der. arriba
                0.2,-0.9,0.0,1.0,       0.6, 0.3, 0.3, 1.0,  #der. abajo

                #Meta Lineas Negras
                -1.0, 1.0,0.0,1.0,          0, 0, 0,1.0,  #izquierda arriba
                -1.0, 0.9,0.0,1.0,          0, 0, 0,1.0,  #izquierda abajo
                -0.9, 1.0,0.0,1.0,           0, 0, 0,1.0, #derecha arriba
                -0.9, 0.9,0.0,1.0,           0, 0, 0,1.0, # derecha abajo 

                -0.8, 1.0,0.0,1.0,          0, 0, 0,1.0,  #izquierda arriba
                -0.8, 0.9,0.0,1.0,          0, 0, 0,1.0,  #izquierda abajo
                -0.7, 1.0,0.0,1.0,           0, 0, 0,1.0, #derecha arriba
                -0.7, 0.9,0.0,1.0,           0, 0, 0,1.0, # derecha abajo 

                -0.6, 1.0,0.0,1.0,          0, 0, 0,1.0,  #izquierda arriba
                -0.6, 0.9,0.0,1.0,          0, 0, 0,1.0,  #izquierda abajo
                -0.5, 1.0,0.0,1.0,           0, 0, 0,1.0, #derecha arriba
                -0.5, 0.9,0.0,1.0,           0, 0, 0,1.0, # derecha abajo 

                -0.4, 1.0,0.0,1.0,          0, 0, 0,1.0,  #izquierda arriba
                -0.4, 0.9,0.0,1.0,          0, 0, 0,1.0,  #izquierda abajo
                -0.3, 1.0,0.0,1.0,           0, 0, 0,1.0, #derecha arriba
                -0.3, 0.9,0.0,1.0,           0, 0, 0,1.0, # derecha abajo 

                -0.2, 1.0,0.0,1.0,          0, 0, 0,1.0,  #izquierda arriba
                -0.2, 0.9,0.0,1.0,          0, 0, 0,1.0,  #izquierda abajo
                -0.1, 1.0,0.0,1.0,           0, 0, 0,1.0, #derecha arriba
                -0.1, 0.9,0.0,1.0,           0, 0, 0,1.0, # derecha abajo 

                0.0, 1.0,0.0,1.0,          0, 0, 0,1.0,  #izquierda arriba
                0.0, 0.9,0.0,1.0,          0, 0, 0,1.0,  #izquierda abajo
                0.1, 1.0,0.0,1.0,           0, 0, 0,1.0, #derecha arriba
                0.1, 0.9,0.0,1.0,           0, 0, 0,1.0, # derecha abajo 

                0.2, 1.0,0.0,1.0,          0, 0, 0,1.0,  #izquierda arriba
                0.2, 0.9,0.0,1.0,          0, 0, 0,1.0,  #izquierda abajo
                0.3, 1.0,0.0,1.0,           0, 0, 0,1.0, #derecha arriba
                0.3, 0.9,0.0,1.0,           0, 0, 0,1.0, # derecha abajo 

                0.4, 1.0,0.0,1.0,          0, 0, 0,1.0,  #izquierda arriba
                0.4, 0.9,0.0,1.0,          0, 0, 0,1.0,  #izquierda abajo
                0.5, 1.0,0.0,1.0,           0, 0, 0,1.0, #derecha arriba
                0.5, 0.9,0.0,1.0,           0, 0, 0,1.0, # derecha abajo 

                0.6, 1.0,0.0,1.0,          0, 0, 0,1.0,  #izquierda arriba
                0.6, 0.9,0.0,1.0,          0, 0, 0,1.0,  #izquierda abajo
                0.7, 1.0,0.0,1.0,           0, 0, 0,1.0, #derecha arriba
                0.7, 0.9,0.0,1.0,           0, 0, 0,1.0, # derecha abajo 

                0.8, 1.0,0.0,1.0,          0, 0, 0,1.0,  #izquierda arriba
                0.8, 0.9,0.0,1.0,          0, 0, 0,1.0,  #izquierda abajo
                0.9, 1.0,0.0,1.0,           0, 0, 0,1.0, #derecha arriba
                0.9, 0.9,0.0,1.0,           0, 0, 0,1.0, # derecha abajo 

                1, 1.0,0.0,1.0,          0, 0, 0,1.0,  #izquierda arriba
                1, 0.9,0.0,1.0,          0, 0, 0,1.0,  #izquierda abajo
                1.1, 1.0,0.0,1.0,           0, 0, 0,1.0, #derecha arriba
                1.1, 0.9,0.0,1.0,           0, 0, 0,1.0, # derecha abajo 

                #peatonal
                -1.5,-0.25,0.0, 1.0,       1, 1, 1, 1, #izq. arriba
                -1.5,-0.28,0.0,1.0,       1, 1, 1, 1, #izq. abajo
                -0.9,-0.25,0.0,1.0,         1, 1, 1, 1, #der. arriba
                -0.9,-0.28,0.0,1.0,       1, 1, 1, 1,  #der. abajo

                -1.5,-0.20,0.0, 1.0,       1, 1, 1, 1, #izq. arriba
                -1.5,-0.23,0.0,1.0,       1, 1, 1, 1, #izq. abajo
                -0.9,-0.20,0.0,1.0,         1, 1, 1, 1, #der. arriba
                -0.9,-0.23,0.0,1.0,       1, 1, 1, 1,  #der. abajo

                -1.5,-0.15,0.0, 1.0,       1, 1, 1, 1, #izq. arriba
                -1.5,-0.18,0.0,1.0,       1, 1, 1, 1, #izq. abajo
                -0.9,-0.15,0.0,1.0,         1, 1, 1, 1, #der. arriba
                -0.9,-0.18,0.0,1.0,       1, 1, 1, 1,  #der. abajo

                -1.5,-0.10,0.0, 1.0,       1, 1, 1, 1, #izq. arriba
                -1.5,-0.13,0.0,1.0,       1, 1, 1, 1, #izq. abajo
                -0.9,-0.10,0.0,1.0,         1, 1, 1, 1, #der. arriba
                -0.9,-0.13,0.0,1.0,       1, 1, 1, 1,  #der. abajo

                -1.5,-0.05,0.0, 1.0,       1, 1, 1, 1, #izq. arriba
                -1.5,-0.08,0.0,1.0,       1, 1, 1, 1, #izq. abajo
                -0.9,-0.05,0.0,1.0,         1, 1, 1, 1, #der. arriba
                -0.9,-0.08,0.0,1.0,       1, 1, 1, 1,  #der. abajo

                ###################################################

                -1.5,0.25,0.0, 1.0,       1, 1, 1, 1, #izq. arriba
                -1.5,0.28,0.0,1.0,       1, 1, 1, 1, #izq. abajo
                -0.9,0.25,0.0,1.0,         1, 1, 1, 1, #der. arriba
                -0.9,0.28,0.0,1.0,       1, 1, 1, 1,  #der. abajo

                -1.5,0.20,0.0, 1.0,       1, 1, 1, 1, #izq. arriba
                -1.5,0.23,0.0,1.0,       1, 1, 1, 1, #izq. abajo
                -0.9,0.20,0.0,1.0,         1, 1, 1, 1, #der. arriba
                -0.9,0.23,0.0,1.0,       1, 1, 1, 1,  #der. abajo

                -1.5,0.15,0.0, 1.0,       1, 1, 1, 1, #izq. arriba
                -1.5,0.18,0.0,1.0,       1, 1, 1, 1, #izq. abajo
                -0.9,0.15,0.0,1.0,         1, 1, 1, 1, #der. arriba
                -0.9,0.18,0.0,1.0,       1, 1, 1, 1,  #der. abajo

                -1.5,0.10,0.0, 1.0,       1, 1, 1, 1, #izq. arriba
                -1.5,0.13,0.0,1.0,       1, 1, 1, 1, #izq. abajo
                -0.9,0.10,0.0,1.0,         1, 1, 1, 1, #der. arriba
                -0.9,0.13,0.0,1.0,       1, 1, 1, 1,  #der. abajo

                -1.5,0.05,0.0, 1.0,       1, 1, 1, 1, #izq. arriba
                -1.5,0.08,0.0,1.0,       1, 1, 1, 1, #izq. abajo
                -0.9,0.05,0.0,1.0,         1, 1, 1, 1, #der. arriba
                -0.9,0.08,0.0,1.0,       1, 1, 1, 1,  #der. abajo

                #alcantarilla
                #0.0,-0.2,0.0,1.0,  0,0.1,0.1,0
            ], dtype="float32"

            
        ))
        #Alcantarilla
        for i in range(0,361,5):
            self.vertices = np.append(self.vertices,
                np.array(
                    [0.08 * math.cos(i * math.pi/180.0),0.08 * math.sin(i * math.pi/180) -0.2,0.0,1.0,  0,0.1,0.1,0]
                , dtype="float32"))
        #Nenufar
        for angulo in range(0, 359, 5):
            componente_x = 0.04 * math.cos(angulo * math.pi / 180) + 0.4
            componente_y =  0.025 * math.sin(angulo * math.pi / 180) - 0.95

            self.vertices = np.append(self.vertices, np.array([componente_x, componente_y, 0.0 , 1.0, 
                                                       40/255, 121/255, 17/255, 1.0 ], dtype="float32"))
        for angulo in range(0, 359, 5):
            componente_x = 0.04 * math.cos(angulo * math.pi / 180) + 0.2
            componente_y =  0.025 * math.sin(angulo * math.pi / 180) - 0.35

            self.vertices = np.append(self.vertices, np.array([componente_x, componente_y, 0.0 , 1.0, 
                                                       40/255, 121/255, 17/255, 1.0 ], dtype="float32"))

        self.posicion = glm.vec3(0,0,0)
        self.transformaciones = glm.mat4(1.0)
        self.posicion = glm.vec3(0,0,0)
        self.transformaciones = glm.mat4(1.0)

        super().__init__(shader, posicion_id, color_id, transformaciones_id)

        # self.transformaciones = glm.mat4(1.0)
        # self.transformaciones = glm.scale(self.transformaciones,
        #         (1.0, 0.5, 0.0))

    
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
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 72, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 76, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 80, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 84, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 88, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 92, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 96, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 100, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 104, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 108, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 112, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 116, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 120, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 124, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 128, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 132, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 136, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 140, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 144, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 148, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 152, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 156, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_FAN, 160, 74)
        gl.glDrawArrays(gl.GL_TRIANGLE_FAN, 234, 70)
        



        gl.glBindVertexArray(0)
        self.shader.liberar_programa()

