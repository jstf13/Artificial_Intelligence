import gym
import numpy as np

'''
Aquí tienes un ejemplo de cómo implementar el algoritmo de Q-Learning en 
el entorno de MountainCar de OpenAI Gym. En este ejemplo, entrenaremos al 
agente durante 1000 episodios y actualizaremos la función Q en cada paso 
utilizando una tasa de aprendizaje (alpha) y un factor de descuento (gamma).
'''

'''
Este código entrenará al agente utilizando el algoritmo de Q-Learning 
durante 1000 episodios y actualizará la función Q en cada paso. 
Después de entrenar, el agente probará su rendimiento y mostrará la recompensa 
total obtenida.
'''

def q_learning(env, num_episodes, alpha, gamma, epsilon):
    # Inicializar la matriz Q con ceros
    num_states = env.observation_space.shape[0]
    num_actions = env.action_space.n
    Q = np.zeros((num_states, num_actions))

    for episode in range(num_episodes):
        state = env.reset()
        done = False

        while not done:
            # Elegir una acción utilizando la política epsilon-greedy
            if np.random.rand() < epsilon:
                action = env.action_space.sample()
            else:
                action = np.argmax(Q[state])

            # Tomar la acción y observar el siguiente estado y recompensa
            next_state, reward, done, _ = env.step(action)

            # Actualizar la función Q
            Q[state][action] += alpha * (reward + gamma * np.max(Q[next_state]) - Q[state][action])

            state = next_state

    return Q

# Crear el entorno MountainCar
env = gym.make('MountainCar-v0')

# Definir los hiperparámetros
num_episodes = 1000
alpha = 0.1
gamma = 0.99
epsilon = 1.0

# Entrenar el agente utilizando Q-Learning
Q = q_learning(env, num_episodes, alpha, gamma, epsilon)

# Probar el agente entrenado
state = env.reset()
done = False
total_reward = 0

while not done:
    action = np.argmax(Q[state])
    state, reward, done, _ = env.step(action)
    total_reward += reward

    env.render()

print("Recompensa total: ", total_reward)

env.close()