from collections import deque
class Solution:
    def isBipartite(self, V, edges):
        # code here
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
                q = deque([]) 
                q.append(n)
                while(len(q)>0):
                    node = q.popleft() 
                    for i in adj[node]:
                        if(color[i] == -1):
                            color[i] = 1-color[node]
                            q.append(i) 
                        elif(color[i] == color[node]):
                            return False
        return True
