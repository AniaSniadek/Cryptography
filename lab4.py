
# Zadanie 1
def suma(a, b):
    binaryA = bin(int(a, 16))[2:]
    binaryB = bin(int(b, 16))[2:]
    return hex(int(binaryA, 2) ^ int(binaryB, 2))[2:]

# Zadanie 2
def xtime(a):
    binaryA = bin(int(a, 16))[2:]
    binaryTmp = bin(int("1B", 16))[2:]
    length = len(binaryA)
    
    while length != 8:
        binaryA = "0" + binaryA
        length = length + 1
    
    if int(binaryA[0]) == 1:
        binaryA = binaryA[1:]
        return hex((int(binaryA, 2) << 1) ^ int(binaryTmp,2))[2:]
    elif int(binaryA[0]) == 0:
        return hex(int(binaryA, 2) << 1)[2:]



# Zadanie 1
print(suma('BA', '53'))
# Zadanie 2
print(xtime('ba'))
