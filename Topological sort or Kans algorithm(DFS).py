class Solution:
    def topoSort(self, V, edges):
        # Code here
        def dfs(n):
            for i in adjList[n]:
                if(vis[i] == 0):
                    vis[i] = 1 
                    dfs(i)
            stack.append(n) 
        adjList = [] 
        for _ in range(V):
            adjList.append([]) 
        for n,m in edges:
            adjList[n].append(m) 
        vis = [0]*V 
        stack = [] 
        for n in range(0,V):
            if(vis[n] == 0):
                vis[n] = 1 
                dfs(n)
        return stack[::-1]
