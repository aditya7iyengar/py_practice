def answer(n):
    return ''.join(prime_strs(n+5))[n:n+5]

def prime_strs(num):
    candidate = 2
    prms = ''
    while len(prms) < num:
        if is_prime(candidate) == True:
            prms += str(candidate)
        candidate += 1
    return prms

def is_prime(num):
    if num < 10:
        return num in [2, 3, 5, 7]
    else:
        return not any(num % x == 0  for x in range(2, ceil_sqrt(num)))

def ceil_sqrt(num):
    return int(num**(0.5)) + 1

print(is_prime(15))
print(prime_strs(20))
print(answer(0))
print(answer(3))
print(answer(5))
