import numpy as np
import matplotlib.pyplot as plt

# Passo 1: definir as variáveis 
A = 0.3  # Área do tanque
qe0 = 0.015  # Vazão inicial de entrada
R = 19.5  # Constante de proporcionalidade
h0 = 0.2925  # Nível inicial do tanque

# Parâmetros da simulação 
deltat = 2  # Intervalo de tempo da simulação em minutos
acao_on = 0.02  # Ação de entrada ON
acao_off = 0  # Ação de entrada OFF
setpoint = 0.35  # Ponto de ajuste do nível do tanque

# Parâmetros do controlador
tempo_simulacao = 16  # Tempo total de simulação em minutos

# Passo 2: definir a equação diferencial 
def edo_tanque(h, qe):
    dh_dt = (1/A) * (qe - (h/R))
    return dh_dt

# Passo 5: função do controlador ON/OFF (ação direta)
def controlador_on_off(h, setpoint, tolerancia=0.02):
    if h <= (setpoint - tolerancia):  # Ligar a entrada
        return acao_on
    elif h >= (setpoint + tolerancia):  # Desligar a entrada
        return acao_off
    else:  # Manter a entrada constante
        return qe0

# Função para simular o tanque
def simular_tanque(h0, qe0, A, R, setpoint, tempo_simulacao, deltat):
    h = h0
    qe = qe0

    # Listas para armazenar os resultados
    tempo_lista = []
    qe_lista = []
    h_lista = []

    # Simulação
    for tempo_atual in np.arange(0, tempo_simulacao + deltat, deltat):
        # Armazenar os valores atuais
        tempo_lista.append(tempo_atual)
        qe_lista.append(qe)
        h_lista.append(h)

        # Atualizar a entrada usando o controlador ON/OFF apenas se o tempo for maior ou igual a 4 minutos
        if tempo_atual >= 4:
            qe = controlador_on_off(h, setpoint)

        # Calcular a nova altura usando o método de Euler
        dh_dt = edo_tanque(h, qe)  # Calcula a taxa de variação da altura
        h = h + dh_dt * deltat  # Atualiza h com o método de Euler

    return tempo_lista, qe_lista, h_lista

# Chamada da função de simulação
tempo_lista, qe_lista, h_lista = simular_tanque(h0, qe0, A, R, setpoint, tempo_simulacao, deltat)

# Gráfico da altura do tanque
plt.figure(figsize=(10, 5))
plt.plot(tempo_lista, h_lista, label='Altura do Tanque (h)', color='blue')
plt.axhline(y=setpoint, color='r', linestyle='--', label='Setpoint')
plt.xlabel('Tempo (min)')
plt.ylabel('Altura do Tanque (m)')
plt.title('Simulação do Nível do Tanque com Controle ON/OFF (Ação Direta)')
plt.grid()
plt.legend()
plt.show()

# Gráfico da vazão
plt.figure(figsize=(10, 5))
plt.plot(tempo_lista, qe_lista, label='Vazão (qe)', color='green')
plt.xlabel('Tempo (min)')
plt.ylabel('Vazão (m³/min)')
plt.title('Vazão de Entrada no Tanque')
plt.grid()
plt.legend()
plt.show()
