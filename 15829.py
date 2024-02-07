r, M = 31, 1234567891

input()
txt = [ord(char) - 96 for char in input()]

print(sum([txt[i] * (r ** i) for i in range(len(txt))]) % M)
