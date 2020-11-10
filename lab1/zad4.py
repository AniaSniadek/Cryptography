# Funkcja z 3 zadania
def efektywne_potegowanie(x, k, n):
    y = 1
    binary = list((bin(k)[2])[::-1])
    l = len(binary)
    i = l - 1

    while i >= 0:
        y = y**2 % n
        if binary[i] == 1:
            y = y*x % n
        i = i - 1
    return y

# Funkcja sprawdzania liczby pierwszej
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
