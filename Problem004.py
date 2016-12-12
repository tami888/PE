# -*- coding: utf-8 -*-
"""
左右どちらから読んでも同じ値になる数を回文数という. 2桁の数の積で表される回文数のうち, 最大のものは 9009 = 91 × 99 である.

では, 3桁の数の積で表される回文数の最大値を求めよ.
"""


def max_palindrome_number(n):
    n = map(str, n)                         # 文字列に変換
    n = filter(lambda x: x == x[::-1], n)   # リストに入った文字列と逆順の文字列が一致したならその要素をfilterで取り出す
    return max(map(int, n))                 # maxで最大値を表示

if __name__ == '__main__':
    ls = []
    for i in range(100, 1000):              # 初期条件から掛ける数は三桁のため100から開始
        for j in range(i, 1000,1):          # 同じく100から開始
            cand = i * j
            ls.append(cand)
    ans = max_palindrome_number(ls)
    print ans
