class Solution:
    def isCyclic(self, V, edges):
        def dfs(n):
            for i in adj[n]:
                if(vis[i] == 0):
                    vis[i] = 1
                    pathVis[i] = 1 
                    if(dfs(i)):
                        return True
                elif(pathVis[i] == 1):
                    return True 
            pathVis[n] = 0 
        # code here
        adj = [] 
        for _ in range(V):
            adj.append([]) 
        for n,m in edges:
            adj[n].append(m) 
        vis = [0]*V 
        pathVis = [0]*V 
        for n in range(0,V):
            if(vis[n] == 0):
                vis[n] = 1 
                pathVis[n] = 1 
                if(dfs(n)):
                    return True 
        return False
