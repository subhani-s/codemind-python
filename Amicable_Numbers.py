a=int(input())
b=int(input())
c=0
for i in range(1,a):
    if a%i==0:
        c+=i
d=0
for i in range(1,b):
    if b%i==0:
        d+=i
if c==b and d==a:
    print("Amicable")
else:
    print("Not Amicable")