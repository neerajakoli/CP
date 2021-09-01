# arr=[1,-2,3,4,1,-1,2,5,-2] 
def submax(arr):
    L=[]
    f=[]
    for i in range(len(arr)):
        t=0
        p=[]
        for j in range(i,len(arr)):
            if(t+arr[j]>t):
                t=t+arr[j]
                p.append(arr[j])
            else:
                break 
        L.append(t)
        f.append(p)
    return f[L.index(max(L))]
arr=[1,-2,3,4,1,-1,2,5,-2] 
print(submax(arr))