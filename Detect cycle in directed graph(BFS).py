from collections import deque
class Solution:
    def isCyclic(self, V, edges):
        # code here
        adj=[]
        for _ in range(0,V):
            adj.append([])
        for u,v in edges:
            adj[u].append(v)
        inDegre =[0]*V
        for u,v in edges:
            inDegre[v]+=1
        q=deque([])
        for i in range(0,V):
            if(inDegre[i]==0):
                q.append(i)
        ans=[]
        while(len(q)>0):
            node=q.popleft()
            ans.append(node)
            for adjNode in adj[node]:
                inDegre[adjNode]-=1
                if(inDegre[adjNode]==0):
                    q.append(adjNode)
        if(len(ans)!=V):
            return True
        return False
