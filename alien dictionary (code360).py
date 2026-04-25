from typing import List
from collections import deque
def getAlienLanguage(dictionary, k) :
    adj=[]
    for _ in range(k):
        adj.append([])
    # Write your code here.
    #step1:- find edges
    #k:-no of characters
    n=len(dictionary)
    #n:-total words
    indegre=[0]*k
    for ind in range(0,n-1):
        w1=dictionary[ind] #word 1
        w2=dictionary[ind+1] #word 2
        for i in range(0,min(len(w1),len(w2))):
            #eg :-w1[i]=b , w2=[i]=a
            if(w1[i]!=w2[i]):
                indegre[ord(w2[i])-ord('a')]+=1
                adj[ord(w1[i])-ord('a')].append(ord(w2[i])-ord('a'))
                break
    q=deque([])
    for i in range(0,k):
        if(indegre[i]==0):
            q.append(i)
    ans=[]
    while(len(q)>0):
        node=q.popleft()
        ans.append(node)
        for adjNode in adj[node]:
            indegre[adjNode]-=1
            if(indegre[adjNode]==0):
                q.append(adjNode)
    result=[]
    for num in ans:
        result.append(chr(ord('a')+num))
    return result


