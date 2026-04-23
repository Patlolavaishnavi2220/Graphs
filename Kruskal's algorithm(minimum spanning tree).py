class Disjoint:
    def __init__(self,V):
        self.rank = [0]*V 
        self.parent = [i for i in range(V)]
    def findUParent(self,node):  # path compression
        if(node == self.parent[node]):
            return node 
        self.parent[node] = self.findUParent(self.parent[node])
        return self.parent[node]
    def unionByRank(self,u,v):
        ultimateParentOfU = self.findUParent(u)
        ultimateParentOfV = self.findUParent(v)
        if(ultimateParentOfU == ultimateParentOfV):
            return 
        if(self.rank[ultimateParentOfU]<self.rank[ultimateParentOfV]):
            self.parent[ultimateParentOfU] = ultimateParentOfV
        elif(self.rank[ultimateParentOfV]<self.rank[ultimateParentOfU]):
            self.parent[ultimateParentOfV] = ultimateParentOfU
        else:
            self.parent[ultimateParentOfV] = ultimateParentOfU
            self.rank[ultimateParentOfU]+=1 
    
class Solution:
    def spanningTree(self, V, edges):
        ds = Disjoint(V)
        Sum = 0 
        edges.sort(key = lambda x:x[2])
        # link 
        for u,v,w in edges:
            if(ds.findUParent(u)!=ds.findUParent(v)):
                Sum+=w 
                ds.unionByRank(u,v)
        return Sum
