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
