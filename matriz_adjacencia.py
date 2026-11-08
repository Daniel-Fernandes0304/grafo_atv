def inserir_vertice(matriz, vertices, vertice):
    if vertice in vertices:
        return

    vertices.append(vertice)
    for linha in matriz:
        linha.append(0)
    matriz.append([0] * len(vertices))


def inserir_aresta(matriz, vertices, origem, destino, nao_direcionado=False):
    inserir_vertice(matriz, vertices, origem)
    inserir_vertice(matriz, vertices, destino)

    i = vertices.index(origem)
    j = vertices.index(destino)

    matriz[i][j] = 1
    if nao_direcionado:
        matriz[j][i] = 1


def remover_vertice(matriz, vertices, vertice):
    if vertice not in vertices:
        print(f"O vértice {vertice} não existe.")
        return

    i = vertices.index(vertice)
    matriz.pop(i)
    for linha in matriz:
        linha.pop(i)
    vertices.remove(vertice)
    print(f"Vértice {vertice} removido.")


def remover_aresta(matriz, vertices, origem, destino, nao_direcionado=False):
    if origem not in vertices or destino not in vertices:
        print("Vértice(s) não existe(m).")
        return

    i = vertices.index(origem)
    j = vertices.index(destino)

    matriz[i][j] = 0
    if nao_direcionado:
        matriz[j][i] = 0


def existe_aresta(matriz, vertices, origem, destino):
    if origem not in vertices or destino not in vertices:
        return False

    i = vertices.index(origem)
    j = vertices.index(destino)
    return matriz[i][j] == 1


def vizinhos(matriz, vertices, vertice):
    if vertice not in vertices:
        return []

    i = vertices.index(vertice)
    lista_vizinhos = []
    for j in range(len(matriz[i])):
        if matriz[i][j] == 1:
            lista_vizinhos.append(vertices[j])
    return lista_vizinhos


def grau_vertices(matriz, vertices, nao_direcionado=False):
    graus = {}
    for i in range(len(vertices)):
        saida = sum(matriz[i])
        if not nao_direcionado:
            entrada = 0
            for linha in matriz:
                entrada += linha[i]
            graus[vertices[i]] = {"saida": saida, "entrada": entrada, "total": entrada + saida}
        else:
            graus[vertices[i]] = saida
    return graus


def percurso_valido(matriz, vertices, caminho):
    for i in range(len(caminho) - 1):
        u = caminho[i]
        v = caminho[i + 1]
        if not existe_aresta(matriz, vertices, u, v):
            return False
    return True


def listar_vizinhos(matriz, vertices, vertice):
    if vertice not in vertices:
        print(f"O vértice {vertice} não existe.")
        return []
    lista = vizinhos(matriz, vertices, vertice)
    print(f"Vizinhos de {vertice}: {lista}")
    return lista


def exibir_grafo(matriz, vertices):
    print("\nMatriz de Adjacência:")
    print("\t", end="")
    for v in vertices:
        print(v, end="\t")
    print()
    for i in range(len(vertices)):
        print(vertices[i], end="\t")
        for valor in matriz[i]:
            print(valor, end="\t")
        print()


def main():
    vertices = ["Ana", "Bia", "Caio", "Davi", "Eva"]
    matriz = [
        [0,   1,   1,   0,   0],
        [1,   0,   0,   1,   0],
        [1,   0,   0,   1,   0],
        [0,   1,   1,   0,   1],
        [0,   0,   0,   1,   0],
    ]
    nao_direcionado = True

    while True:
        print("\n===== MENU - MATRIZ DE ADJACÊNCIA =====")
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
            exibir_grafo(matriz, vertices)
        elif opcao == "2":
            v = input("Nome do vértice: ")
            inserir_vertice(matriz, vertices, v)
            print(f"Vértice {v} inserido.")
        elif opcao == "3":
            o = input("Origem: ")
            d = input("Destino: ")
            inserir_aresta(matriz, vertices, o, d, nao_direcionado)
            print(f"Aresta {o} - {d} inserida.")
        elif opcao == "4":
            v = input("Vértice a remover: ")
            remover_vertice(matriz, vertices, v)
        elif opcao == "5":
            o = input("Origem: ")
            d = input("Destino: ")
            remover_aresta(matriz, vertices, o, d, nao_direcionado)
            print(f"Aresta {o} - {d} removida (se existia).")
        elif opcao == "6":
            o = input("Origem: ")
            d = input("Destino: ")
            if existe_aresta(matriz, vertices, o, d):
                print(f"Existe aresta {o} - {d}.")
            else:
                print(f"Não existe aresta {o} - {d}.")
        elif opcao == "7":
            v = input("Vértice: ")
            listar_vizinhos(matriz, vertices, v)
        elif opcao == "8":
            graus = grau_vertices(matriz, vertices, nao_direcionado)
            for v in graus:
                print(f"{v}: grau = {graus[v]}")
        elif opcao == "9":
            caminho = input("Digite o caminho separado por espaço (ex: Ana Bia Davi): ").split()
            if percurso_valido(matriz, vertices, caminho):
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