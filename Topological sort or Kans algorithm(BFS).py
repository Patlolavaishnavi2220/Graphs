from collections import deque 
class Solution:
    def topoSort(self, V, edges):
        # Code here
        adj = [] 
        for _ in range(0,V):
            adj.append([]) 
        for n,m in edges:
            adj[n].append(m) 
        q = deque([]) 
        inDegree = [0]*V 
        for i in range(0,V):
            for j in adj[i]:
                inDegree[j]+=1 
        for i in range(0,V):
            if(inDegree[i] == 0):
                q.append(i) 
        ans = []
        while(len(q)>0):
            node = q.popleft() 
            ans.append(node) 
            for i in adj[node]:
                inDegree[i]-=1 
                if(inDegree[i] == 0):
                    q.append(i) 
        return ans
