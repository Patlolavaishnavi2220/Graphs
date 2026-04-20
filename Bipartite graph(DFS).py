class Solution:
    def isBipartite(self, V, edges):
        # code here
        def dfs(n):
            for i in adj[n]:
                if(color[i] == -1):
                    color[i] = 1-color[n] 
                    if(dfs(i) == False):
                        return False
                elif(color[n] == color[i]):
                    return False
        adj = [] 
        for _ in range(V):
            adj.append([]) 
        for n,m in edges:
            adj[n].append(m)
            adj[m].append(n) 
        color = [-1]*V 
        for n in range(0,V):
            if(color[n] == -1):
                color[n] = 0 
                if(dfs(n) == False):
                    return False 
        return True
