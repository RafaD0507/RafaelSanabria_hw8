import numpy as np
import matplotlib.pyplot as plt

def normal_dist(x, mean, sigma):
    """Distribucion normal
    x valor a evaluar en la distribucion
    mean promedio para la distribucion
    sigma desviacion estandar para la distribucion
    retorna la funcion evaluada en x
    """
    return (1/(2*np.pi*sigma**2))*np.exp(-(x-mean)**2/sigma**2)

def get_fit(filename):
    '''Grafica el histograma y ajuste de los datos en filename
    filename datos del sample
    '''
    data = np.loadtxt(filename)
    plt.figure()
    plt.hist(data)
    plt.savefig(filename[:-3]+'png')
    plt.close()

fs = ['sample_1', 'sample_2']
N = [10, 100, 1000]

for f in fs:
    #recorre los samples
    for n in N:
        #recorre los Ns
        name = f+'_'+str(n)+'.txt'
        get_fit(name)
