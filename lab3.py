import rsa
import lab1
import lab2
import random
import generator
import math

def mysqrt(x):
  if x==0:
      return 0 
  m=x
  p=x
  while True:
    r=(m+p//m)//2
    if m<=r:
        return m 
    m=r
    

def oblicz_ord(p):
    return (p + 1 - (2 * int(mysqrt(p)))) % p


# Zadanie 1
def generowanie_kluczy_ElGamal(k):
    while True:
        p = generator.generowanie(k)
        if p % 4 == 3 and lab1.pierwsza_Fermat(p):
            A, B = lab2.generowanie_krzywej(p)
            P = lab2.punkt_na_krzywej(A, B, p)
            _ord = oblicz_ord(p)

            while True:
                x = random.randint(1, _ord)
                if x < _ord:
                    Q = wielokrotnosc_punktu(A, B, p, x, P[0], P[1])
                    return A, B, p, P[0], P[1], Q[0], Q[1], x

            

# Zadanie 2
def wielokrotnosc_punktu(A, B, p, n, x, y):
    xq, yq = x, y
    xr, yr = 'e', 'e'
    
    while n > 0:
        if n % 2 == 1:
            xr, yr = lab2.suma_punktow(A, B, p, xr, yr, xq, yq)
            n = n - 1
        xq, yq = lab2.suma_punktow(A, B, p, xq, yq, xq, yq)
        n = n // 2
    
    return xr, yr


# Zadanie 3
def kodowanie_na_punkt_na_krzywej(A, B, p, m, n, u):
    if m < n and p > n * u:
        for i in range(1, u):
            x = (m * u % p) + (i % p)
            y_kwadrat = lab2.rownanie_krzywej(A, B, p, x)
            
            if lab2.czy_pierwiastek_kwadratowy(y_kwadrat, p):
                y = lab1.efektywne_potegowanie(y_kwadrat, (p+1)//4, p)
                return x,y
    else:
        print('Podane dane są niepoprawne')


# Zadanie 4
def szyfrowanie_na_krzywej(PMx, PMy, A, B, p, px, py, qx, qy):
    y = random.randint(0, oblicz_ord(p))
    c1x, c1y = wielokrotnosc_punktu(A, B, p, y, px, py)
    yq = wielokrotnosc_punktu(A, B, p, y, qx, qy)
    c2x, c2y = lab2.suma_punktow(A, B, p, PMx, PMy, yq[0], yq[1])
    return c1x, c1y, c2x, c2y


# Zadanie 5
def deszyfrowanie_na_krzywej(c1x, c1y, c2x, c2y, A, B, p, x):
    xc1 = wielokrotnosc_punktu(A, B, p, x, c1x, c1y)
    pmd = lab2.suma_punktow(A, B, p, c2x, c2y, xc1[0], -int(xc1[1]))
    return pmd

# Zadanie 6
def dekodowanie_punktu_na_krzywej(A, B, p, x, y, u):
    return (x - 1) // u

m = 300
n = m + random.randint(0, 1000000)
u = random.randint(30, 50)

# A, B, p, Px, Py, Qx, Qy, x = generowanie_kluczy_ElGamal(300)
# klucz_publiczny = [A, B, p, Px, Py, Qx, Qy]
# klucz_tajny = [A, B, p, Px, Py, Qx, Qy, x]
# print('Klucz publiczny: ' + str(klucz_publiczny))
# print('Klucz prywatny: ' + str(klucz_tajny))
# print('\n')
# PMx, PMy = kodowanie_na_punkt_na_krzywej(A, B, p, m, n, u)
# print('pm: (' + str(PMx) + ', ' + str(PMy) +')')
# print('\n')
# C1x, C1y, C2x, C2y = szyfrowanie_na_krzywej(PMx, PMy, A, B, p, Px, Py, Qx, Qy)
# print('c1: (' + str(C1x) + ', ' + str(C1y) +')')
# print('c2: (' + str(C2x) + ', ' + str(C2y) +')')
# print('\n')
# print('pmd: ' + str(deszyfrowanie_na_krzywej(C1x, C1y, C2x, C2y, A, B, p, x)))
# print('m: ' + str(dekodowanie_punktu_na_krzywej(A, B, p, PMx, PMy, u)))
