y =39
dx=1/(y+1)
c = [0]*(y**2)
n = 1
while n > 1e-3:
    n = 0
    for i in range(y**2):
        l = c[i]
        b=0
        aE = aW = aN = aS = 1
        if (i+1)%y == 0:
            aE = 0           
        if i%y == 0:
            aW = 0
        if i >= y*(y-1):
            aN = 0
        if i < y:
            aS = 0

        row = i//y + 1
        col = i%y + 1
        x = col*dx
        yy = row*dx
        source = 32*(x*(x-1)+yy*(yy-1))
        b -= source*(dx**2)

        left  = c[i-1] if aW else 0
        right = c[i+1] if aE else 0
        top   = c[i+y] if aN else 0
        bot   = c[i-y] if aS else 0

        aP = aE + aW + aN + aS
        if (i+1)%y == 0:
            aP += 2
        if i < y:
            aP += 2
        if i>(y**2-y):
            aP+=2
        if i%y == 0:
            aP+=2
        
        w = 1.95

        c[i] = (1-w)*l + w*(left + right + top + bot + b)/aP

        if abs(c[i]-l) > n:
            n = abs(c[i]-l)

rows = []
for r in range(y):
    row = c[r*y:(r+1)*y]
    rows.append( row )


with open("C:\\Users\\jothi\\Downloads\\2dgrid.csv", "w") as f:
    for row in rows:
        f.write(",".join(map(str,row)))
        f.write("\n")
