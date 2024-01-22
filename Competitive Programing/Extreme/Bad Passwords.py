
n = int(input())


sequence_map = {}
for i in range(n):
    values = input().split()[1:]
    for value in values:
        sequence_map[value] = i


p = int(input())
count =0

for _ in range(p):
    old_password, new_password = input().split()
    for i in old_password:
        for y in new_password:
            if i == y:
                count +=1
            else: 
                count -=1

    
    
    if ( 
        sequence_map.get(old_password, -1) == sequence_map.get(new_password, -2) or
        old_password == new_password
    ):
        print("REJECT")
    elif( count> len(old_password) or len(old_password)-len(new_password)>0 or  abs(len(old_password)-len(new_password))>2  ):
         print("REJECT")

    else:
        print("OK")
