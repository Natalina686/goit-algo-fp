import heapq

class Graph:
    def __init__(self):
        self.graph = {}
    
    def add_edge(self, u, v, weight):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append((v, weight))
        # Додамо вершину v, якщо її ще немає в графі
        if v not in self.graph:
            self.graph[v] = []

def dijkstra(graph, start):
    # Відстані до всіх вершин (ініціалізуємо до безкінечності)
    distances = {vertex: float('infinity') for vertex in graph.graph}
    distances[start] = 0  # Відстань до початкової вершини 0

    # Використовуємо бінарну купу для вибору вершини з найменшою відстанню
    priority_queue = [(0, start)]  # (відстань, вершина)

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # Якщо відстань, яку ми витягнули, більша за вже знайдену, пропускаємо
        if current_distance > distances[current_vertex]:
            continue

        # Проходимо по сусідам
        for neighbor, weight in graph.graph.get(current_vertex, []):
            distance = current_distance + weight

            # Якщо знайдено коротший шлях до сусіда
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

def main():
    g = Graph()
    g.add_edge('A', 'B', 1)
    g.add_edge('A', 'C', 4)
    g.add_edge('B', 'C', 2)
    g.add_edge('B', 'D', 5)
    g.add_edge('C', 'D', 1)

    start_vertex = 'A'
    shortest_paths = dijkstra(g, start_vertex)

    print("Найкоротші шляхи від вершини", start_vertex)
    for vertex, distance in shortest_paths.items():
        print(f"Вершина {vertex}: {distance}")

if __name__ == "__main__":
    main()