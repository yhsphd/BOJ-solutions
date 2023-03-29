string = input().upper()
chars = [0] * 26

for i in range(len(string)):
    chars[ord(string[i]) - 65] += 1

most = []
maxchar = max(chars)
for i in range(len(chars)):
    if chars[i] == maxchar:
        most.append(i)

if len(most) > 1:
    print("?")
    exit()

print(chr(most[0] + 65))
