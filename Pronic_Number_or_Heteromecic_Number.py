n=int(input())
fact=0
for i in range(1,n):
    if i*(i+1)==n:
        fact=10
        print("YES")
        
if fact!=10:
    print("NO")