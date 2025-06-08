class Solution(object):
    def findRedundantConnection(self, edges):
        n = len(edges)
        parent = [i for i in range(n + 1)] # Initialize each node as its own parent
        rank = [0] * (n + 1) # Rank for union by rank

        def find(i):
            if parent[i] != i:
                parent[i] = find(parent[i]) #path compression
            return parent[i]

        def join(u, v):
            rootU = find(u)
            rootV = find(v)

            if rootU != rootV:
                #uniom by rank
                if rank[rootU] > rank[rootV]:
                    parent[rootV] = rootU
                elif rank[rootU] < rank[rootV]:
                    parent[rootU] = rootV
                else:
                    parent[rootV] = rootU
                    rank[rootU] += 1
        
        for u, v in edges:
            if find(u) == find(v):
                return [u, v] #cycle detected
            join(u, v) #merge sets
        
        return [] #unreachable for valid inputs
        