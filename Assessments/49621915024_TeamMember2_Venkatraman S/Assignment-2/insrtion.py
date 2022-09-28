n=int(input())
list=[]
for i in range(0,n):
    v=input().split()
    if v[0]=="insert":
        list.insert(int(v[1]),int(v[2]))
    elif v[0]=="print":
        print(list)
    elif v[0]=="remove":
        list.remove(int(v[1]))
    elif v[0]=="append":
        list.append(int(v[1]))
    elif v[0]=="sort":
        list.sort()
    elif v[0]=="pop":
        list.pop()
    else:
        list.reverse()
