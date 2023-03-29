def recursion(s, l, r, c=0):
    c += 1
    if l >= r:
        return f"1 {c}"
    elif s[l] != s[r]:
        return f"0 {c}"
    else:
        return recursion(s, l + 1, r - 1, c)


def isPalindrome(s):
    return recursion(s, 0, len(s) - 1)


for i in range(int(input())):
    print(isPalindrome(input()))
