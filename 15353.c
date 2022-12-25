#include <stdio.h>

int main(void){

}

/* python code wip
A, B = input().split()
ans = ""

up = False
for i in range(max([len(A), len(B)])):
    a = 0
    b = 0
    try:
        a = int(A[-1-i])
    except IndexError:
        a = 0
    try:
        b = int(B[-1-i])
    except IndexError:
        b = 0
    x = a+b
    ans = str(x % 10 + up) + ans
    up = x >= 10

if up:
    ans = "1" + ans

print(ans)

*/