# Implementacao Pilha baseada na List do Python

from lse import LSE, Nodo
import os
import time



class Pilha:
    def __init__(self):
        self.pilha = LSE() # lista interna

    def peek(self): # retorna qual item esta no topo
        if self.pilha.head is not None:
            return self.pilha.head.dado
        else:
            print('A lista se encontra vazia, tente adicionar um item.')
    
       
    def push(self, item): # metodo de inserir item
        self.pilha.inserir_inicio(Nodo(item))
        
    def pop(self): # remover o topo e retornar item para usuario
        if self.pilha.is_empty():
            print("Lista Vazia!")
            return None
        return self.pilha.remover_inicio().dado
                
    def is_empty(self): # teste se é vazia
        if len(self.pilha) > 0:
            return False
        return True
        
    def __len__(self): # retorna o total de itens
        return len(self.pilha)

    def __str__(self): # representacao da pilha como string
        return str(self.pilha)
    
    def delay(self):
        os.system('cls')
        time.sleep(2)
        
    
    
## TESTES ##


p = Pilha()

programa = True

while True: 
    
    menu = {
            'Menu': {
                'pergunta': '------------OPÇÕES------------',
                'opcoes': {
                    '(1)': 'ADICIONAR UM ITEM AO INICIO DO NODO',
                    '(2)': 'REMOVER O PRIMEIRO ITEM DO NODO',
                    '(3)': 'RETORNAR O PRIMEIRO ITEM',
                    '(4)': 'RETORNAR O NODO EM MODO DE VISUALIZAÇÃO',
                    '(5)': 'RETORNAR OS ITENS DO NODO',
                    '(0)': 'SAIR'
                }
            }
        }
    

    for chavePerg, chaveResp in menu.items():
        print(chaveResp['pergunta'])


        for respChave, respValor in chaveResp['opcoes'].items():
            print(f'{respChave}:{respValor}')

        respUsuario = input('Sua escolha: ')
        os.system('cls')
        
        try:
            respUsuario = int(respUsuario)
        except:
            print("VALOR INVÁLIDO. Escolha apenas entre '1', '2', '3', '4', '5' ou '0'.")
            time.sleep(3)
            os.system('cls')
            
        
    if respUsuario == 1:
        p.push(input('Digite algo a ser inserido no NODO: '))
        os.system('cls')
        
    elif respUsuario == 2:
        print(f'O item "{p.pop()}" foi removido com sucesso')
        time.sleep(2)
        
    elif respUsuario == 3:
        print(f'O primeiro item é: {p.peek()}')
        time.sleep(2)
    
    elif respUsuario == 4:
        print(f'Graficamente o NODO se parecia com isso:\n', p.__str__())
        time.sleep(2)
        
    elif respUsuario == 5:
        print(f'Segue o NODO criado: {p}')
        time.sleep(2)
    
    elif respUsuario == 0:
        print('Você optou por sair! Até logo.')
        break  
    
    else:
        print('Valor inválido')     
        
            
        
        
        
    

