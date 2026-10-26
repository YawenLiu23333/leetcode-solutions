class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = set()
        province = 0
        for city in range(len(isConnected)):
            if city in visited:
                continue

            province += 1
            queue = deque([city])
            visited.add(city)
            while queue:
                current = queue.popleft()
                for neighbor in range(len(isConnected)):
                    if isConnected[current][neighbor] == 1:
                        if neighbor not in visited:
                            queue.append((neighbor))
                            visited.add(neighbor)
        return province 
                            
