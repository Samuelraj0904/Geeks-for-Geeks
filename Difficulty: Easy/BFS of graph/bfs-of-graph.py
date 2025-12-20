class Solution:
    def bfs(self, adj):
        res = []
        qu = [0]
        vis = [False] * len(adj)
        vis[0] = True
        
        while(qu != []):
            node = qu.pop(0)
            res.append(node)
            for v in adj[node]:
                if vis[v] == False:
                    vis[v] = True
                    qu.append(v)
        return res