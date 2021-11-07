from typing import no_type_check
import numpy as np

def zigzag(input):
    #initializing the variables
    #----------------------------------
    h = 0
    v = 0

    vmin = 0
    hmin = 0

    vmax = input.shape[0]
    hmax = input.shape[1]
    
    #print(vmax ,hmax )

    i = 0

    output = np.zeros(( vmax * hmax))
    #----------------------------------

    while ((v < vmax) and (h < hmax)):
    	
        if ((h + v) % 2) == 0:                 # going up
            
            if (v == vmin):
            	#print(1)
                output[i] = input[v, h]        # if we got to the first line

                if (h == hmax):
                    v = v + 1
                else:
                    h = h + 1                        

                i = i + 1

            elif ((h == hmax -1 ) and (v < vmax)):   # if we got to the last column
            	#print(2)
            	output[i] = input[v, h] 
            	v = v + 1
            	i = i + 1

            elif ((v > vmin) and (h < hmax -1 )):    # all other cases
            	#print(3)
            	output[i] = input[v, h] 
            	v = v - 1
            	h = h + 1
            	i = i + 1

        
        else:                                    # going down

        	if ((v == vmax -1) and (h <= hmax -1)):       # if we got to the last line
        		#print(4)
        		output[i] = input[v, h] 
        		h = h + 1
        		i = i + 1
        
        	elif (h == hmin):                  # if we got to the first column
        		#print(5)
        		output[i] = input[v, h] 

        		if (v == vmax -1):
        			h = h + 1
        		else:
        			v = v + 1

        		i = i + 1

        	elif ((v < vmax -1) and (h > hmin)):     # all other cases
        		#print(6)
        		output[i] = input[v, h] 
        		v = v + 1
        		h = h - 1
        		i = i + 1




        if ((v == vmax-1) and (h == hmax-1)):          # bottom right element
        	#print(7)        	
        	output[i] = input[v, h] 
        	break

    #print ('v:',v,', h:',h,', i:',i)
    return output

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
print(np.matmul(figure_1,figure_2))
a = np.matmul(figure_1,figure_2)
b = np.matmul(figure_2,a)
print("A")

print(a)
print("B")
print(b)
print("------------------------------")
yk=b;
# yk_tmp = np.zeros([figure_1.shape[0],figure_1.shape[1]])
# for i in range(figure_1.shape[0]):
#     for j in range(figure_1.shape[1]):
#         yk_tmp[i,j]= figure_1[i,j] * math.cos(((2*i+1)*j*math.pi)/16)
#     # y_k[i] = yk    
# yk = np.zeros([figure_1.shape[0],figure_1.shape[1]])

# for i1 in range(figure_1.shape[0]):
#     yk[:,i1] = np.matmul(yk_tmp[i1,:],figure_2[:,i1])
# print(yk)
Z_u_v= np.array([[16, 11 ,10, 16 ,24 ,40 ,51 ,61],
                [12 ,12 ,14 ,19 ,26, 58 ,60 ,55],
                [14 ,13 ,16 ,24 ,40 ,57 ,69 ,56],
                [14 ,17 ,22 ,29 ,51 ,87 ,80 ,62],
                [18 ,22 ,37 ,56 ,68 ,109 ,103, 77],
                [24 ,35 ,55 ,64 ,81 ,104 ,113 ,92],
                [49 ,64 ,78 ,87 ,103 ,121 ,120 ,101],
                [72 ,92, 95 ,98, 112 ,100, 103 ,99]])
QF = 1
f_u_v = np.zeros([figure_1.shape[0],figure_1.shape[1]],dtype=np.uint8)
f_u_v = np.round(yk/(QF*Z_u_v))
print("000000000000000000000")
print("fuv",f_u_v)
newdata=list()
for line in f_u_v:
    line = list(line)
    newdata.append(line)
print(newdata)
# import matplotlib.pyplot as plt
# plt.figure(f_u_v)
# plt.show()
print(zigzag(f_u_v))