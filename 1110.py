numbers = []
numbers.append(int(input()))

while True:
    num = numbers[-1] // 10 + numbers[-1] % 10
    numbers.append(10 * (numbers[-1] % 10) + num % 10)
    if numbers[0] == numbers[-1]:
        print(len(numbers) - 1)
        break
