class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        for i, (a, b) in enumerate(equations):
            weight = values[i]
            graph[a].append((b, weight))
            graph[b].append((a, 1/weight))

        def dfs(current, target, product, visited):
            if current in visited:
                return -1

            visited.add(current)
            if current == target:
                return product
            
            for variable, weight in graph[current]:
                result = dfs(variable, target, product* weight, visited)
                if result != -1:
                    return result
            return -1

        res = []
        for a, b in queries:
            if a not in graph or b not in graph:
                res.append(-1)
            else:
                res.append(dfs(a, b, 1, set()))

        return res

            