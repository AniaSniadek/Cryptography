import lab1
import random
import math

message="823789137891789217389173981378913789137289"

def generowanie_pierwszych(k):
    n = random.getrandbits(k)
    while not lab1.pierwsza_Fermat(n):
        n = random.getrandbits(k)
    return n

def nwd(a, b): return nwd(b, a%b) if b else a

def generowanie_kluczy():
    p = generowanie_pierwszych(1024)
    print('p = ' + str(p))
    q = generowanie_pierwszych(1024)
    print('q = ' + str(q))
    print('\n')

    n = p * q
    phi = (p - 1) * (q - 1)

    while True:
        e = random.randint(0, phi)
        d = lab1.odwrotnosc(phi, e)

        if math.gcd(e, phi) == 1 and d > 1:
            break
    
    return n,e,d

# Generowanie klucza publicznego i prywatnego
n,e,d = generowanie_kluczy()
print('n = ' + str(n))
print('e = ' + str(e))
print('d = ' + str(d))
print('\n')
# publicKey = [n,e]
# privateKey = [n,d]

# Szyfrowanie wiadomości
cipher = lab1.efektywne_potegowanie(int(message), int(e), int(n))
print('c = ' + str(cipher))
print('\n')

# Odszyfrowywanie wiadomości
m = lab1.efektywne_potegowanie(int(cipher), int(d), int(n))
print('m = ' + str(m))

