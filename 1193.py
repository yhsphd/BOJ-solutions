X = int(input())
n = 0
m = 0

while True:
    n += 1
    if 2*n*n-5*n+3 < X and X <= 2*n*n-n:
        break
while True:
    m += 1
    if 2*m*m-3*m+1 < X and X <= 2*m*m+m:
        break

A = X-(2*n*n-5*n+3)
if A > 2*n-1:
    A = 4*n-2-A
B = X-(2*m*m-3*m+1)
if B > 2*m:
    B = 4*m-B

print(f"{A}/{B}")
