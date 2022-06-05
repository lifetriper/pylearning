def guanjia(game):
    def inner(*args, **kwargs):  # 此处的*/**表示打包所有的传入参数
        print("开外挂")
        game(*args, **kwargs)  # 此处的*/**表示将元组打散为位置参数，将字典打散为关键字参数
        print("关闭外挂")
    return inner


@guanjia  # play_dnf = guanjia(play_dnf)
def play_dnf(username, password):
    print(f"playing dnf with {username}, {password}")


@guanjia
def play_lol(username, password, hero):
    print(f"playing lol with {username}, {password}, {hero}")


play_dnf("admin", "password")
play_lol("admin", "password", "big hero")
