# CHAT ROOM SERVER
# Aluno: Kayque Costa Moreira

import threading
import socket

# setando o host ip e a porta para o servidor rodar
host = '127.0.0.1'
port = 80

# configuracao do servidor

# criando um servidor objeto
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# ligando(bind) o servidor ao host e a porta
server.bind((host, port))
'''para o cliente A mandar mensagem para o cliente B ele primeiro manda a 
mensagem para o servidor que vai fazer esse intermediacao dessa comunicacao'''
# ativar o modo de escuta para todas as conexões de entrada para o servidor
server.listen()

# Criando lista de clientes e nicks
clients = []
aliases = []


# Funcao que manda mensagem do servidor para todos clientes conectados
def broadcast(msg):
    # iremos iterar através da lista de clientes, e para cada cliente enviamos esta mensagem
    for client in clients:
        client.send(msg)


# Funcao para cuidar de cada conexao de cada cliente
def handle_client(client):
    while True:
        try:  # mensagem vai ser igual a mensagem recebida do cliente
            msg = client.recv(1024)
            '''se a mensagem for recebida com sucesso do cliente, a funcao broadcast para 
            mandar essa mensagem para todos os outros clientes '''
            broadcast(msg)
        except:
            ''' em caso de falhas ou erros de conexao, precisamos identificar o cliente que 
            iremos derrubar da lista de clientes e do servidor '''
            # o index vai achar a tupla no nosso caso o cliente
            index = clients.index(client)
            # remocao do cliente da lista de clientes
            clients.remove(client)
            # encerra a conexao do cliente com o servidor
            client.close()
            # fazendo a mesma coisa para o apelido do cliente
            alias = aliases[index]
            # avisa ao servidor que o cliente de tal nickname acabou de sair do servidor
            broadcast(f'{alias} acabou de sair do chat!'.encode('utf-8'))
            # remove o nick da lista de nicks
            aliases.remove(alias)
            # quebra o loop
            break


# Funcao principal para receber a conexao dos clientes
def receive():
    while True:
        # avisando que o servidor esta rodando e ouvindo conexoes
        print('Servidor esta rodando ...')
        # servidor apto para aceitar qualquer conexao que venha a surgir
        client, address = server.accept()
        # printando a mensagem que a conexao foi estabelecida
        print(f'conexao estabelecida com {str(address)}')
        # agora nos mandamos para o cliente alguma palavra(alias?) para falar a ele qual o alias
        client.send('alias?'.encode('utf-8'))
        # criar o alias baseado na informacao recebida do cliente
        alias = client.recv(1024)
        # acrescentando o apelido a lista de apelidos
        aliases.append(alias)
        # acrescentando o cliente a lista de clientes
        clients.append(client)
        # mostrar mensangem retornando ao cliente qual eh o apelido dele
        print(f'O apelido dele eh  {alias}'.encode('utf-8'))
        # usar a funcao broadcast para mostrar a todos os clientes online que esse cliente entrou no chat room
        broadcast(f'{alias} esta conectado ao chat'.encode('utf-8'))
        # mandar uma mensagem do servidor para esse cliente falando que agora ele esta conectado
        client.send('Voce esta conectado ao servidor!'.encode('utf-8'))

        """ criando e startando a thread(tarefa) objeto que vai ser responsavel por rodar uma 
            thread individual para cada cliente de forma que as threads funcionem ao mesmo tempo
            dessa forma quando o cliente A, mandar mensagem para o cliente B, a comunicacao acontecera
            instantaneamente gracas a esse recurso chamado multi threading do python"""

        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()


# inciando a funcao receive
if __name__ == "__main__":
    receive()
