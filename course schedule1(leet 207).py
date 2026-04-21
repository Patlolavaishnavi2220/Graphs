from collections import deque
class Solution:
    def canFinish(self, V: int, edges: List[List[int]]) -> bool:
        adj=[]
        for _ in range(0,V):
            adj.append([])
        for u,v in edges:
            adj[v].append(u)
        inDegre =[0]*V
        for u,v in edges:
            inDegre[u]+=1
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
            return False
        return True


        
