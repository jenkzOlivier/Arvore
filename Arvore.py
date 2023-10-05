# Define uma classe No que representa um nó em uma árvore binária
class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

# Define a classe ArvoreBinaria para representar a árvore binária
class ArvoreBinaria:
    def __init__(self):
        self.raiz = None  # Inicializa a raiz da árvore como None (vazia)

    # Método para inserir um valor na árvore binária
    def inserir(self, valor):
        self.raiz = self._inserir_recursivamente(self.raiz, valor)

    # Método auxiliar para inserir um valor de forma recursiva
    def _inserir_recursivamente(self, no, valor):
        if no is None:
            return No(valor)  # Se o nó atual for None, cria um novo nó com o valor
        if valor < no.valor:
            no.esquerda = self._inserir_recursivamente(no.esquerda, valor)  # Insere na subárvore esquerda
        elif valor > no.valor:
            no.direita = self._inserir_recursivamente(no.direita, valor)  # Insere na subárvore direita
        return no

    # Método para imprimir os valores da árvore em ordem
    def imprimir(self):
        self._imprimir_recursivamente(self.raiz)

    # Método auxiliar para imprimir os valores em ordem de forma recursiva
    def _imprimir_recursivamente(self, no):
        if no is not None:
            self._imprimir_recursivamente(no.esquerda)  # Imprime os valores da subárvore esquerda
            print(no.valor)  # Imprime o valor do nó atual
            self._imprimir_recursivamente(no.direita)  # Imprime os valores da subárvore direita

    # Métodos semelhantes para percorrimento em pré-ordem e pós-ordem

    # Método para buscar um valor na árvore
    def buscar(self, valor):
        return self._buscar_recursivamente(self.raiz, valor)

    # Método auxiliar para buscar um valor de forma recursiva
    def _buscar_recursivamente(self, no, valor):
        if no is None:
            return False  # Se o nó atual for None, o valor não foi encontrado
        if valor == no.valor:
            return True  # Se o valor for igual ao valor do nó atual, ele foi encontrado
        elif valor < no.valor:
            return self._buscar_recursivamente(no.esquerda, valor)  # Busca na subárvore esquerda
        else:
            return self._buscar_recursivamente(no.direita, valor)  # Busca na subárvore direita

    # Métodos para encontrar o maior e o menor valor na árvore

    # Método para calcular a soma de todos os valores na árvore
    def soma_valores(self):
        return self._soma_valores_recursivamente(self.raiz)

    # Método auxiliar para calcular a soma de valores de forma recursiva
    def _soma_valores_recursivamente(self, no):
        if no is None:
            return 0  # Se o nó atual for None, a soma é zero
        return no.valor + self._soma_valores_recursivamente(no.esquerda) + self._soma_valores_recursivamente(no.direita)

    # Métodos para contar o número de nós e folhas na árvore

    # Método para contar o número de nós na árvore
    def contar_nos(self):
        return self._contar_nos_recursivamente(self.raiz)

    # Método auxiliar para contar o número de nós de forma recursiva
    def _contar_nos_recursivamente(self, no):
        if no is None:
            return 0  # Se o nó atual for None, não há nós a serem contados
        return 1 + self._contar_nos_recursivamente(no.esquerda) + self._contar_nos_recursivamente(no.direita)

    # Método para contar o número de folhas na árvore
    def contar_folhas(self):
        return self._contar_folhas_recursivamente(self.raiz)

    # Método auxiliar para contar o número de folhas de forma recursiva
    def _contar_folhas_recursivamente(self, no):
        if no is None:
            return 0  # Se o nó atual for None, não há folhas a serem contadas
        if no.esquerda is None and no.direita is None:
            return 1  # Se o nó atual não tem filhos, é uma folha
        return self._contar_folhas_recursivamente(no.esquerda) + self._contar_folhas_recursivamente(no.direita)

    # Método para calcular a altura da árvore
    def altura(self):
        return self._altura_recursivamente(self.raiz)

    # Método auxiliar para calcular a altura da árvore de forma recursiva
    def _altura_recursivamente(self, no):
        if no is None:
            return 0  # Se o nó atual for None, a altura é zero
        altura_esquerda = self._altura_recursivamente(no.esquerda)
        altura_direita = self._altura_recursivamente(no.direita)
        return max(altura_esquerda, altura_direita) + 1

    # Método para calcular a média dos valores na árvore
    def media(self):
        if self.raiz is None:
            return None  # Se a árvore estiver vazia, a média não pode ser calculada
        soma = self.soma_valores()
        num_nos = self.contar_nos()
        return soma / num_nos  # Calcula a média como a soma dividida pelo número de nós
    
    # Método para calcular a soma de todos os valores na árvore
