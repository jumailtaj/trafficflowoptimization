import heapq

class TrafficNetwork:
    def __init__(self):
        # Define the road network as a graph (adjacency list)
        # Format: node: [(neighbor, travel_time), ...]
        self.graph = {
            'A': [('B', 4), ('C', 2)],
            'B': [('A', 4), ('C', 1), ('D', 5)],
            'C': [('A', 2), ('B', 1), ('D', 8), ('E', 10)],
            'D': [('B', 5), ('C', 8), ('E', 2), ('F', 6)],
            'E': [('C', 10), ('D', 2), ('F', 3)],
            'F': [('D', 6), ('E', 3)]
        }

    def dijkstra(self, start):
        # Initialize distances with infinity
        distances = {node: float('inf') for node in self.graph}
        distances[start] = 0
        pq = [(0, start)]  # Priority queue

        while pq:
            current_distance, current_node = heapq.heappop(pq)

            if current_distance > distances[current_node]:
                continue

            for neighbor, weight in self.graph[current_node]:
                distance = current_distance + weight

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(pq, (distance, neighbor))

        return distances

    def optimize_traffic_flow(self):
        print("Optimized Travel Times from All Nodes:\n")
        for node in self.graph:
            shortest_paths = self.dijkstra(node)
            print(f"From {node}:")
            for dest, time in shortest_paths.items():
                print(f"  to {dest}: {time} units")
            print("-" * 30)

# Run the optimization
if __name__ == "__main__":
    network = TrafficNetwork()
    network.optimize_traffic_flow()
