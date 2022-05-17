num=input()
l=[]
for i in num:
    l.append(i)
for i in range(len(l)):
    if(l[i]=="6"):
        l=l[:i]+["9"]+l[i+1:]
        break
print("".join(l))