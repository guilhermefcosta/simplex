import numpy as np

def printArray(arr):
    arr = arr.astype(np.float64).tolist()
    for n in range(len(arr)):
        if (n != len(arr)-1):
            print('{:.7f} '.format(arr[n]), end='')
        else:
            print('{:.7f}'.format(arr[n]))
       

# a = np.array([1,2,3.0])
# printArray(a)
# exit
''' 
TP1 - PO
'''

''' 
CAPTURANDO TODAS AS ENTRADAS
'''
# bases iniciais da auxiliar


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
Gerar Tableux Auxiliar Extendida

Enquanto C não estiver (negativa/positiva)
    1. O vetor b tem que estar positivo (checar)
    2. Até que C maior que 0 pivotear
    3. passos simplex
    4. se V.O menor que 0, então vetor de operações de C é o certificado de inviabilidade
    5. Se V.O igual a 0, prosseguimos
'''
# Gerando o tableuxd
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

bases_aux = [] 
for i in range(n):
    #               (coluna)
    bases_aux.append(n+m+i)

''' Agora temos que deixar na forma canônica a PL Auxiliar '''
for i in range(n):
    tableux_auxiliar[0,:] = -tableux_auxiliar[i+1,:] + tableux_auxiliar[0,:]

print(tableux_auxiliar)

''' Enquanto tivermos algum valor menor que 0 '''
while ((tableux_auxiliar[0,n:-1] < 0).any()):
    # varremos o c até encontrar um valor < 0
    for i in range(n+m):
        if tableux_auxiliar[0,n+i] < 0:
            nova_base = n+i # nova base
            break
    
    print("nova_base: ", nova_base)             
    # nao há ilimitada pois sabemos que a auxiliar é sempre limitada
    menor = np.inf
    linha_menor = 0
    for j in range(n):
        if (tableux_auxiliar[j+1,nova_base] > 0): # Aij > 0
            b_a = tableux_auxiliar[j+1, -1] / tableux_auxiliar[j+1,nova_base]
            if (b_a < menor and b_a >= 0): #se for igual nao muda (caimos no principio da não ciclagem)
                menor = b_a
                linha_menor = j+1
    print("menor_linha: ", linha_menor)
    # divimos a linha pelo pivô 
    tableux_auxiliar[linha_menor,:] = tableux_auxiliar[linha_menor,:] * 1.0/tableux_auxiliar[linha_menor, nova_base]
    input("esc")
    print(tableux_auxiliar)
    # escalamento
    # teremos a coluna e a linha que teremos que pivoterar
    # Fazer eliminacao de gaus
    for i in range(n+1):
        if (i == linha_menor):
            continue
        # vamos zerar todos da coluna
        bij = tableux_auxiliar[i, nova_base]
        if (bij != 0): # não faço nada
            tableux_auxiliar[i,:] = (-bij * tableux_auxiliar[linha_menor,:]) + tableux_auxiliar[i,:]
            print(tableux_auxiliar)
    
    bases_aux[linha_menor-1] = nova_base
    print("bases:", bases_aux)
    
# visualizando auxiliar 
VO = tableux_auxiliar[0,-1]
if (VO < 0):
    cert_inv = tableux_auxiliar[0,0:n]
    
    print('inviavel')
    printArray(cert_inv)
    exit(0)



''' 
*** HOJE *** 
Gerar Tableux Original

1. Tableux já vem na forma canônica e em FPI
2. Observamos C, enquanto não estiver (positiva)
3. Então, um ciclo do simplex, até encontrar valor
4. Se, temos um valor em c negativo(Regra de Brand) 
   que vamos aumentar xi associado e temos e sua coluna
   está toda negativa... entao temos certificado de ilimitada
5. Se não nos deparamos com esse caso então, temos uma soluçao ótima na matriz de operacoes
'''

# bases iniciais
bases_map = [] 
for i in range(n):
    #               (coluna)
    bases_map.append(n+m+i)
    
while ((tableux_original[0, n:-1] < 0).any()):
        
    # Já está na forma canônica
    # varrendo C
    for i in range(n+m):
        if tableux_original[0,n+i] < 0:
            nova_base = n+i # nova base
            break

    # checamos se temos o caso de uma ilimitada
    if ((tableux_original[1:,nova_base] <= 0).all()):
        # temos uma ilimitada
        # Ad <= b | d >= 0  
        d = np.zeros(n+m)
        # x_viav = np.zeros(n+m) 
        d[nova_base-n] = 1.0
        
        val_base_ilimitada = -tableux_original[1:,nova_base]
        val_viavel = tableux_original[1:, -1]
        for i in range(n):
            d[bases_map[i]-n] = val_base_ilimitada[i]   
            # x_viav[bases_map[i]-n] = val_viavel[i]   

        
        print("ilimitada")
        # viavel
        viavel = np.zeros(m+n)
        b_aux = tableux_auxiliar[1:, -1]
        for i in range(n):
            viavel[bases_aux[i]-n] = b_aux[i]
         
        printArray(viavel[:m])
        printArray(d[:m]) # certificado de ilimitada cortando a folga
        # printArray(x_viav) # viavel cortando a folga
        exit(0)

    # Aqui podemos ter ilimitada 
    # escolha do menor bij / Aij
    menor = np.inf
    linha_menor = 0
    for j in range(n):
        if (tableux_original[j+1,nova_base] > 0): # Aij > 0
            b_a = tableux_original[j+1, -1] / tableux_original[j+1,nova_base]
            
            # posso ter um erro no **and**
            if (b_a < menor and b_a >= 0): # se for igual nao muda (caimos no principio da não ciclagem)
                menor = b_a
                linha_menor = j+1

    # NESSE PONTO TENHO AS COORDENADAS DO PIVÔ
    # (linha_menor, nova_base)
    
    # divimos a linha pelo pivô 
    tableux_original[linha_menor,:] = tableux_original[linha_menor,:] * 1.0/tableux_original[linha_menor, nova_base]
    # escalamento
    # teremos a coluna e a linha que teremos que pivoterar
    # Fazer eliminacao de gauss
    for i in range(n+1):
        if (i == linha_menor):
            continue
        # vamos zerar todos da coluna
        bij = tableux_original[i, nova_base]
        if (bij != 0): # não faço nada
            tableux_original[i,:] = (-bij * tableux_original[linha_menor,:]) + tableux_original[i,:]
    
    # Agora inserimos a nova coluna na base
    bases_map[linha_menor-1] = nova_base

''' 
Printando...
'''

print("otima")
printArray(np.array([tableux_original[0,-1]]))

otimo_x = np.zeros(n+m)
for i in range(n):
    otimo_x[bases_map[i] - n] =  tableux_original[i+1, -1]
    
printArray(otimo_x[:m])
printArray(tableux_original[0, :n])


    

