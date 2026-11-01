class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        par = [i for i in range(n)]
        rank = [1]*n
        components = n

        def find(node):
            while node != par[node]:
                node = par[node]
                par[node] = par[par[node]]
            return node
        
        def union(n1, n2):
            nonlocal components
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return False
            components -= 1
            if rank[p1] < rank[p2]:
                p1, p2 = p2, p1
            par[p2] = p1
            rank[p1] += rank[p2]
            return True
        
        for a, b in edges:
            if not union(a, b):
                return False
        
        return True if components == 1 else False