import random

def mochila_genetico(pesos, valores, capacidad, poblacion_size=100, generaciones=1000):
    def crear_individuo():
        return [random.randint(0, 1) for _ in range(len(valores))]

    def calcular_fitness(individuo):
        peso_total = sum(pesos[i] * individuo[i] for i in range(len(individuo)))
        valor_total = sum(valores[i] * individuo[i] for i in range(len(individuo)))
        return valor_total if peso_total <= capacidad else 0

    poblacion = [crear_individuo() for _ in range(poblacion_size)]

    for _ in range(generaciones):
        poblacion = sorted(poblacion, key=calcular_fitness, reverse=True)
        nueva_generacion = poblacion[:10]  # Mantener los mejores

        while len(nueva_generacion) < poblacion_size:
            padre1, padre2 = random.choices(poblacion[:30], k=2)  # Selección
            punto_cruce = random.randint(1, len(valores) - 1)
            hijo = padre1[:punto_cruce] + padre2[punto_cruce:]
            if random.random() < 0.1:  # Mutación
                index_mutacion = random.randint(0, len(hijo) - 1)
                hijo[index_mutacion] = 1 - hijo[index_mutacion]  # Flip
            nueva_generacion.append(hijo)

        poblacion = nueva_generacion

    mejor_individuo = max(poblacion, key=calcular_fitness)
    return calcular_fitness(mejor_individuo)

# Ejemplo
max_valor_genetico = mochila_genetico(pesos, valores, capacidad)
print(f'Máximo valor (Algoritmo Genético): {max_valor_genetico}')


# Usé un algoritmo genético para resolver el problema
# de qué artículos llevar al campo, maximizando
# el valor sin exceder la capacidad de mi mochila.
# Generé una población inicial con combinaciones de
# artículos y evalué cada una en función de su valor
# total y peso. En cada iteración, seleccioné
# las mejores soluciones, realicé cruces entre ellas y
# apliqué mutaciones para generar nuevas combinaciones.
# Así, fui mejorando progresivamente la selección
# de artículos. Aunque no garantiza la solución
# perfecta, me permitió encontrar
# una buena combinación en un tiempo razonable.
