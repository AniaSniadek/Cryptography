import random

def generator(n,k):
    if k > 0:
        if k == 1:
            min_number = 0
            max_number = 1
        else:    
            min_number = 2**(k-1)
            max_number = (2**k)-1

        if min_number < n:
            while True:
                result = random.randint(min_number, max_number)
                if result < n:
                    break   
            return result
