def inserir_vertice(grafo, vertice):
    if vertice not in grafo:
        grafo[vertice] = []


def inserir_aresta(grafo, origem, destino, nao_direcionado=False):
    inserir_vertice(grafo, origem)
    inserir_vertice(grafo, destino)

    if destino not in grafo[origem]:
        grafo[origem].append(destino)

    if nao_direcionado and origem not in grafo[destino]:
        grafo[destino].append(origem)


def vizinhos(grafo, vertice):
    if vertice in grafo:
        return grafo[vertice]
    return []


def listar_vizinhos(grafo, vertice):
    if vertice not in grafo:
        print(f"O vértice {vertice} não existe.")
        return []
    lista = vizinhos(grafo, vertice)
    print(f"Vizinhos de {vertice}: {lista}")
    return lista


def exibir_grafo(grafo):
    print("\nLista de Adjacência:")
    for vertice in grafo:
        print(f"{vertice} -> {grafo[vertice]}")


def remover_aresta(grafo, origem, destino, nao_direcionado=False):
    if origem not in grafo:
        return

    if destino in grafo[origem]:
        grafo[origem].remove(destino)

    if nao_direcionado and destino in grafo:
        if origem in grafo[destino]:
            grafo[destino].remove(origem)


def remover_vertice(grafo, vertice, nao_direcionado=True):
    if vertice not in grafo:
        print(f"O vértice {vertice} não existe.")
        return False

    for outro in grafo:
        if vertice in grafo[outro]:
            grafo[outro].remove(vertice)

    del grafo[vertice]
    print(f"Vértice {vertice} removido.")
    return True


def existe_aresta(grafo, origem, destino):
    if origem not in grafo:
        return False
    return destino in grafo[origem]


def grau_vertices(grafo):
    graus = {}
    for vertice in grafo:
        graus[vertice] = {"saida": 0, "entrada": 0, "total": 0}

    for u in grafo:
        graus[u]["saida"] = len(grafo[u])
        for v in grafo:
            if u in grafo[v]:
                graus[u]["entrada"] += 1

    for vertice in graus:
        graus[vertice]["total"] = graus[vertice]["entrada"] + graus[vertice]["saida"]

    return graus


def percurso_valido(grafo, caminho):
    if len(caminho) < 2:
        return True

    for i in range(len(caminho) - 1):
        origem = caminho[i]
        destino = caminho[i + 1]
        if not existe_aresta(grafo, origem, destino):
            return False

    return True


def main():
    grafo = {
        "SP":  ["RJ", "BH"],
        "RJ":  ["BH"],
        "BH":  ["SSA"],
        "SSA": ["SP"],
        "CWB": ["SP"],
    }
    nao_direcionado = False

    while True:
        print("\n===== MENU - LISTA DE ADJACÊNCIA =====")
        print("1 - Mostrar o grafo")
        print("2 - Inserir vértice")
        print("3 - Inserir aresta")
        print("4 - Remover vértice")
        print("5 - Remover aresta")
        print("6 - Verificar se existe aresta")
        print("7 - Listar vizinhos")
        print("8 - Grau dos vértices")
        print("9 - Verificar percurso")
        print("0 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            exibir_grafo(grafo)
        elif opcao == "2":
            v = input("Nome do vértice: ")
            inserir_vertice(grafo, v)
            print(f"Vértice {v} inserido.")
        elif opcao == "3":
            o = input("Origem: ")
            d = input("Destino: ")
            inserir_aresta(grafo, o, d, nao_direcionado)
            print(f"Aresta {o} -> {d} inserida.")
        elif opcao == "4":
            v = input("Vértice a remover: ")
            remover_vertice(grafo, v, nao_direcionado)
        elif opcao == "5":
            o = input("Origem: ")
            d = input("Destino: ")
            remover_aresta(grafo, o, d, nao_direcionado)
            print(f"Aresta {o} -> {d} removida (se existia).")
        elif opcao == "6":
            o = input("Origem: ")
            d = input("Destino: ")
            if existe_aresta(grafo, o, d):
                print(f"Existe aresta {o} -> {d}.")
            else:
                print(f"Não existe aresta {o} -> {d}.")
        elif opcao == "7":
            v = input("Vértice: ")
            listar_vizinhos(grafo, v)
        elif opcao == "8":
            graus = grau_vertices(grafo)
            for v in graus:
                print(f"{v}: saída={graus[v]['saida']}, entrada={graus[v]['entrada']}, total={graus[v]['total']}")
        elif opcao == "9":
            caminho = input("Digite o caminho separado por espaço (ex: SP RJ BH): ").split()
            if percurso_valido(grafo, caminho):
                print("Percurso válido!")
            else:
                print("Percurso inválido!")
        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida!")


if __name__ == "__main__":
    main()
