from numpy import exp, array, random, dot

class NeuralNetwork():
    def __init__(self):
        # Seed el generador de números aleatorios, con una raíz a fin de generar 
        # los mismo números aleatorios en cada proceso.
        random.seed(1)

        # Modelamos una sola neurona, con 3 conexiones de entrada y una conexión de salida
        # Asignamos los pesos aleatorios a una matriz de 3x1, con valores en el rango de -1 a 1
        # y significa 0
        self.synaptic_weights = 2 * random.random((8, 1)) - 1

    # La función Sigmoid, que describe una curva en forma de S
    # Se pasan la suma ponderada de las entradas a través de esta función para 
    # normalizarlos entre 0 y 1.
    def __sigmoid(self, x):
        return 1 / (1 + exp(-x))

    # La derivada de la función Sigmoid.
    # Este es el gradiente de la función Sigmoid.
    # Indica la confianza que tenemos en el peso existente.
    def __sigmoid_derivative(self, x):
        return x * (1 - x)

    # Entrenamos a la red neuronal a través de un proceso de prueba y error
    # Se realiza un ajuste de los pesos sinápticos cada vez.
    def train(self, training_set_inputs, training_set_outputs, number_of_training_iterations=1000):
        for iteration in range(number_of_training_iterations):
            # Pasar el conjunto de entrenamiento a través de nuestra red neuronal (una sola neurona)
            output = self.think(training_set_inputs)

            # Calcular el error(La diferencia entre el resultado deseado
            # y el resultado obtenido).
            error = training_set_outputs - output

            # Multiplica el error por la entrada y nuevamente por el gradiente de la curva Sigmoid
            # Esto significa que los pesos menos confiables se están ajustando más
            # Esto significa que las entradas que son cero, no causan cambios en los pesos.
            adjustment = dot(training_set_inputs.T, error * self.__sigmoid_derivative(output))

            # Ajuste de los pesos
            self.synaptic_weights += adjustment

    # La red neuronal piensa.
    def think(self, inputs):
        # Pasar las entradas a través de nuestra red neuronal (una neurona)
        return self.__sigmoid(dot(inputs, self.synaptic_weights))


# if __name__ == "__main__":

#     #Iniciar una red neuronal de una neurona
#     neural_network = NeuralNetwork()

#     print ("Random starting synaptic weights: ")
#     print (neural_network.synaptic_weights)

#     # El conjunto de pruebas. Tenemos cuatro ejemplos, cada uno consiste en 3 valores de entrada
#     # y un valor de salida.
#     training_set_inputs = array([[0, 0, 1], [1, 1, 1], [1, 0, 1], [0, 1, 1]])
#     print("Datos de entrada de entrenamiento")
#     print(training_set_inputs)
#     training_set_outputs = array([[0, 1, 1, 0]]).T
#     print("Datos de salida de entrenamiento")
#     print(training_set_outputs)

#     # Entrenar la red neuronal utilizando el conjunto de entrenamiento.
#     # Realizar 10000 veces y realizar un ajuste más pequeño cada vez.
#     neural_network.train(training_set_inputs, training_set_outputs, 10000)

#     print ("New synaptic weights after training: ")
#     print (neural_network.synaptic_weights)

#     # Prueba la red neuronal con una nueva situación
#     print ("Considering new situation [1, 0, 0] -> ?: ")
#     print (neural_network.think(array([1, 0, 0])))