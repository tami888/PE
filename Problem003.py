
def prime_factorization(num):
    prime_factors = []

    i = 2
    while 4 <= num:
        while num % i == 0:
            num /= i
            prime_factors.append(i)
        i += 1
    if num > 1:
        prime_factors.append(num)
    print prime_factors

if __name__ == '__main__':
    prime_factorization(100)