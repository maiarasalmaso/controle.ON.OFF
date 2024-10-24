### Controle de Processos
## Controle ON / OFF

Este é um exemplo de controle ON/OFF, cujo objetivo é regular a vazão de entrada por meio de uma válvula para controlar a altura do líquido no tanque. Há um arquivo em Python neste repositório que representa a simulação, e aqui você encontrará a explicação do mesmo.

![image](https://github.com/user-attachments/assets/0a764313-0210-4596-af72-7c94e38c3ec8)   ![image](https://github.com/user-attachments/assets/62e4d4b6-5772-4370-977f-d8ba3e0c4e62) onde ![image](https://github.com/user-attachments/assets/ce1e2ed7-a75b-4646-9030-82c91e84f3ab)

Ao lado da representação do tanque, constam as equações que representam este sistema, as quais podem ser resolvidas utilizando o método de Euler, por se tratar de um sistema simples que envolve poucas variáveis.

# Algoritmo Manual para o Metodo de Euler

####  Inicializacao
* Defina as constantes:
* fazr os cálculos com 
* Defina o numero de iteracoes desejadas (ou o tempo final).

####  Calculo do Proximo Valor
Deve-se calcular um dh/dt com base nos primreiros valores, e entao substituir na equação abaixo para achar o novo valor da altura do tanque. o mesmo deve ser feito até chegar no tempo final desejado
![image](https://github.com/user-attachments/assets/aca7dc0f-d41c-4e41-bde6-b729fa4cc662)
