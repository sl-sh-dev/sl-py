def eval_pol(n, x):
    su = 0.0
    mu = 10.0
    pu = 0.0
    pol = [0.0] * 100
    for _ in range(n):
        su = 0.0
        for j in range(100):
            mu = (mu + 2.0) / 2.0
            pol[j] = mu
        for j in range(100):
            su = pol[j] + su * x
        pu = pu + su
    return pu
