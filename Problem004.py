# -*- coding: utf-8 -*-


def palindrome(n):
    n = map(str, n)                         # 文字列に変換
    n = filter(lambda x: x == x[::-1], n)   # リストに入った文字列と逆順の文字列が一致したならその要素をfilterで取り出す
    return max(map(int, n))                 # maxで最大値を表示

if __name__ == '__main__':
    ls = []
    for i in range(100, 1000):              # 初期条件から掛ける数は三桁のため100から開始
        for j in range(100, 1000):          # 同じく100から開始
            cand = i * j
            ls.append(cand)
    ans = palindrome(ls)
    print ans
