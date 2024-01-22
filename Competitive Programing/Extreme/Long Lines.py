s=list(map(int,input().strip().split()))

num1=s[0]
height=s[1]
aisec=s[2]
cest=s[3]
q12=s[4]

data_var=[height]

for i in range(1,num1):
    number1=(aisec*data_var[i-1]+cest)
    number =number1%q12
    data_var.append(number)

count_number=0

for y in range(1,number):
    height=0
    for zz in range(y-1,-1,-1):
        if data_var[zz]>height:
            height=data_var[zz]
            count_number+=1

print(count_number)