for i in range(int(input())):
    scores = list(map(int, input().split(" ")))[1:]
    mean = sum(scores)/len(scores)
    abv = 0
    for score in scores:
        if score > mean:
            abv += 1
    print("{:0.3f}%".format(abv/len(scores)*100))
