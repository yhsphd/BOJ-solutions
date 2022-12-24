num = input().split(" ")
num = [int(x) for x in num]
period = int(input())

time = num[0] * 60 + num[1]
time += period
print(f"{time//60 if time<1440 else time//60%24} {time%60}")
