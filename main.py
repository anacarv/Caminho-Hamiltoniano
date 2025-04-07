def hamiltonian_path(graph, path, visited, n):
    if len(path) == n:
        return True

    last = path[-1]
    for neighbor in graph[last]:
        if not visited[neighbor]:
            visited[neighbor] = True
            path.append(neighbor)

            if hamiltonian_path(graph, path, visited, n):
                return True

            # backtrack
            visited[neighbor] = False
            path.pop()

    return False


def find_hamiltonian_path(graph):
    n = len(graph)
    for start in range(n):
        visited = [False] * n
        path = [start]
        visited[start] = True

        if hamiltonian_path(graph, path, visited, n):
            return path

    return None


def build_graph_from_input():
    n = int(input("Digite o número de vértices: "))
    m = int(input("Digite o número de arestas: "))
    is_directed = input("O grafo é direcionado? (s/n): ").lower() == 's'

    graph = [[] for _ in range(n)]

    print("Digite as arestas (uma por linha, no formato 'origem destino'):")
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        if not is_directed:
            graph[v].append(u)

    return graph


if __name__ == "__main__":
    graph = build_graph_from_input()
    result = find_hamiltonian_path(graph)

    if result:
        print("Caminho Hamiltoniano encontrado:")
        print(" -> ".join(map(str, result)))
    else:
        print("Nenhum Caminho Hamiltoniano encontrado.")
