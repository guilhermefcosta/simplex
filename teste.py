from matplotlib.pyplot import axis
import numpy as np
n = 3
m = 3
# log_c = np.zeros(n)
# matriz_de_operacoes = np.identity(n)

# aux = np.vstack((log_c, matriz_de_operacoes))
# o = np.zeros(shape=(3,5))

# t = np.hstack(())
# print(aux)

C = [2., 4., 8., 0., 0., 0.]

A = np.array([
 [1., 0., 0., 1., 0., 0.],
 [0., 1., 0., 0., 1., 0.],
 [0., 0., 1., 0., 0., 1.]]
)

B = np.array([
    [1.],
    [1.],
    [1.]
])

B_tableux = np.vstack((np.array([[0.]]), B))
A_C = np.vstack((C, A))
ACB = np.hstack((A_C, B_tableux))
print(ACB)

op_de_c = np.zeros(n)
mat_operacoes = np.identity(n)
mat_op_completa = np.vstack((op_de_c, mat_operacoes))
print(mat_op_completa)

tableux = np.hstack((mat_op_completa, ACB))
print(tableux)


print(tableux[2, -1])
# print(np.vstack((C, A)))
# print(np.hstack((A, B)))
# print(np.vstack((np.array([[0]]), B)))