# -*- coding: utf-8 -*-
"""
ピタゴラス数(ピタゴラスの定理を満たす自然数)とは a < b < c で以下の式を満たす数の組である.

a2 + b2 = c2
例えば, 32 + 42 = 9 + 16 = 25 = 52 である.

a + b + c = 1000 となるピタゴラスの三つ組が一つだけ存在する.
これらの積 abc を計算しなさい.
"""


def Problem9(n):
    for a in range(1, n+1):
        for b in range(1, n+1):
            c = n - a - b
            if c < 0:
                continue
            if (a ** 2 + b ** 2 == c ** 2):
                return a * b * c

if __name__ == '__main__':
    print Problem9(1000)