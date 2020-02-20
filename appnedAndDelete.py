s="abcd"
t="abcdert"
k=10
slen=len(s)
tlen=len(t)
if slen>tlen:
    length=tlen
else:
    length=slen
index=0
for i in range(length):
    if s[i]==t[i]:
        index+=1
        length-=1
    else:
        break
a=len(s[index:])
b=len(t[index:])
if a+b<=k:
    if (k-(a+b))%2==0:
        print("Yes")
    elif (k-len(s))>=len(t):
        print("Yes")
    else:
        print("No")
else:
    print("No")



# srest=[]
# trest=[]
# if len(s)>len(t):
#     length=len(t)
# else:
#     length=len(s)
# # length=len(s)>len(t)?len(s):len(t)
# for i in range(length):
#     if s[i]==t[i]:
#         continue
#     else:
#         srest.append(s[i:])
#         trest.append(t[i:])
#         break
# print(srest)
# print(trest)
# # a=len(srest)
# if len(srest):
#     k=k-len(srest[0])
# # b=len(trest)
# if len(trest):
#     k=k-len(trest[0])
# print(k)
# if k==0:
#     print("Yes case k=0")   
# elif len(srest)==0 and (k%2==0 or k>2*len(srest)):
#     print("yes case srest=0 and k>>")
# else:
#     print("No")