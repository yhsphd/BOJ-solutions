nonself = set([])


def d(num: int):
    res = num + sum(map(int, str(num)))
    nonself.add(res)
    if (res < 10000):
        d(res)


for i in range(10000):
    d(i+1)

self = sorted(list(set(range(1, 10001)) - nonself))
for selfnum in self:
    print(selfnum)
