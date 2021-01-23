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

p=930917809712841190032234708931401833451223394003818996220942158417286177606512230222515411
A=652018270186154717421126631979393340970709947093116948108083997942910588843194646030606382
B=493799115760624732891565181938648723101021421496598826542269096507977518380248750294579977
Px=860430333125178036509041357522553067138434346142085978366840451226766507920511927509535129
Py=536103635762214177603513687147777634166587108062011952936909643137433886451948417491746372
Qx=298129590994489142170135458553839712442439542644042878986075491694594710070845942532905215
Qy=532533462216673525821672559296439940677493761263865333095142836345081948742037149494735458
PMx=921544506336407957781707573412211768896371516222103471357199600899452124775303364567386977
PMy=444101125521907558613093920748160083004097153304696684347180306791863463949925079217235459
x=1365397280620819586260501631149989000495114327677431408652285325118105717765

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
