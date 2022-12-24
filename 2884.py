num = input().split(" ")
num = [int(x) for x in num]

time = num[0] * 60 + num[1]
time -= 45
print(f"{time//60 if time>=0 else time//60+24} {time%60}")
