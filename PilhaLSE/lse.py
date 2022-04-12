class Nodo:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None

    def __str__(self):
        return str(self.dado)

# ##############################
# Lista Simplesmente Encadeada
# [NODO] => [NODO] => None
class LSE:
    def __init__(self):
        self.head = None  # cabeca | inicio
        self.tail = None  # cauda  | fim
        self.tam = 0  # quantidade de elementos

    def is_empty(self):  # retorna se a lista esta vazia
        if self.tam == 0 or self.head is None or self.tail is None:
            return True
        return False

    def inserir_fim(self, novo):  # similar ao append da List
        self.tam += 1
        if self.is_empty():
            # lista vazia
            self.head = novo
            self.tail = novo
        else:
            # ja possui itens
            ## o tail atual deve apontar para o novo
            ## o tail sera atribuido para o novo
            self.tail.proximo = novo
            self.tail = novo

    def inserir_inicio(self, novo):  # similar ao insert(0,item) da List
        if self.head is None and self.tail is None:
            # lista vazia
            self.head = novo
            self.tail = novo
        else:
            novo.proximo = self.head
            self.head = novo

        self.tam += 1

    def remover_inicio(self):
        if self.is_empty():
            print('Lista Vazia!')
            return

        self.tam -= 1  # diminui o contador de itens

        ## quando temos apenas 1 item
        if (self.head == self.tail):
            removido = self.head
            self.head = None
            self.tail = None

        # lista possui + de 1 item
        else:
            removido = self.head
            self.head = self.head.proximo
            removido.proximo = None

        return removido

    def remover_fim(self):
        if self.is_empty():
            print('Lista Vazia!')
            return

        ## precisamos descobrir quem eh o penultimo da lista!!
        removido = None
        item = self.head
        while (item != None):
            # quando tem apenas 1 item
            if (item == self.tail and item == self.head):
                self.head = None
                self.tail = None
                self.tam -= 1
                return item

            # quando tem mais de 1
            if (item.proximo != None and item.proximo == self.tail):
                removido = self.tail
                self.tail = item
                item.proximo = None
                self.tam -= 1
                return removido

            item = item.proximo

    def buscar(self, valor):  # retorna um Nodo
        if self.is_empty():
            print('Lista Vazia')
            return

        item = self.head
        while (item != None):
            if item.dado == valor:
                return item

            item = item.proximo

    def imprimir(self):
        if (self.head is None and self.tail is None):
            print('Lista Vazia')
            return

        item = self.head
        while (item != None):
            print(item)
            item = item.proximo

    def imprimir_lado(self):
        saida = ''
        item = self.head
        while (item != None):
            if item == self.head:
                saida += '[' + str(item) + ']'
            else:
                saida += ' => ' + '[' + str(item) + ']'
            item = item.proximo
        print(saida)

    def __contains__(self, valor):  ## para poder utilizar o IN, retorna boolean
        item = self.head
        while (item != None):
            if item.dado == valor:
                return True

            item = item.proximo

        return False

    def __len__(self):
        return self.tam

    def __str__(self):
        saida = ''
        item = self.head
        while (item != None):
            if item == self.head:
                saida += '[' + str(item) + ']'
            else:
                saida += ' => ' + '[' + str(item) + ']'
            item = item.proximo

        return saida

    def limpar(self):
        while(self.tam >= 0):
            self.remover_inicio()

    def get(self, posicao):
        
        contador = 0
        
        item = self.head
        while (item != None):
            if(posicao == contador):
                return item

            contador += 1
            item = item.proximo


    def para_lista(self):
        lista = []
        item = self.head
        
        while (item != None):
            lista.append(item).dado
            item = item.proximo

        return lista















