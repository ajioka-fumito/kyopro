def cumsum(list_):
    lenth = len(list_)
    now = 0
    ls = [0 for _ in range(lenth)]
    for i in range(lenth):
        now += list_[i]
        ls[i] = now
    return ls