m = int(input())
list = []
for i in range(0,m):
    ch = input().split()

    if ch[0] == "insert":
        list.insert(int(ch[1]),int(ch[2]))
    elif ch[0] == "print":
        print(list)
    elif ch[0] == "remove":
        list.remove(int(ch[1]))
    elif ch[0] == "append":
        list.append(int(ch[1]))
    elif ch[0] == "sort":
        list.sort()
    elif ch[0] == "pop":
        list.pop()
