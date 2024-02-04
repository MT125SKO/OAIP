import math
for x in range (-250,250,50):
    s=1
    a=x
    n=1
    while s+a !=s:
        s=s+a
        n=n+1
        a=a*x / n
        an = math.radians(250)
        q = x-an
    print("x=", x,"             ",  "s =",a,"                   ","math.exp= ", an, "                            ", "1=",  q)
