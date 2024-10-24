### Controle de Processos
[![Aumente o nível e vá para o controle PID](https://img.shields.io/badge/Acessar-Controle%20PID-blue)](https://github.com/maiarasalmaso/controle.ON.OFF/blob/main/CONTROLE%20PID)

## Controle ON / OFF

Este é um exemplo de controle ON/OFF, cujo objetivo é regular a vazão de entrada por meio de uma válvula para controlar a altura do líquido no tanque. Há um arquivo em Python neste repositório que representa a simulação, e aqui você encontrará a explicação do mesmo.

![image](https://github.com/user-attachments/assets/0a764313-0210-4596-af72-7c94e38c3ec8)   ![image](https://github.com/user-attachments/assets/62e4d4b6-5772-4370-977f-d8ba3e0c4e62) onde ![image](https://github.com/user-attachments/assets/ce1e2ed7-a75b-4646-9030-82c91e84f3ab)

Ao lado da representação do tanque, constam as equações que representam este sistema, as quais podem ser resolvidas utilizando o método de Euler, por se tratar de um sistema simples que envolve poucas variáveis.
Este sisetma é uma ação DIRETA, pois quando eu quero aumentar o nível da água (VARIÁVEL CONTROLADA), a vazão que é a (VARIÁVEL MANIPULADA) deve ser aumentada

# Algoritmo Manual para o Metodo de Euler

####  Inicializacao
* Defina as constantes:
* fazr os cálculos com 
* Defina o numero de iteracoes desejadas (ou o tempo final).

####  Calculo do Proximo Valor
Deve-se calcular um dh/dt com base nos primreiros valores, e entao substituir na equação abaixo para achar o novo valor (próximo ao anterior) da altura do tanque.
O mesmo deve ser feito até chegar no tempo final desejado

![image](https://github.com/user-attachments/assets/aca7dc0f-d41c-4e41-bde6-b729fa4cc662)

# Algoritmo do Python  ( análise dos resultados)



### Gráfico obtido para a altura em relação ao tempo 

![image](https://github.com/user-attachments/assets/769701e1-e7e2-4113-8e37-4c4280b51f2f)

O gráfico apresenta uma simulação do nível de um tanque controlado por um sistema ON/OFF, com o objetivo de manter o nível de líquido próximo a um setpoint de 0,35 metros. O controle ON/OFF é um método simples, onde o sistema alterna entre ligar (ON) e desligar (OFF) o enchimento do tanque, dependendo da altura do líquido em relação ao valor de referência. No início da simulação, o nível do tanque está abaixo do setpoint, em aproximadamente 0,29 metros. Como o nível está abaixo do valor de referência, o controlador liga o enchimento do tanque, o que faz com que o nível de líquido comece a subir. Conforme o nível se aproxima de 0,35 metros, o controlador desliga o enchimento (OFF), fazendo com que o nível comece a cair novamente. Esse ciclo de liga e desliga se repete até 16 min sem nunca se estabilizar exatamente no setpoint. Essas oscilações no nível do tanque são resultado da ausência de uma ação proporcional que poderia ajustar gradualmente o fluxo de líquido. Em vez disso, o controle ON/OFF faz ajustes abruptos, o que leva a essas flutuações regulares. Apesar disso, o nível se mantém em uma faixa aceitável, próximo ao setpoint, mas sem alcançar precisão total.

### Gráfico obtido para a vazão em relação ao tempo

![image](https://github.com/user-attachments/assets/3d992e32-15c2-4bdc-bd37-154a5143080a)



