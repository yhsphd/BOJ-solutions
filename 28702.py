"""1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
"""

ary = [input() for i in range(3)]
ary = [int(ent) if ent.isnumeric() else -1 for ent in ary]
dst = 0

for i in range(len(ary)):
    if(ary[i] > 0):
        dst = ary[i] + len(ary) - i

print("FizzBuzz" if dst % 15 == 0 else "Fizz" if dst % 3 == 0 else "Buzz" if dst % 5 == 0 else dst)