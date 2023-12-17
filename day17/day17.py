import copy


class Graph:
    nodes = set()
    edges = set()


def load_data():
    data = []
    with open('map_test1') as f:
        for line in f.readlines():
            line_array = []
            for char in line.strip():
                line_array.append(int(char))
            data.append(line_array)
    return data


def print_matrix(matrix):
    for row in matrix:
        for item in row:
            print(item, end='\t\t')
        print()


def data2graph(data):
    graph = Graph()
    for y, line in enumerate(data):
        for x, value in enumerate(line):
            graph.nodes.add((y, x))
            if y > 0:
                weight = data[y-1][x]
                graph.edges.add(((y, x), (y-1, x), weight))
            if y < len(data) - 1:
                weight = data[y+1][x]
                graph.edges.add(((y, x), (y+1, x), weight))
            if x > 0:
                weight = data[y][x-1]
                graph.edges.add(((y, x), (y, x-1), weight))
            if x < len(line) - 1:
                weight = data[y][x+1]
                graph.edges.add(((y, x), (y, x+1), weight))
    return graph


def dijkstra(graph, start, end):
    Q = set()
    dist = {}
    prev = {}
    for node in graph.nodes:
        dist[node] = float('inf')
        prev[node] = None
        Q.add(node)
    dist[start] = 0

    while len(Q) > 0:
        u = None
        # find node with smallest distance to start
        for node in Q:
            if u is None or dist[node] < dist[u]:
                u = node
        Q.remove(u)
        # update distance for all neighbours
        for edge in graph.edges:
            if edge[0] == u:
                v = edge[1]
                alt = dist[u] + edge[2]
                if alt < dist[v]:
                    dist[v] = alt
                    prev[v] = u
    return dist, prev


def task1(graph):
    total = 0
    start = (0, 0)
    end = (max(graph.nodes)[0], max(graph.nodes)[1])
    dist, prev = dijkstra(graph, start, end)

    print_out = []
    for y in range(end[0] + 1):
        line = []
        for x in range(end[1] + 1):
            line.append(prev[(y, x)])
        print_out.append(line)

    print_matrix(print_out)

    return total


def task2(data):
    max_value = 0
    return max_value


def main():
    data = load_data()
    for line in data:
        print(line)
    print()

    graph = data2graph(data)

    print(f'Task 1: {task1(copy.deepcopy(graph))}')
    print(f'Task 2: {task2(copy.deepcopy(data))}')


if __name__ == '__main__':
    main()
