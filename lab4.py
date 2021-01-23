
# Zadanie 1
def suma(a, b):
    binaryA = bin(int(a, 16))[2:]
    binaryB = bin(int(b, 16))[2:]
    return hex(int(binaryA, 2) ^ int(binaryB, 2))[2:]

# Zadanie 2
def xtime(a):
    binaryA = bin(int(a, 16))[2:]
    binaryTmp = bin(int("1B", 16))[2:]
    dlugosc = len(binaryA)
    
    while dlugosc != 8:
        binaryA = "0" + binaryA
        dlugosc = dlugosc + 1
    
    if int(binaryA[0]) == 0:
        return hex(int(binaryA, 2) << 1)[2:]
    elif int(binaryA[0]) == 1:
        binaryA = binaryA[1:]
        return hex((int(binaryA, 2) << 1) ^ int(binaryTmp,2))[2:]


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
            
            wynik = suma(hex(int(tmp, 16))[2:], wynik)

        dlugosc = dlugosc- 1    
    
    return wynik    


# Zadanie 1
print(suma('BA', '53'))
# Zadanie 2
print(xtime('ba'))
# Zadanie 3
print(iloczyn('57', '13'))
