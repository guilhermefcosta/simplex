from matplotlib.pyplot import table
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

C_original = -np.append(C, np.zeros(n))

op_de_c = np.zeros(n)
mat_operacoes = np.identity(n)

''' Checar se tenho todas entradas positivas no b '''
linhas_negativas_b = []
for i in range(n):
    if (B[i, 0] < 0):
        B[i, 0] = -B[i, 0]
        A[i,:] = -A[i,:]
        mat_operacoes[i,:] = -mat_operacoes[i,:]
        
        
#matriz A setada aqui
folgas = np.identity(n)
A_new = np.append(A, folgas, axis=1)


# CRIAR UMA FUNCAO para optimizar
''' 
*** HOJE ***
Gerar Tableux Auxiliar Extendida

Enquanto C não estiver (negativa/positiva)
    1. O vetor b tem que estar positivo (checar)
    2. Até que C maior que 0 pivotear
    3. passos simplex
    4. se V.O menor que 0, então vetor de operações de C é o certificado de inviabilidade
    5. Se V.O igual a 0, prosseguimos
'''
# Gerando o tableux
B_tableux = np.vstack((np.array([[0.]]), B))

C_auxiliar = np.append(np.zeros(m), np.ones(n))
A_C_auxiliar = np.vstack((C_auxiliar, A_new))
ACB_auxiliar = np.hstack((A_C_auxiliar, B_tableux)) 

A_C = np.vstack((C_original, A_new))
ACB_original = np.hstack((A_C, B_tableux)) 

# os componentes dessa matriz foram construidos acima
mat_op_completa = np.vstack((op_de_c, mat_operacoes))

tableux_original = np.hstack((mat_op_completa, ACB_original))
tableux_auxiliar = np.hstack((mat_op_completa, ACB_auxiliar))


print(tableux_auxiliar)
print()
print(tableux_original)
print()


''' Agora temos que deixar na forma canônica a PL Auxiliar '''
bases_colunas = [n+m+1, n+m+2]
for i in range(n):
    tableux_auxiliar[0,:] = -tableux_auxiliar[i+1,:] + tableux_auxiliar[0,:]

print("Forma Canonica") 
print(tableux_auxiliar)

input("Digite algo para continuar")

''' Enquanto tivermos algum valor menor que 0 '''
while ((tableux_auxiliar[0,n:-1] < 0).any()):
    print("Entrei")
    # varremos o c até encontrar um valor < 0
    for i in range(n+m):
        if tableux_auxiliar[0,n+i] < 0:
            nova_base = n+i # nova base
            print(nova_base)
            break
                        
    # nao há ilimitada pois sabemos que a auxiliar é sempre limitada
    menor = np.inf
    linha_menor = 0
    for j in range(n):
        print("Aij = ",  tableux_auxiliar[j+1,nova_base])
        if (tableux_auxiliar[j+1,nova_base] > 0): # Aij > 0
            b_a = tableux_auxiliar[j+1, -1] / tableux_auxiliar[j+1,nova_base]
            print("bij_Aij = ", b_a)
            input("Seguir...")
            if (b_a < menor): #se for igual nao muda (caimos no principio da não ciclagem)
                input("Entrei no ultimo if")
                menor = b_a
                linha_menor = j+1

    print(linha_menor)
    print("elemento a ser pivoteado: ", tableux_auxiliar[linha_menor, nova_base])
    # divimos a linha pelo pivô 
    tableux_auxiliar[linha_menor,:] = tableux_auxiliar[linha_menor,:] * 1.0/tableux_auxiliar[linha_menor, nova_base]
    print(tableux_auxiliar)
    
    # escalamento
    # teremos a coluna e a linha que teremos que pivoterar
    # Fazer eliminacao de gaus
    for i in range(n+1):
        if (i == linha_menor):
            continue
        # vamos zerar todos da coluna
        bij = tableux_auxiliar[i, nova_base]
        print(bij)
        input("Aqui")
        if (bij != 0): # não faço nada
            tableux_auxiliar[i,:] = (-bij * tableux_auxiliar[linha_menor,:]) + tableux_auxiliar[i,:]
           
                
    print(tableux_auxiliar)
    print("----")
    input("Pressione algo para ir para proxima iteracao...")              



''' 
*** AMANHÂ *** 
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
    

