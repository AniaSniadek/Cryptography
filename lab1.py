# Zadanie 1:
import random

def generator_Zn(n,k):
    if k > 0:
        if k == 1:
            min_number = 0
            max_number = 1
        else:    
            min_number = 2**(k-1)
            max_number = (2**k)-1

        if min_number < n:
            while True:
                result = random.randint(min_number, max_number)
                if result < n:
                    break   
            return result


# Zadanie 2
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


# Zadanie 3:
def efektywne_potegowanie(x, k, n):
    y = 1
    binary = list((bin(k))[::-1])
    binary.pop()
    binary.pop()
    l = len(binary)
    i = l - 1

    while i >= 0:
        y = y**2 % n
        if int(binary[i]) == 1:
            y = y*x % n
        i = i - 1
    return y


# Zadanie 4:
def czy_pierwsza(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def reszta_kwadratowa(a, p):
    isPrime = czy_pierwsza(p)
    if isPrime:
        result = efektywne_potegowanie(a, (p-1)//2, p)
        if result == 1:
            return True
        else:
            return False
    else: 
        return False              


# Zadanie 5
def pierwiastek_kwadratowy(b, p):
    if p % 4 == 3:
        isRest = reszta_kwadratowa(b, p)
        if isRest:
            result = efektywne_potegowanie(b, (p+1)//4, p)
            return result

         
# Zadanie 6
def pierwsza_Fermat(n):
    if n == 1:
        return False
    elif n == 2 or n == 3:
        return True
    elif n > 3:
        k = 100
        while k != 0:
            a = random.randint(2, n-2)
            result = efektywne_potegowanie(a, n-1, n)
            if result != 1:
                return False
            k = k - 1

        return True



# PRINT
# print('ZADANIE 1:', generator_Zn(100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000961, 300))
# print('ZADANIE 2:', odwrotnosc(100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000961, 76638723687263876287368268368726378623873687326872634868374687236487623874687648634863847623846834687643))
# print('ZADANIE 3:', efektywne_potegowanie(76638723687263876287368268368726378623873687326872634868374687236487623874687648634863847623846834687643, 76382637812836812638612836812638612376182263812623861283618723681263861238612386, 100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000961))
# print('ZADANIE 4:', reszta_kwadratowa(4, 15485863))
# print('ZADANIE 5:', pierwiastek_kwadratowy(2, 15485863))
# print('ZADANIE 6:', pierwsza_Fermat(100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000961))
