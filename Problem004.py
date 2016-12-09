# -*- coding: utf-8 -*-
def palindrome():
    num = []
    for i in range(100, 1000):                  # 初期条件から掛ける数は三桁のため100から開始
        for j in range(100, 1000):              # 同じく100から開始
            res = i * j
            num.append(res)                     # 結果をnumリストに格納
    num = map(str, num)                         # 文字列に変換
    num = filter(lambda x: x == x[::-1], num)   # リストに入った文字列と逆順の文字列が一致したならその要素をfilterで取り出す
    print max(map(int, num))                    # maxで最大値を表示

if __name__ == '__main__':
    palindrome()

