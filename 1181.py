words = set()
ans = []

for i in range(int(input())):
    words.add(input())

words = sorted(list(words))
for i in range(1, 51):
    for word in words:
        if len(word) == i:
            ans.append(word)

print("\n".join(ans))
