def heapifDown(arr,index):
    largest=index
    lchild=2*index+1
    rchild=2*index+2
    if(lchild<len(arr) and arr[lchild]>arr[largest]):
        largest=lchild
    if(rchild<len(arr) and arr[rchild]>arr[largest]):
        largest=rchild
    if(largest!=index):
        arr[largest],arr[index]=arr[index],arr[largest]
        heapifDown(arr,largest)
def heapifUp(arr,index):
    if(index>0):
        parent=(index-1)//2
        if(arr[index]>arr[parent]):
            arr[index],arr[parent]=arr[parent],arr[index]
            heapifUp(arr,parent)
arr=[10,7,6,4,5,4,5,3,2]
t=int(input("enter number of Queries"))
for _ in range(t):
    index,val=map(int,input().split())
    if(arr[index]>val):
        arr[index]=val
        heapifDown(arr,index)
    elif(arr[index]<val):
        arr[index]=val
        heapifUp(arr,index)
print(arr)
        
