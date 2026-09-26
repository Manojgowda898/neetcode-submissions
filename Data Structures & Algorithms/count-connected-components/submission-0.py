class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {i:[] for i in range(n)}

        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited =set()

        def dfs(node):

            visited.add(node)

            for nei in graph[node]:
                if nei not in visited:
                    dfs(nei)

        components = 0

        for i in range(n):
            if i not in visited:
                dfs(i)
                components += 1

        return components