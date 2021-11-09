# CHAT ROOM CLIENT
# Aluno: Kayque Costa Moreira

import threading
import socket

# entrada do nick do cliente
alias = input('Escolha um nick para voce >>> ')
# criando um objeto cliente
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# conectando o cliente ao local host e a porta respectivamente
client.connect(('127.0.0.1', 80))

"""Criar duas funcoes para duas tarefas(threads), uma para receber mensagens de 
outros clientes pelo servidor, e a outra funcao para enviar mensagens para outros 
clientes pelo servidor! """


# funcao para receber mensagens de outros clientes pelo servidor
def client_receive():
    while True:
        try:
            msg = client.recv(1024).decode('utf-8')
            # se a msg for igual a 'alias?' que foi definido la no server.py
            if msg == 'alias?':
                # entao vmos enviar o alias que eh o input alias la do escolha um nick
                client.send(alias.encode('utf-8'))
            else:
                # caso nao seja iremos printar qualquer q seja a msg mandada pelo servidor
                print(msg)
                # tratando os erros e fechando o cliente
        except:
            print('Error!')
            client.close()
            break


# funcao para enviar mensagens para outros clientes pelo servidor
def client_send():
    while True:
        # como vai ficar a mensagem (seunick: mensagem que digitou)
        msg = f'{alias}: {input("")}'
        # mandando a mensagem
        client.send(msg.encode('utf-8'))


""" Criando e startando duas threads(tarefas), uma para receber mensagens 
e uma para enviar mensagens"""
receive_thread = threading.Thread(target=client_receive)
receive_thread.start()

send_thread = threading.Thread(target=client_send)
send_thread.start()

# encode vai com o envio, e decode vai com o recebimento
