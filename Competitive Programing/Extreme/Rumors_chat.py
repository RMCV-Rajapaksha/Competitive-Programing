inputs = int(input())

possibleSpreader = []
receiver = [] 

for i in range(inputs):
    inputLine = input().strip().split()

    if inputLine[1] == "??":
        if i != inputs - 1:
            if inputLine[0] not in possibleSpreader and inputLine[0] not in receiver:
                possibleSpreader.append(inputLine[0])
            if inputLine[2] not in possibleSpreader and inputLine[2] not in receiver:
                possibleSpreader.append(inputLine[2])

    elif inputLine[1] == "->":
        if inputLine[2] not in receiver:
            receiver.append(inputLine[2])
        if inputLine[0] not in possibleSpreader:
            possibleSpreader.append(inputLine[0])
        if inputLine[2] in possibleSpreader:
            possibleSpreader.remove(inputLine[2])

possibleSpreader.sort()


for i in possibleSpreader:
    print(i)
