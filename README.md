![Logo do Projeto](./assets/logo-spawn2.png)
 
## TCP-Chat-Room
 
Um programa usando socket tcp, que funciona para comunicacao <br> de chat entre clientes que entram em um servidor.
 
 
## Tecnologias: 
 
Aqui estao as tecnologias usadas nesse projeto
 
* Python  3.9.5
* Prompt de comando
 
 
## Servicos usados:
 
* Github 


## Comecando:
 
* Primeiro rodar o arquivo server:
* Abrir o cmd e digitar:
>    cd endereco de onde esta a pasta
* Rodar o arquivo servidor:
>    python server.py
* Depois rodar o arquivo cliente:
>    python client.py
* Agora eh so abrir mais quantos clientes quiser e comecar a comunicacao
 
## Como utilizar:
 
![](./assets/Screenshot_1.jpg)

* O primeiro cmd eh o server, e os dois de baixo sao os clientes logados no server!!!

* Primeiro passo eu abri tres cmds(Prompt de comando), para todos deve se localizar a pasta onde esta os arquivos server.py e client.py.  
* Nesse caso eu copiei o endereco da pasta onde estava os arquivos e dei o comando "cd C:\Users\kayqu\python\TCP-Chat-Room-Python"). 
* Em seguida ja estando na pasta, eh preciso primeiro abrir o arquivo server.py com o comando "python server.py no cmd", abrindo o servidor vc vai receber a mensagem "Servidor esta rodando ..." 
* Agora eh abrir os clientes, entao para cada cmd de baixo eh so digitar o comando "python client.py", ai vc vai receber a mensagem "Escolha um nick para voce >>>".
* Logo depois de escolher o nick voce entrara no servidor, e quem ja estiver la vai receber uma mensagem dizendo que vc se conectou no servidor, e para voce vai aparecer a mensagem "Voce esta conectado ao servidor".
* Pronto agora eh so outro cliente se conectar da mesma forma que esse passo a passo e voces poderam conversar pelo servidor!!!

 
 
## Protocolo da Aplicacao:

![](./assets/Screenshot_2.jpg)
 
1.  O socket usado foi o tcp/ip pois possui suas funções divididas em camada da mesma forma que o OSI. A diferença principal nestas estruturas é o número de camadas encontradas em cada modelo: no OSI encontramos 7 camadas, enquanto no TCP/IP somente 4: Aplicação, Transporte, Rede e Interface de rede.

4. Camada Aplicação:
* A camada de aplicação é o topo da arquitetura TCP/IP, tratada de forma monolítica, onde são realizadas a maior parte das requisições para execução de tarefas na rede. Ela faz a comunicação entre os programas e os protocolos de transporte e é responsável por tudo que está relacionado aos serviços de comunicação que visam a interação junto ao usuário.
* O protocolo da aplicacao usado foi o AF_INET(IPv4) que usa o Ip e a porta http.
* codigo: 
 ~~~python
 # No programa servidor:
 '''
 O que acontece no lado do servidor Web é um pouco mais complexo. Primeiro, o Servidor Web cria um “soquete tipo servidor”:
 
 Algumas coisas que deves observar: usamos server.bind(('127.0.0.1', 80)) que eh soquete do tipo “servidor”, mas esse so esta visível dentro do computador em que está sendo executado. server.bind(('127.0.0.1', 80)) determina que o soquete estará acessível por qualquer computador que possuas o endereço IP do computador.
 Ja o socket.gethostname() eh usado para que o soquete esteja visível ao mundo exterior.

Uma segunda coisa que precisas observar é: as portas baixas, normalmente estão reservadas para serviços “bem conhecidos”, tais como (HTTP, SNMP etc). Como essa eh apenas uma atividade de redes, utilizei um número baixo (80).

Por fim, o argumento “listen” diz à biblioteca de soquetes que queremos enfileirar no máximo 5 requisições de conexão (normalmente o máximo) antes de recusar começar a recusar conexões externas. Caso o resto do código esteja escrito corretamente, isso deverá ser o suficiente.

 
 '''
 import socket

 # setando o host ip e a porta http para o servidor rodar
 host = '127.0.0.1'
 port = 55555

 # configuracao do servidor

 # criando um servidor objeto
 server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 # ligando(bind) o servidor ao host e a porta
 server.bind((host, port))
 '''para o cliente A mandar mensagem para o cliente B ele primeiro manda a 
 mensagem para o servidor que vai fazer esse intermediacao dessa comunicacao'''
 # ativar o modo de escuta para todas as conexões de entrada para o servidor
 server.listen()
 
 # No programa cliente:
 '''
Quando a connect (conexão) foi estabelecida, o soquete client pode ser utilizado para enviar uma solicitação de texto para a página. O mesmo soquete é que irá ler a resposta e, em seguida, o mesmo será destruído. Isso mesmo, será destruído. Os soquetes de Clientes normalmente são usados apenas numa única transação (troca) (ou um pequeno conjunto sequencial de transações).
 '''
 import socket

 # entrada do nick do cliente
 alias = input('Escolha um nick para voce >>> ')
 # criando um objeto cliente
 client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 # conectando o cliente ao local host e a porta http respectivamente
 client.connect(('127.0.0.1', 55555))
 
 ~~~
3. Camada de Transporte


2. dsa



1. dsada
  
  
 
 
## Links
 
  - Link of deployed application: (if has been deployed)
  - Repository: https://link_of_repository
    - In case of sensitive bugs like security vulnerabilities, please contact
      YOUR EMAIL directly instead of using issue tracker. We value your effort
      to improve the security and privacy of this project!
 
 
## Versioning
 
1.0.0.0
 
 
## Authors
 
* **KAYQUE MOREIRA**: @Kaymoreira (https://github.com/Kaymoreira)
 
 
Please follow github and join us!
Thanks to visiting me and good coding!



