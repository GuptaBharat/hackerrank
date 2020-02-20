import math
a=3
b=90000000000
count=0
lower=(int)(a**0.5)
higher=(int)(b**0.5)+1
for i in range(lower,higher+1):
    if (i**2) in range(a,b+1):
        count+=1
print(count)



# count=0
# l=[]
# a1=(int)(a**0.5)
# print(a1)
# b1=(int)(b**0.5)+1
# print(b1)
# for i in range(a1,b1+1):
#     l.append(i**2)
# for i in range(a,b+1):
#     if i in l:
#         count+=1
# print(count)