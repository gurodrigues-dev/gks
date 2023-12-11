#!/usr/bin/env python3

import argparse
import subprocess
import json
import sys
import os

def obter_namespace_do_pod(nome_do_pod):
    comando = ["kubectl", "get", "pods", "-A", "-o", "json"]

    try:
        resultado = subprocess.run(comando, check=True, capture_output=True)
        saida_json = resultado.stdout.decode("utf-8")
        dados_json = json.loads(saida_json)

        for item in dados_json.get("items", []):
            metadata = item.get("metadata", {})
            nome_pdo_atual = metadata.get("name", "")
            namespace = metadata.get("namespace", "")

            if nome_pdo_atual == nome_do_pod:
                return namespace

        return None
    except subprocess.CalledProcessError as e:
        print("Erro ao executar o comando:", e)
        print("Saída de erro:", e.stderr.decode("utf-8"))
        sys.exit(1)

def encontrar_e_descrever_pod(nome_do_pod):
    namespace = obter_namespace_do_pod(nome_do_pod)

    if namespace is not None:
        comando = ["kubectl", "describe", "pod", nome_do_pod, "-n", namespace]
        try:
            resultado = subprocess.run(comando, check=True, capture_output=True)
            saida = resultado.stdout.decode("utf-8")

            indice_inicio = saida.find("Containers:")
            if indice_inicio != -1:
                container_info_linha = [linha for linha in saida[indice_inicio:].splitlines() if linha.startswith("  ")][0]
                container_nome = container_info_linha.strip().split()[0]
                container_nome = container_nome[:-1]
                return container_nome
            
            return None
        except subprocess.CalledProcessError as e:
            print("Erro ao executar o comando:", e)
            print("Saída de erro:", e.stderr.decode("utf-8"))
            sys.exit(1)
    else:
        print(f"O pod {nome_do_pod} não foi encontrado.")

def verificar_logs_do_container(nome_do_pod):
    container_nome = encontrar_e_descrever_pod(nome_do_pod)
    namespace = obter_namespace_do_pod(nome_do_pod)

    if container_nome is not None and namespace is not None:
        comando_logs = f"kubectl logs {nome_do_pod} -c {container_nome} -n {namespace} -f"
        os.system(comando_logs)

def main():
    parser = argparse.ArgumentParser(description="Obter informações de um pod, seu namespace e nome do container")
    parser.add_argument("-cpn", "--check-pod-namespace", dest="nome_do_pod",
                        help="Verificar o namespace de um pod")

    parser.add_argument("-fcp", "--find-container-pod", dest="nome_do_pod_descricao",
                        help="Encontrar e descrever um pod")
    
    parser.add_argument("-ccp", "--check-container-pod", dest="nome_do_pod_logs",
                        help="Verificar os logs de um container em um pod")

    args = parser.parse_args()

    if args.nome_do_pod_descricao:
        encontrar_e_descrever_pod(args.nome_do_pod_descricao)

    elif args.nome_do_pod:
        nome_do_pod = args.nome_do_pod
        namespace = obter_namespace_do_pod(nome_do_pod)

        if namespace is not None:
            print(f"O namespace do pod {nome_do_pod} é: {namespace}")
        else:
            print(f"O pod {nome_do_pod} não foi encontrado.")

    elif args.nome_do_pod_logs:
        verificar_logs_do_container(args.nome_do_pod_logs)

    else:
        print("Olá! Parece que nenhum argumento foi passado, por gentileza passe alguma flag como parametro, ou então. Digite gcut -h ou gcut --help para verificar o manual de instruções")

if __name__ == "__main__":

    print("""
   ________ _______
  / ____/ //_/ ___/
 / / __/ ,<  \__ \ 
/ /_/ / /| |___/ / 
\____/_/ |_/____/  
                   
""")

    main()