def soma_valores(self):
    return self._soma_valores_recursivamente(self.raiz)

# Método auxiliar para calcular a soma de valores de forma recursiva
def _soma_valores_recursivamente(self, no):
    if no is None:
        return 0  # Se o nó atual for None, a soma é zero
    return no.valor + self._soma_valores_recursivamente(no.esquerda) + self._soma_valores_recursivamente(no.direita)

# Método para contar o número de nós na árvore
def contar_nos(self):
    return self._contar_nos_recursivamente(self.raiz)

# Método auxiliar para contar o número de nós de forma recursiva
def _contar_nos_recursivamente(self, no):
    if no is None:
        return 0  # Se o nó atual for None, não há nós a serem contados
    return 1 + self._contar_nos_recursivamente(no.esquerda) + self._contar_nos_recursivamente(no.direita)

# Método para contar o número de folhas na árvore
def contar_folhas(self):
    return self._contar_folhas_recursivamente(self.raiz)

# Método auxiliar para contar o número de folhas de forma recursiva
def _contar_folhas_recursivamente(self, no):
    if no is None:
        return 0  # Se o nó atual for None, não há folhas a serem contadas
    if no.esquerda is None and no.direita is None:
        return 1  # Se o nó atual não tem filhos, é uma folha
    return self._contar_folhas_recursivamente(no.esquerda) + self._contar_folhas_recursivamente(no.direita)

# Método para calcular a altura da árvore
def altura(self):
    return self._altura_recursivamente(self.raiz)

# Método auxiliar para calcular a altura da árvore de forma recursiva
def _altura_recursivamente(self, no):
    if no is None:
        return 0  # Se o nó atual for None, a altura é zero
    altura_esquerda = self._altura_recursivamente(no.esquerda)
    altura_direita = self._altura_recursivamente(no.direita)
    return max(altura_esquerda, altura_direita) + 1

# Exemplo de uso:
arvore = ArvoreBinaria()
arvore.inserir(10)
arvore.inserir(5)
arvore.inserir(15)
arvore.inserir(3)
arvore.inserir(7)
arvore.inserir(12)
arvore.inserir(18)

print("Valores na árvore:")
arvore.imprimir()

print("\nValores na árvore (pré-ordem):")
arvore.imprimir_pre_ordem()

print("\nValores na árvore (pós-ordem):")
arvore.imprimir_pos_ordem()

valor = 15
if arvore.buscar(valor):
    print(f"\nO valor {valor} está presente na árvore.")
else:
    print(f"\nO valor {valor} não está presente na árvore.")

print(f"\nMaior valor na árvore: {arvore.encontrar_maior()}")
print(f"Menor valor na árvore: {arvore.encontrar_menor()}")
print(f"Média dos valores na árvore: {arvore.media()}")
print(f"Soma dos valores na árvore: {arvore.soma_valores()}")
print(f"Número de nós na árvore: {arvore.contar_nos()}")
print(f"Número de folhas na árvore: {arvore.contar_folhas()}")
print(f"Altura da árvore: {arvore.altura()}")