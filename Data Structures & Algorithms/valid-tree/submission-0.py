class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        if len(edges) != n - 1:
            return False

        graph = defaultdict(list)

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        '''{0:[1,2,3]
          1:[0,4]
          2:[0]
          3:[0]
          4:[1]}'''

        visited = set()

        def dfs(node):
            if node in visited:
                return 

            visited.add(node)

            for neighbours in graph[node]:
                dfs(neighbours)

        dfs(0)

        return len(visited) == n