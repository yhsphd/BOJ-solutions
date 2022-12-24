input()
numbers = input().split(" ")
numbers = [int(x) for x in numbers]
print(f"{min(numbers)} {max(numbers)}")
