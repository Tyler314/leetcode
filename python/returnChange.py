def returnChange(change):
    coins = [1, 5, 10, 25]
    ret = []
    while change != 0:
        if change - coins[-1] >= 0:
            change -= coins[-1]
            ret.append(coins[-1])
        else:
            coins.pop()
    return ret