import math
import numpy as np
import matplotlib.pyplot as plt



fim = math.pi/2
inicio = 0
espaco = []
erro_lista_ret = []
erro_lista_trap = []
#gerar intervalos de espaçamentos entre os dados
for n in range (10,1010,10): 
    intervalo = (fim - inicio)/(n-1)
    espaco.append(n)
    
    dados_4 = []
    tempos_4 = []
    for i in range (n): #vamos gerar os dados
        data = inicio + intervalo * i
        tempos_4.append(data) #dados de tempo
        dados_4.append (math.cos(data)) #dados do cosseno
    
    soma_4 = 0
    for r in range (0,n-1,1): #regra dos retângulos
        soma_4 = soma_4 + intervalo*dados_4[r]
        erro_4 = 1 - soma_4
        absoluto_retangulo = abs(erro_4)
    erro_lista_ret.append(absoluto_retangulo)
    
    soma_5 = 0
    for t in range (0,n-1,1): # regra dos trapézios
        trapezios = intervalo * (dados_4[t]+dados_4[t+1])/2
        soma_5 = soma_5 + trapezios      
        erro_trapezio = 1 - soma_5
        absoluto_trapezio = abs(erro_trapezio)
    erro_lista_trap.append(absoluto_trapezio)


plt.figure()
plt.yscale('log')
plt.xlabel("Número de dados")
plt.ylabel('Erro')
plt.title('Erro de Integração numérica')
plt.plot (espaco, erro_lista_ret,'-b', label = "Retângulos")
plt.plot (espaco, erro_lista_trap, '-r', label = 'Trapézios' )
plt.legend(loc = 'upper right' )
plt.savefig ('Tarefa_4_Integracao.png')