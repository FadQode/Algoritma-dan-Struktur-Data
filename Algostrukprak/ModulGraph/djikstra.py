import heapq


# Create a graph from the adjacency matrix



def dijkstra(graph, start):
	n = len(graph)
	distances = [float('inf')] * n
	distances[start] = 0
	priority_queue = [(0, start)]
	while priority_queue:
		current_distance, current_node = heapq.heappop(priority_queue)
		if current_distance > distances[current_node]:
			continue
		for neighbor in range(n):
			if graph[current_node][neighbor] != 0 : # There is an edge
				distance = current_distance + graph[current_node][neighbor]
				if distance < distances[neighbor] :
					print(distance, neighbor)
					distances[neighbor] = distance
					heapq.heappush(priority_queue, (distance, neighbor))
	
	return distances

# Example graph represented as an adjacency matrix
graph = [
	[0, 1, 4, 0],
	[1, 0, 2, 5],
	[4, 2, 0, 1],
	[0, 5, 1, 0]
]
qn1 = [
    # 0 1 2 3 4 5 6 7 8 
     [0,4,0,0,0,0,0,8,0],
     [4,0,8,0,0,0,0,11,0],
     [0,8,0,7,0,4,0,0,2],
     [0,0,7,0,9,14,0,0,0],
     [0,0,0,9,0,10,0,0,0],
     [0,0,4,14,10,0,2,0,0],
     [0,0,0,0,0,2,0,1,6],
     [8,11,0,0,0,0,1,0,7],
     [0,0,2,0,0,0,6,7,0]
]

start_node = 0


print(dijkstra(qn1, start_node))

