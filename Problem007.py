# -*- coding: utf-8 -*-
"""
素数を小さい方から6つ並べると 2, 3, 5, 7, 11, 13 であり, 6番目の素数は 13 である.

10 001 番目の素数を求めよ.
"""


def prime_number(n):
    i = 3
    ls = [2]
    while len(ls) < n:      # 入力したnより小さい場合ループを続ける
        for p in ls:
            if i % p == 0:  # iがpで割れるものならループを抜ける
                break;
        else:
            ls += [i]
        i += 2
    return ls

if __name__ == '__main__':
    ls = prime_number(10001)
    result = ls[-1]
    print result
    print len(ls)