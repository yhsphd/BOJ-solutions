abc = input().split(" ")
abc = [int(x) for x in abc]

print((abc[0] + abc[1]) % abc[2])
print(((abc[0] % abc[2]) + (abc[1] % abc[2])) % abc[2])
print((abc[0]*abc[1]) % abc[2])
print(((abc[0] % abc[2]) * (abc[1] % abc[2])) % abc[2])
