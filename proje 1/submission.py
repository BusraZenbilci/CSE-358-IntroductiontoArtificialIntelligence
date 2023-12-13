import csv
import queue as Q 
import heapq


class CityNotFoundError(Exception):
    def __init__(self, city):
        print("%s does not exist" % city)
    


def build_graph(path):
   
    graph = {}
    
    with open(path, 'r',  encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            source = row['city1']
            target = row['city2']
            distance = float(row['distance'])
        
            if source not in graph:
                graph[source] = {}
            if target not in graph:
                graph[target] = {}

            graph[source][target] = distance
            graph[target][source] = distance

    return graph


def uniform_cost_search(graph, start, end):
    if start not in graph:
        raise CityNotFoundError(start)
    if end not in graph:
        raise CityNotFoundError(end)

    priority_queue = [(0, start)]

    cost_so_far = {start: 0}

    previous_node = {start: None}

    while priority_queue:
        
        current_cost, current_node = heapq.heappop(priority_queue)

        if current_node == end:
            break

        for neighbor, edge_cost in graph[current_node].items():
            
            total_cost = current_cost + edge_cost

            if neighbor not in cost_so_far or total_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = total_cost
                previous_node[neighbor] = current_node
                heapq.heappush(priority_queue, (total_cost, neighbor))

    path = []
    current = end
    while current:
        path.append(current)
        current = previous_node[current]
    path.reverse()
    distance = cost_so_far[end]
    return path, distance
        


if __name__ == "__main__":

    path=r'C:\Users\BÜŞRA\Desktop\proje 1\data\cities.csv'

    start = input("Enter the start (current city): ")
    end = input("Enter the end (target city): ")

    try:
        graph = build_graph(path)
        result = uniform_cost_search(graph, start, end)
        if result:
            path, distance = result

            print("Shortest path: ", " -> ".join(path))
            print("distance: ", distance)
        else:
            print("No path found.")
    except FileNotFoundError:
        print("File not found.")
    except CityNotFoundError   :
        pass