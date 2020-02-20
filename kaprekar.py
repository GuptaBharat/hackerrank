p=400
q=700
kar=[]
for i in range(p, q+1):
    # d=len(i)
    # s = str(i)
    # d = len(s)
    sqr = i**2
    st = str(sqr)
    length=len(st)//2
    right = st[length:]
    left = st[0:length]
    # print(length, "  ", left,"-", right)
    # print(left, right)
    if len(left)==0:
        left=0
    li = int(left)
    ri = int(right)
    if (li+ri == i):
        print(i, end=" ")
        kar.append(i)
if len(kar)==0:
    print("INVALID RANGE")