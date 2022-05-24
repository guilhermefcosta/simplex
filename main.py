import numpy as np
from scipy import linalg

''' 
TP1 - PO
'''

''' 
CAPTURANDO TODAS AS ENTRADAS
'''

# B = np.zeros(shape=(3, 1))
# print(B[0, 0])
# exit



n, m = input().split(' ')
n = int(n)
m = int(m)

entrada2 = input().split()
C = np.zeros(m)
for i in range(m):
    C[i] = int(entrada2[i])
    
A = np.zeros(shape=(n,m))
B = np.zeros(shape=(n, 1))
for i in range(n):
    entrada_linhas = input().split(' ')
    for j in range(m):
        A[i,j] = np.float64(entrada_linhas[j])
    B[i, 0] = entrada_linhas[m]

''' 
Adicionar as variaveis de folga
'''

folgas = np.identity(n)
A_new = np.append(A, folgas, axis=1)
C_new = np.append(C, np.zeros(n))

print("C\n",  C_new)
print("A\n",  A_new)
print("b\n",  B)


''' 

Gerar Tableux Auxiliar Extendida

Enquanto C não estiver (negativa/positiva)
    1. O vetor b tem que estar positivo (checar)
    2. Até que C maior que 0 pivotear
    3. passos simplex
    4. se V.O menor que 0, então vetor de operações de C é o certificado de inviabilidade
    5. Se V.O igual a 0, prosseguimos
'''


''' 
Gerar Tableux Original

1. Tableux já vem na forma canônica e em FPI
2. Observamos C, enquando não estiver (positiva)
3. Então, um ciclo do simplex, até encontrar valor
4. Se, temos um valor em c negativo(Regra de Brand) 
   que vamos aumentar xi associado e temos e sua coluna
   está toda negativa... entao temos certificado de ilimitada
5. Se não nos deparamos com esse caso então, temos uma soluçao ótima na matriz de operacoes
'''


''' FALTA MUITO, MAS BORA LÁ '''
    

