arr=[1, 2, 4, 5, 7, 8, 10]
d=3
count=0

for i in arr:
    for j in arr:
        if j-i==d:
            for k in arr:
                if k-j==d:
                    count+=1
print(count)                