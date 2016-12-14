# -*- coding: utf-8 -*-
"""
10以下の素数の和は 2 + 3 + 5 + 7 = 17 である.

200万以下の全ての素数の和を求めよ.
"""
import math


def isprime2(n, primes):
    for i in range(int(math.sqrt(n))):
        if n % primes[i] == 0:
            return False
    return True

def primes(n):
    prms = [2]
    for i in range(3, n+1, 2):
        if isprime2(i, prms):
            prms.append(i)
    return prms

if __name__ == '__main__':
    print sum(primes(2000000))