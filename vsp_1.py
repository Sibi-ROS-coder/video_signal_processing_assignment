from typing import no_type_check


import numpy as np
figure_1 = np.array([[10 ,10, 10, 10, 10, 10, 10, 10],
                    [10, 10, 10, 10, 10, 10, 10, 10],
                    [20 ,20, 20, 20, 20, 20, 20, 20],
                    [20, 20, 20 ,20, 20 ,20, 20 ,20],
                    [40, 40 ,40 ,40 ,40 ,40 ,40 ,40],
                    [40 ,40 ,40 ,40 ,40 ,40 ,40 ,40],
                    [10 ,10 ,10 ,10 ,10 ,10, 10 ,10],
                    [10 ,10 ,10, 10 ,10, 10, 10, 10]])
figure_2 = np.array([[1,1,1,1,1,1,1,1],
                    [1,-1,1,-1,1,-1,1,-1],
                    [1,1,-1,-1,1,1,-1,-1],
                    [1,-1,-1,1,1,-1,-1,1],
                    [1,1,1,1,-1,-1,-1,-1],
                    [1,-1,1,-1,-1,1,-1,1],
                    [1,1,-1,-1,-1,-1,1,1],
                    [1,-1,-1,1,-1,1,1,-1]])
# print()
import math
yk_tmp = np.zeros([figure_1.shape[0],figure_1.shape[1]])
for i in range(figure_1.shape[0]):
    for j in range(figure_1.shape[1]):
        yk_tmp[i,j]= figure_1[i,j] * math.cos(((2*i+1)*j*math.pi)/16)
    # y_k[i] = yk    
yk = np.zeros([figure_1.shape[0],figure_1.shape[1]])

for i1 in range(figure_1.shape[0]):
    yk[:,i1] = np.matmul(yk_tmp[i1,:],figure_2[:,i1])
# print(yk)
Z_u_v= np.array([[16, 11 ,10, 16 ,24 ,40 ,51 ,61],
                [12 ,12 ,14 ,19 ,26, 58 ,60 ,55],
                [14 ,13 ,16 ,24 ,40 ,57 ,69 ,56],
                [14 ,17 ,22 ,29 ,51 ,87 ,80 ,62],
                [18 ,22 ,37 ,56 ,68 ,109 ,103, 77],
                [24 ,35 ,55 ,64 ,81 ,104 ,113 ,92],
                [49 ,64 ,78 ,87 ,103 ,121 ,120 ,101],
                [72 ,92, 95 ,98, 112 ,100, 103 ,99]])
QF = 2
f_u_v = np.zeros([figure_1.shape[0],figure_1.shape[1]],dtype=np.uint8)
f_u_v = np.round(yk/(QF*Z_u_v))
print(f_u_v)
newdata=list()
for line in f_u_v:
    line = list(line)
    newdata.append(line)
print(newdata)
# import matplotlib.pyplot as plt
# plt.figure(f_u_v)
# plt.show()