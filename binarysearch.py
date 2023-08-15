# algoritmo de busca binaria, o target = alvo sera um valor aleatorio
# e o codigo compara os dois algoritmos de busca e suas eficiencias

import time
from random import randint

# gerar uma lista com mil numeros

lista = []
for c in range(50000):
    lista.append(c)


# forma de pesquisa de 1 em 1 e contando seu tempo de execução

start = time.time()
for target in lista:
    def search_naive(i, target):
        for i in range(len(lista)):
            if lista[i] == target:
                return i
        return -1
end = time.time()
print("O tempo de execução do primeiro algoritmo foi de :", (end - start))

# forma de pesquisa binaria
start = time.time()
for target in lista:
    def binary_search(lista, target, low=None, high=None):
        if low is None:
            low = 0
        if high is None:
            high = len(lista)-1
        if high < low:
            return -1

        midpoint = (low + high) // 2
        if lista[midpoint] == target:
            return midpoint
        elif target < lista[midpoint]:
            return binary_search(lista, target, low, midpoint-1)
        else:
            target > lista[midpoint]
            return binary_search(lista, target, midpoint+1, high)
end = time.time()
print("O tempo de execução da busca binaria foi de :", (end - start))


if __name__ == '__main__':

    target = randint(0, 10000)
    print("o alvo da busca é {}".format(target))
    print(search_naive(lista, target))
    print(binary_search(lista, target))
