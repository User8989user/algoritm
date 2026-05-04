#1 

def has_cycle(graph, directed=False):
    """
    graph: dict или list списков смежности
    directed: True для ориентированного графа, False для неориентированного
    возвращает True, если есть цикл
    """
    n = len(graph)
    visited = [0] * n  # 0 - не посещена, 1 - в стеке (для directed), 2 - обработана

    def dfs(v, parent):
        visited[v] = 1 if directed else True  # для неориентированного просто отмечаем посещённой
        for neighbor in graph[v]:
            if directed:
                if visited[neighbor] == 1:
                    return True
                if visited[neighbor] == 0:
                    if dfs(neighbor, v):
                        return True
            else:  # неориентированный
                if neighbor == parent:
                    continue
                if visited[neighbor]:
                    return True
                if dfs(neighbor, v):
                    return True
        if directed:
            visited[v] = 2
        return False

    for i in range(n):
        if directed:
            if visited[i] == 0:
                if dfs(i, -1):
                    return True
        else:
            if not visited[i]:
                if dfs(i, -1):
                    return True
    return False

# Пример для неориентированного графа
undirected_graph = {0: [1, 2], 1: [0, 3], 2: [0, 3], 3: [1, 2]}  # есть цикл 0-1-3-2-0
print(has_cycle(undirected_graph, directed=False))  # True

# Пример без цикла (дерево)
tree_graph = {0: [1, 2], 1: [0, 3], 2: [0], 3: [1]}
print(has_cycle(tree_graph, directed=False))  # False

