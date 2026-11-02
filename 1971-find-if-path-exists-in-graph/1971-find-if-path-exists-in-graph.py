class Solution:
    def validPath(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)

        def dfs(current, target, visited):
            if current in visited:
                return False
            
            visited.add(current)

            if current == target:
                return True

            for nei in graph[current]:
                result = dfs(nei, target, visited)
                if result:
                    return True
            return False
        return dfs(source, destination, set())