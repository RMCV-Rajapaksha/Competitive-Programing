inputs = int(input())

possibleSpreader = []
reciver = []

for i in range(inputs):
    inputLine = input().strip().split()
 

    if(inputLine[1] == "??"):
        if i!=inputs-1 :    
            if possibleSpreader.count(inputLine[0])==0 and reciver.count(inputLine[0])==0:
                possibleSpreader.append(inputLine[0])
            if possibleSpreader.count(inputLine[2])==0 and reciver.count(inputLine[2])==0:
                possibleSpreader.append(inputLine[2])
        
    elif(inputLine[1]=="->"):
        if reciver.count(inputLine[2])==0:
            reciver.append(inputLine[2])
        if possibleSpreader.count(inputLine[0])==0:
            possibleSpreader.append(inputLine[0])
        if possibleSpreader.count(inputLine[2]) !=0:
            possibleSpreader.remove(inputLine[2])

for i  in possibleSpreader:
    print(i)
                                                                                                                                                                                                                                                                                                                                                                                                    