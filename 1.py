d = int(input())
d1 = 0
c = []
while d > d1:
    a = str(input())
    c.append(a)
    d1+= 1
new_c = [x.lower() for x in c]

d2 = int(input())
d3 = 0
c1 = []
while d2 > d3:
    a1 = str(input())
    c1.append(a1)
    d3+= 1
new_c1 = [x.lower() for x in c1]

v = []
for i in new_c1:
    for j in (i.split(' ')):
        if j not in new_c:
            if j not in v:
                v.append(j)
for k in v:
    print(k)
