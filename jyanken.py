import random

#関数にまとめる
def janken():
    i = int(input("あなたの手は？（1:グー 2:チョキ 3:パー 0:終わり）=>"))

#vが0だった場合、ここでジャンケンを終了させる
    if i == 0:
        print("これでジャンケンを終わります")
        return i

    ih = "グー"
    if i == 2:
        ih = "チョキ"
    if i == 3:
        ih = "パー"
    print("あなたの手は{}です".format(ih))

    c = random.randint(1,3)
    ch = "グー"
    if c == 2:
        ch = "チョキ"
    if c == 3:
        ch = "パー"

    print("コンピューターの手は",ch,"です")

    if i == 1:
        if c == 1:
            print("あいこ")
        elif c == 2:
            print("勝ち")
        else:
            print("負け")
    elif i == 2:
        if c == 1:
            print("負け")
        elif c == 2:
            print("あいこ")
        else:
            print("負け")
    else:
        if c == 1:
            print("勝ち")
        elif c == 2:
            print("負け")
        else:
            print("あいこ")
    return i

#0~3以外であればvは何でもOK
v = 100

#vが0にならない限りジャンケンを続ける
while v != 0:
    v = janken()