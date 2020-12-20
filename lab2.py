import lab1
import random

# Wyróżnik
def deltaE(A, B, p):
    return (4 * lab1.efektywne_potegowanie(A, 3, p) + 27 * lab1.efektywne_potegowanie(B, 2, p)) % p

# Równianie krzywej - zwracanie y^2
def rownanie_krzywej(A, B, p, x):
    return (lab1.efektywne_potegowanie(x, 3, p) + (A * x) + B) % p

# Sprawdzanie czy liczba jest pierwiastkiem kwadratowym
def czy_pierwiastek_kwadratowy(x, p):
    if lab1.efektywne_potegowanie(x, (p-1)/2, p) and lab1.pierwsza_Fermat(p):
        return True
    else:
        return False

# Zadanie 1
def generowanie_krzywej(p):
    while True:
        if lab1.pierwsza_Fermat(p) and p % 4 == 3:
            A = random.randint(1, p - 1)
            B = random.randint(1, p - 1)

            delta = deltaE(A, B, p)
            if delta != 0:
                break
    
    # print('Y^2 = X^3 + ' + str(A) + 'X + ' + str(B) + ' mod ' + str(p))
    return A, B


# Zadanie 2
def punkt_na_krzywej(A, B, p):
    delta = deltaE(A, B, p)

    if delta != 0 and p % 4 == 3:
        while True:
            x = random.randint(0, p - 1)
            y_kwadrat = rownanie_krzywej(A, B, p, x)

            if czy_pierwiastek_kwadratowy(y_kwadrat, p):
                y = lab1.efektywne_potegowanie(y_kwadrat, (p+1)/4, p)
                break
        
        return x,y


# Zadanie 3
def czy_punkt_nalzey(A, B, p, x, y):
    y_kwadrat = rownanie_krzywej(A, B, p, x)
    
    if y_kwadrat == lab1.efektywne_potegowanie(y, 2, p):
        return True
    else:
        return False


# Zadanie 4
def punkt_przeciwny(x, y):
    return x, -y


# Zadanie 5
def suma_punktow(A, B, p, x1, y1, x2, y2):
    # P + 0 = P
    if x1 == 'e' and y1 == 'e':
        return x2, y2
    elif x2 == 'e' and y2 == 'e':
        return x1, y1

    # P + Q = R
    if x1 != x2:
        l = ((y2 - y1) * lab1.odwrotnosc((x2 - x1), p)) % p
        x3 = (lab1.efektywne_potegowanie(l, 2, p) - x1 - x2) % p
        y3 = (l * (x1 - x3) - y1) % p
        return x3, y3

    # P + P = 2P
    if x1 == x2 and y1 == y2:
        l = ((3 * lab1.efektywne_potegowanie(x1, 2, p) + A) * (lab1.odwrotnosc(2 * y1, p))) % p
        x3 = (lab1.efektywne_potegowanie(l, 2, p) - 2 * x1) % p
        y3 = (l * (x1 - x3) - y1) % p
        return x3, y3

    # P + -Q = 0
    if x1 == x2 and y1 == -y2:
        return 'e','e'
    



A=239614427021073265587611886177902927263167863041565491257781227550405368115731464059190159
B=447169285435982716467332439542997876345372330045685811964291613238129105735899852114277221
p=1183779584357076950937981497685946292711107412152534481102525547387604378262522402526266939
x=285113634279465403319996581740169338329454608669814309137990174814243655992779447106132850
y=598700530906084162596261101440667782569915319623798143751082061599951188013331503150304328
# Zadanie 1
# print(generowanie_krzywej(p))   
# Zadanie 2
# print(punkt_na_krzywej(A, B, p)) 
# Zadanie 3
# print(czy_punkt_nalzey(A, B, p, x, y))
# Zadanie 4
# print(punkt_przeciwny(x, y))
# Zadanie 5
print(suma_punktow(2,9,19,4,9,6,3))
print(suma_punktow(2,9,19,4,9,4,9))
print(suma_punktow(2,9,19,4,9,'e','e'))
print(suma_punktow(2,9,19,4,9,4,-9))
# print(suma_punktow(A, B, p, x, y, x, y))
