from collections import deque
class Solution(object):
    def min_connections(self, graph, start, target): # solve by bfs
        visited = set([start])
        queue = deque([start])
        min_length = 0

        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                if node == target:
                    return min_length
                for nodes in graph[node]:
                    if nodes not in visited:
                        visited.add(nodes)
                        queue.append(nodes)
            min_length += 1
        return -1

def main():
    graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D', 'E'],
    'D': ['B', 'C', 'F'],
    'E': ['C'],
    'F': ['D']
    }
    start = 'A'
    target = 'F'
    sol = Solution()
    result = sol.min_connections(graph, start, target)
    print(result)

if __name__ == "__main__":
    main()