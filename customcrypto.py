import os, random


r = random.SystemRandom()
string = "ARE YOU WITH US"

def random_prime_gen(limit)->list[int]:
    primes = []
    while True:
        random_target = r.randint(1, 1000)
        k = 2
        composite_found = False
        while k < random_target:
            if (random_target%k == 0):
                composite_found = True
                break
            else: k+=1

        if not composite_found:
            primes.append(random_target)
            if (len(primes) == limit): break

    return primes


rBitString = str((r.randbytes(64)))

# print(rBitString)

print(random_prime_gen(8))
