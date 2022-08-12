<h1 align="center"> 🍐 FREXCO DEVOPS 🍐 </h1>
Aplicação API em Django com PostgreSQL, utilizando containers Docker e Docker-Compose, disparando via Pipeline CI/CD com GitHub Actions 
<p align="center"> <img src=".github/workflows/docker-githubactions.png" /> </p>

## Objetivo do Desafio:
• Criar um script Vagrant que suba uma máquina CentOS 7.x com 2 CPUs (2 cores de processador), 4 GB de memória RAM e 50gb de HD chamada “teste-zeppelin”. O acesso a ela deve ser através de uma chave privada, não com senha.

• Criar um programa em python que faça a instalação do Java e do Apache Zeppelin nessa máquina recém criada. Além disso, o programa deve subir o webserver do Zeppelin na porta 8888 e fazer uma criação de usuários a partir da lista presente no arquivo Lista_Usuarios_Zeppelin.txt.

• Com base no teste anterior, criar um script Python que faça a instalação do Python 3.6 e do Apache Superset na máquina Centos 7 criada e suba o webserver do Superset.

• Adicionar ao script Python a instalação do MySQL (ou banco de dados semelhante) e a integração dele com o Superset.

• Fazer a instalação do Redis, conectá-lo ao Superset e colocar isso no código Python.

## Resumo:
✅ Todos objetivos cumpridos 

✅ Um comando executa toda infraestrutura

✅ Necessario apenas vagrant instalado na maquina local 

## Construção e Desenvolvimento:
✌️ 1. Criado Vagrantfile que sobe uma VM com 4GB de RAM, 2 CPUs, 50GB HD, executando script (master.sh).

🐍 2. Criado scripts em Python que executam: criacao de usuarios linux com senhas e roles definidas, instalacao do Java, Apache Zeppelin, MySQL e Apache Superset.

$ 3. Script que executa toda a infraestrura (one-script-to-rule-them-all.sh)

## Como efetuar o Deploy:
✌️ 1. Ter o Vagrant instalado na maquina local.

✌️ 2. Seguintes comandos: vagrant up, vagrant ssh, em seguida logar como root na vm, sudo su.

💍 3. Ir ate o diretorio /vagrant e executar o script ./one-script-to-rule-them-all.sh

## Imagens:

1. Webserver Apache Zeppelin rodando na porta solicitada (8888)
2. Webserver Apache Superset rodando na porta 8088, com MySQL.
