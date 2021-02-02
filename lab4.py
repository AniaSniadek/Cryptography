
# Zadanie 1
def suma(a, b):
    binaryA = bin(int(a, 16))[2:]
    binaryB = bin(int(b, 16))[2:]
    wynik = hex(int(binaryA, 2) ^ int(binaryB, 2))[2:]
    return wynik

# Zadanie 2
def xtime(a):
    binaryA = bin(int(a, 16))[2:]
    tmp = "1B"
    dlugosc = len(binaryA)
    
    while dlugosc != 8:
        binaryA = "0" + binaryA
        dlugosc = dlugosc + 1
    
    if int(binaryA[0]) == 0:
        wynik = hex(int(binaryA, 2) << 1)[2:]
        return wynik
    elif int(binaryA[0]) == 1:
        binaryA = binaryA[1:]
        hexA = hex((int(binaryA, 2) << 1))[2:]
        wynik = suma(hexA, tmp)
        return wynik


# Zadanie 3
def iloczyn(a, b):
    binaryA = bin(int(a, 16))[2:]
    dlugosc = len(binaryA) - 1
    wynik = '0'

    for i,v in enumerate(binaryA):
        if v == '1':
            tmp = b
            licznik = dlugosc
            
            while licznik != 0:
                tmp = xtime(tmp)
                licznik = licznik - 1
            
            hexTmp = hex(int(tmp, 16))[2:] 
            wynik = suma(hexTmp, wynik)

        dlugosc = dlugosc- 1    
    
    return wynik   


# Zadanie 4
def odwrotnosc(a):
    licznik = 13
    wynik = a

    while licznik > 0:
        binaryLicznik = int(bin(licznik)[2:])
        binaryStala = int(bin(1)[2:])

        if binaryLicznik & binaryStala != 1:
            tmp = a
        else:
            tmp = wynik
        
        wynik = iloczyn(wynik, tmp)
        licznik = licznik - 1
    
    return wynik


# Zadanie 1
print(suma('BA', '53'))
# Zadanie 2
print(xtime('ba'))
# Zadanie 3
print(iloczyn('57', '13'))
# Zadanie 4
print(odwrotnosc('BA'))
