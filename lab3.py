import rsa
import lab1
import lab2
import random

# Zadanie 1
# def generowanie_kluczy_ElGamal(k):
#     while True:
#         p = rsa.generowanie_pierwszych(k)
        
#         if(p % 4 == 3):
#             A, B = lab2.generowanie_krzywej(p)
#             P = punkt_na_krzywej(A, B, p)
            

# Zadanie 2
def wielokrotnosc_punktu(A, B, p, n, x, y):
    Q = [x, y]
    R = ['e', 'e']
    
    while n > 0:
        if n % 2 == 1:
            R = lab2.suma_punktow(A, B, p, R[0], R[1], Q[0], Q[1])
            n = n - 1
        Q = lab2.suma_punktow(A, B, p, Q[0], Q[1], Q[0], Q[1])
        n = n // 2
    
    return R


# Zadanie 3
def kodowanie_na_punkt_na_krzywej(A, B, p, m):
    n = m + random.randint(0, 1000000)
    u = random.randint(30, 50)
    
    if m < n and p > n * u:
        for i in range(1, u):
            x = (m * u % p) + (i % p)
            y_kwadrat = lab2.rownanie_krzywej(A, B, p, x)
            
            if lab2.czy_pierwiastek_kwadratowy(y_kwadrat, p):
                y = lab1.efektywne_potegowanie(y_kwadrat, (p+1)/4, p)
                return x,y,u
    else:
        print('Podane dane są niepoprawne')


# Zadanie 6
def dekodowanie_punktu_na_krzywej(A, B, p, x, y, u):
    return (x - 1) // u


# print(wielokrotnosc_punktu(8,10,19,3,15,3))
A = 336958446
B = 118309806
p = 927080059
m = 73
# n = m + random.randint(0, 1000000)
# u = random.randint(30, 50)
x,y,u = kodowanie_na_punkt_na_krzywej(A, B, p, m)
print(x, y)
print(dekodowanie_punktu_na_krzywej(A, B, p, x, y, u))

