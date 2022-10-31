n=int(input())
temp=n
if n<0:
    n=(-1)*n
rev=0
while n>0:
    x=n%10
    rev=rev*10+x
    n=n//10
if temp>0:
    print(rev)
else:
    print((-1)*rev)