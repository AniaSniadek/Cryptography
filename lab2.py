import lab1
import random

def generowanie_pierwszych(k):
    n = random.getrandbits(k)
    while not lab1.pierwsza_Fermat(n):
        n = random.getrandbits(k)
    return n

def generowanie_kluczy():
    p = generowanie_pierwszych(1000)
    print(p)
    q = generowanie_pierwszych(1000)
    print(q)

generowanie_kluczy()

