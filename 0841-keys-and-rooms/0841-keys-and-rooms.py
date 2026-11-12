class Solution:
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
        visited = set()

        def dfs(i):
            if i >= len(rooms) or i in visited:
                return
            
            visited.add(i)

            if rooms[i]:
                for j in rooms[i]:
                    dfs(j)
        dfs(0)
        return len(visited) == len(rooms)
        
