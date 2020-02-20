p=20
d=3
m=6
s=85
cost=0
count=0

while s>=0:
    cost+=p
    s-=p
    if p-d<m:
        p=m
    else:
        p-=d
    count+=1
    
print(count)
