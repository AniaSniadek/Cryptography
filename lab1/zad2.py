def euklides(a,n):
    A = n
    B = a
    U = 0
    V = 1

    while B != 0:
        q = A//B
        x1 = B
        x2 = A - q*B
        A = x1
        B = x2
        x1 = V
        x2 = U - q*V
        U = x1
        V = x2
    
    d = A
    u = U
    v = (d - a*u) // n
    return u,v,d

def odwrotnosc(n, b):
    u,v,d = euklides(b,n)
    if u*b % n == 1:
        return u  
