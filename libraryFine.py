d1, m1, y1, d2, m2, y2 = 9, 6, 2015, 6, 6, 2015
if y1 != y2:
    print(10000)
elif m1 != m2:
    if m1>m2:
        print(500*(abs(m1-m2)))
    else:
        print(0)
elif d1!=d2:
    if d1>d2:
        print(15*(abs(d1-d2)))
    else:
        print(0)
else:
    print(0)
