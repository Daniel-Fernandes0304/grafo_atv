def inserir_vertice(vertices, vertice):
    if vertice not in vertices:
        vertices.append(vertice)


def inserir_aresta(vertices, arestas, origem, destino, nao_direcionado=False):
    inserir_vertice(vertices, origem)
    inserir_vertice(vertices, destino)

    if [origem, destino] not in arestas:
        arestas.append([origem, destino])

    if nao_direcionado and [destino, origem] not in arestas:
        arestas.append([destino, origem])


def remover_aresta(arestas, origem, destino, nao_direcionado=False):
    if [origem, destino] in arestas:
        arestas.remove([origem, destino])

    if nao_direcionado and [destino, origem] in arestas:
        arestas.remove([destino, origem])


def remover_vertice(vertices, arestas, vertice):
    if vertice not in vertices:
        print(f"O vértice {vertice} não existe.")
        return

    vertices.remove(vertice)

    i = 0
    while i < len(arestas):
        if arestas[i][0] == vertice or arestas[i][1] == vertice:
            arestas.pop(i)
        else:
            i += 1

    print(f"Vértice {vertice} removido.")


def existe_aresta(arestas, origem, destino):
    for aresta in arestas:
        if aresta == [origem, destino]:
            return True
    return False


def vizinhos(vertices, arestas, vertice):
    lista_vizinhos = []
    for aresta in arestas:
        if aresta[0] == vertice:
            lista_vizinhos.append(aresta[1])
    return lista_vizinhos


def grau_vertices(vertices, arestas, nao_direcionado=False):
    graus = {}
    for vertice in vertices:
        if nao_direcionado:
            grau = 0
            for aresta in arestas:
                if aresta[0] == vertice:
                    grau += 1
            graus[vertice] = grau
        else:
            entrada = 0
            saida = 0
            for aresta in arestas:
                if aresta[0] == vertice:
                    saida += 1
                if aresta[1] == vertice:
                    entrada += 1
            graus[vertice] = {"saida": saida, "entrada": entrada, "total": entrada + saida}
    return graus


def percurso_valido(arestas, caminho):
    for i in range(len(caminho) - 1):
        u = caminho[i]
        v = caminho[i + 1]
        if not existe_aresta(arestas, u, v):
            return False
    return True


def listar_vizinhos(vertices, arestas, vertice):
    if vertice not in vertices:
        print(f"O vértice {vertice} não existe.")
        return
    lista = vizinhos(vertices, arestas, vertice)
    print(f"Vizinhos de {vertice}: {lista}")


def exibir_grafo(vertices, arestas):
    print(f"\nVértices: {vertices}")
    print("Arestas:")
    for aresta in arestas:
        print(f"({aresta[0]} -> {aresta[1]})")


def main():
    vertices = ["1", "2", "3", "4", "5"]
    arestas = [
        ["1", "2"],
        ["1", "3"],
        ["2", "4"],
        ["3", "4"],
        ["4", "5"],
        ["5", "1"],
    ]
    nao_direcionado = False

    while True:
        print("\n===== MENU - LISTA DE ARESTAS =====")
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
            exibir_grafo(vertices, arestas)
        elif opcao == "2":
            v = input("Nome do vértice: ")
            inserir_vertice(vertices, v)
            print(f"Vértice {v} inserido.")
        elif opcao == "3":
            o = input("Origem: ")
            d = input("Destino: ")
            inserir_aresta(vertices, arestas, o, d, nao_direcionado)
            print(f"Aresta {o} -> {d} inserida.")
        elif opcao == "4":
            v = input("Vértice a remover: ")
            remover_vertice(vertices, arestas, v)
        elif opcao == "5":
            o = input("Origem: ")
            d = input("Destino: ")
            remover_aresta(arestas, o, d, nao_direcionado)
            print(f"Aresta {o} -> {d} removida (se existia).")
        elif opcao == "6":
            o = input("Origem: ")
            d = input("Destino: ")
            if existe_aresta(arestas, o, d):
                print(f"Existe aresta {o} -> {d}.")
            else:
                print(f"Não existe aresta {o} -> {d}.")
        elif opcao == "7":
            v = input("Vértice: ")
            listar_vizinhos(vertices, arestas, v)
        elif opcao == "8":
            graus = grau_vertices(vertices, arestas, nao_direcionado)
            for v in graus:
                print(f"{v}: grau = {graus[v]}")
        elif opcao == "9":
            caminho = input("Digite o caminho separado por espaço (ex: 1 2 4 5): ").split()
            if percurso_valido(arestas, caminho):
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