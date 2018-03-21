import numpy as np

def sample_1(N):
    """
    Numeros asociados a una probabilidad
    N es el numero de valores evaluados
    """
    return np.random.choice([-10, -5, 3, 9], N, p=[0.1, 0.4, 0.2, 0.3])

def sample_2(N):
    """
    Distribucion exponencial
    N es el numero de valores evaluados
    """
    return np.random.exponential(0.5, N)

def get_mean(sampling_fun, N, M):
    """
    Obtiene M promedios para sampling_fun evaluada en N valores
    """
    ans = []
    for m in range(M):
        ans.append(np.mean(sampling_fun(N)))
    return np.asarray(ans)


M = 10000
N = [10, 100, 1000]
samples = [sample_1, sample_2]

for sample in samples:
    for n in N:
        name = sample.__name__ + '_' + str(n)+ '.txt'
        np.savetxt(name, get_mean(sample, n, M) )

