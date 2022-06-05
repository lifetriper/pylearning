def wrapper1(game):
    def inner(*args, **kwargs):
        print("wrapper1 进入")   # 1
        ret = game(*args, **kwargs)  # wrapper2.inner
        print("wrapper1 推出")  # 5
        return ret
    return inner


def wrapper2(game):
    def inner(*args, **kwargs):
        print("wrapper2 进入")  # 2
        ret = game(*args, **kwargs)  # play_dnf
        print("wrapper2 推出")  # 4
        return ret
    return inner


@wrapper1  # play_dnf = wrapper1(wrapper2.inner)  play_dnf = wrapper1.inner
@wrapper2  # play_dnf = wrapper2(play_dnf)   play_dnf = wrapper2.inner
def play_dnf(username, password):
    print(f"playing dnf with {username}, {password}")  # 3
    return 100


@wrapper2
def play_lol(username, password, hero):
    print(f"playing lol with {username}, {password}, {hero}")
    return 200


ret = play_dnf("admin", "password")
print(ret)

ret = play_lol("admin", "password", "big hero")
print(ret)
