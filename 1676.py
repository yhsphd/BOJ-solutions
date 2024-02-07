# we already have many even numbers, so we can consider only the multiples of 5

def count(num):
    if num == 0:
        return 0
    return num // 5 + count(num // 5)


print(count(int(input())))
