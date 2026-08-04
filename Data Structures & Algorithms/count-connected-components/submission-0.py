class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        par = [i for i in range(n)]
        rank = [1]*n

        def find(node):
            while node!= par[node]:
                node = par[node]
                par[node] = par[par[node]]
            return par[node]
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return False
            if rank[p1] < rank[p2]:
                p1, p2 = p2, p1
            par[p2] = p1
            rank[p1] += rank[p2]
            return True
        
        for a, b in edges:
            if union(a, b):
                n -= 1
        
        return n