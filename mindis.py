# trav = []
a = [7, 1, 3, 4, 1, 7]
mindis = 99999
s = set(a)
index = 0
mindis = 99999
# if len(s) == len(a):
#     return -1
for i in range(len(a)):
    for j in range(i+1, len(a)):
        if a[i] == a[j]:
            print(a[i],a[j])
            index = j-i
            print(index)
            if index < mindis:
                mindis = index
print(mindis)
