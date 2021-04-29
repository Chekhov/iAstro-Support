from math import *
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
from pprint import *
from scipy import stats
import click
import statistics
from mpl_toolkits.mplot3d import Axes3D 

def cumulative(y, n_bins = 10):   
    # TODO o resultado deve ser apenas cumulativo, sem fazer plot da funcao para permitir inversoes x y -> y x
    return stats.cumfreq(y, numbins = n_bins).cumcount

# TODO interpolation

def splining(x, y, kind = "natural", k0t = 0, kNt = 0):
    # x,y autoexplained
    # k0t and kNT are optional inputs and only necessary for clamped splines
    if (len(x)==len(y)):
        N = len(x) -1
        #Contruir v, e w
        v = []
        w = []
        for k in range(0, N):
            pV = y[k+1] - y[k]
            pW = 1/(x[k+1] - x[k])
            v.append(pV)
            w.append(pW)
        #Construir Delta
        if (kind =='periodic'):
            delta = periodic(v,w,N)
            Y = delta
        if (kind =='clamped'):
            delta = periodic(v,w,N).pop(0)
            nDelta = np.zeros((N,))
            nDelta[0] = -1*w[0]*k0t
            nDelta[N-1] = -1*w[N-1]*kNt
            Y = delta - nDelta
        if (kind =='natural'):
            delta = periodic(v,w,N)
            delta[0] = 3*v[0]*pow(w[0],2)
            dF = 3*v[N-1]*pow(w[N-1],2)
            delta.append(dF)
            Y = delta
        #Construir Omega
        base_matrix = np.zeros((N+1,N+1))
        for k in range(0, N+1): 
            if k == 0:
                base_matrix[0,0] = 2*w[0]
                base_matrix[0,1] = w[0]
            elif k == N:
                base_matrix[N,N] = w[N-1]
                base_matrix[N,N] = 2*w[N-1]
            else:
                base_matrix[k,k-1]= w[k-1]
                base_matrix[k,k] = 2*(w[k-1]+ w[k])
                base_matrix[k, k+1]= w[k]
        if (kind == 'periodic'):
            base_matrix =  np.delete(base_matrix, (N), axis = 0) #eliminar a ultima linha
            base_matrix =  np.delete(base_matrix, (N), axis = 1) #eliminar a ultima coluna
            base_matrix[0,0] += 2*w[N-1]
            base_matrix[0,N-1] = w[N-1]
            base_matrix[N-1,0] = w[N-1]
        elif (kind == 'clamped'):
            base_matrix =  np.delete(base_matrix, (0), axis = 0) #eliminar a primeir linha
            base_matrix =  np.delete(base_matrix, (0), axis = 1) #eliminar a primeir coluna
        else : 
            print('')
        print (base_matrix)
        print (Y)
        return (np.linalg.solve(base_matrix, Y),w)
    else:
        print("NO VALUE, x and y sizes don't match")

def periodic(v, w, N):
    delta = []
    pD =3*(v[0]*pow(w[0],2) + v[N-1]*pow(w[N-1],2))
    delta.append(pD)
    for k in range(1,N):
        pD = 3*(v[k]*pow(w[k],2) + v[k-1]*pow(w[k-1],2))
        delta.append(pD)
    return delta

def spline(x, y, kind, k0t = 0, kNt=0, plot = True):
    N = len(x)
    C_matrix = np.zeros((N,4))
    k_matrix, w = splining(x,y,kind,k0t,kNt)
    if (kind == 'clamped'):
        new_k = np.zeros((N+1,))
        new_k[0] = k0t
        for j in range(0,len(k_matrix)):
            new_k[j+1] = k_matrix[j]
        new_k[N] = kNt
        k_matrix = new_k.copy()
    if (kind == 'periodic'):
        k_matrix = np.append(k_matrix, k_matrix[0])
    #Construir matriz C
    for line in range(0,N-1):
        v = y[line+1] - y[line]
        u = x[line+1] - x[line]
        C_matrix[line, 0] = y[line]
        C_matrix[line, 1] = k_matrix[line]*u
        C_matrix[line, 2] = 3*v - u*(2*k_matrix[line]+ k_matrix[line+1])
        C_matrix[line, 3] = u*(k_matrix[line] + k_matrix[line+1]) - 2*v
    #Constuir matriz A
    A_matrix = np.zeros((N-1,4))
    for line in range(0, N-1):
        A_matrix[line, 0] = C_matrix[line,0] - C_matrix[line,1]*x[line]*w[line]+ C_matrix[line,2]*(pow((x[line]*w[line]),2)) - C_matrix[line,3]*pow((x[line]*w[line]),3)
        A_matrix[line, 1] = w[line]*C_matrix[line,1] - 2*pow(w[line],2)*C_matrix[line,2]*x[line] + 3*pow(w[line],3)*C_matrix[line,3]*pow(x[line],2)
        A_matrix[line, 2] = pow(w[line],2)*C_matrix[line,2] - 3*pow(w[line],3)*C_matrix[line,3]*x[line]
        A_matrix[line, 3] = pow(w[line],3)*C_matrix[line,3]
    if plot == True:
        LINE_COLOR = 'b'
        MARKER_COLOR = 'k'
        #Funcao Lambda que retorna o valor do polinomial de X para o intervalo de xi->xi+1
        poly = lambda i, X: A_matrix[i,0] + A_matrix[i,1]*X + A_matrix[i,2]*pow(X,2) + A_matrix[i,3]*pow(X,3)
        interval_x = []
        interval_y = []
        shorts = 1000
        for z in range(0,len(x)-1):
            xi = x[z]
            interval_x.append(xi)
            interval_y.append(y[z])
            for k in range(1, shorts):
                X = xi + k*(x[z+1]-xi)/shorts
                interval_x.append(X)
                Y = poly(z, X)
                interval_y.append(Y)
        plt.plot(interval_x, interval_y, c = LINE_COLOR)
        plt.scatter(x,y, c=MARKER_COLOR, marker='X')
        plt.title('Spline using {0} borders'.format(kind))
        plt.legend([
            'Interpolation',
            'Numbers'
        ])
        plt.grid(axis ='both')
        plt.show()
    return (A_matrix)