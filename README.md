# gks - Gustavo Kubernetes Service

O GKS, é um CLI (Command Line Interface) utilizado para facilitar suas buscas no Kubernetes. Em princípio ele surgiu, com a dificuldade de ver logs de um container dentro de um pod. Não com a dificuldade em si, mas sim com a demora.

Agora com um simples comando, apenas passando o nome do pod, você consegue ver os logs do container dentro dele de maneira veloz.

Além disso, você também pode:

> Descobrir de maneira mais rápida:

- namespace de um pod
- container dentro de um pod

#### Requisitos

- `kubectl` ou `minikube`
- Python 3

# Como Usar

1. Primeiro faça o clone do repositório.

`https://github.com/gurodrigues-dev/gks.git` ou `https://github.com/gurodrigues-dev/gks.git` 

2. Dê permissão ao `installer.sh`.

`chmod u+x installer.sh`

3. Rode o installer.sh com sudo.

`sudo ./installer.sh`

4. Feito! Pronto para uso