import math

def inserir(fila, item, tamanho):
    tamanho += 1
    fila.append(item)

def remover(fila, tamanho, indice):
    fila.pop(indice)
    tamanha -= 1

def pai(indice):
    return math.floor(indice)
def esquerda(indice):
    return 2 * indice
def direita(indice):
    return (2 * indice) + 1

def heapfy (fila, indice):
    l = esquerda(indice)
    r = direita(indice)

    if(l <= len(fila) and fila[l] > fila[indice]):
        maior = l
    else:
        maior = indice

    if(r <= len(fila) and fila[r] > fila[maior]):
        maior = r
    if(maior != indice):
        swap(fila[indice], fila[maior])
        heapfy(fila, maior)

def swap(a,b):
    aux = a
    a = b
    b = aux
    return a,b


def constroi_heap (fila):
    i = math.floor(len(fila))
    for i in range (len(fila)//2-1, -1, -1):
        heapfy(fila,i)

    return fila


priority = [5, 55, 25, 1, 515]

heap = constroi_heap(priority)

c = len(priority)
print(inserir(heap, 35, c))

#print(heap)

#------------------------------------------------------------------

class FilaDePrioridade:

	def __init__(self):
		self._fila = []
		self._indice = 0

	def inserir(self, item, prioridade):
		heapq.heappush(self._fila, (-prioridade, self._indice, item))
		self._indice += 1

	def remover(self):
		return heapq.heappop(self._fila)[-1]


class Pessoa:
	def __init__(self, nome):
		self.nome = nome

	def __repr__(self):
		return self.nome


fila = FilaDePrioridade()
fila.inserir(Pessoa('Maria'), 20)
fila.inserir(Pessoa('Pedro'), 16)
fila.inserir(Pessoa('Felipe'), 25)
fila.inserir(Pessoa('Carol'), 23)