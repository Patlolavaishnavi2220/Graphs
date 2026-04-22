class Disjoint:
    def __init__(self,V):
        self.rank=[0]*V
        self.parent=[i for i in range(0,V)]
        #path compression
    def findUParent(self,node):
        if(node==self.parent[node]):
            return node
        self.parent[node]=self.findUParent(self.parent[node])
        return self.parent[node]
    
    def findParent(self,u,v):
        return self.findUParent(u)==self.findUParent(v)

    def unionByRank(self,u,v):
        pu=self.findUParent(u)
        pv=self.findUParent(v)
        #if same ultimate parent for u,v need not to find rank and give connection so
        if(pu==pv):
            return
        #if ultimate parents have same rank eg:-(u,v)=(1,2)
        if(self.rank[pu]==self.rank[pv]):
            self.parent[pv]=pu
            self.rank[pu]+=1
        #if pu rank is small and pv rank is bigger ie [pu<pv] then parent changes but rank does not changes
        elif(self.rank[pu]<self.rank[pv]):
            self.parent[pu]=pv
        #if pv<pu
        elif(self.rank[pv]<self.rank[pu]):
            self.parent[pv]=pu
ob=Disjoint(7)
ob.unionByRank(0,1)
ob.unionByRank(1,2)
ob.unionByRank(2,3)
if(ob.findParent(0,3)):
    print(True)
else:
    print(False)



