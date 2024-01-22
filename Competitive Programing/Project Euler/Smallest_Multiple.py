import math
result=1

for i in range(1,21):
    if result>= i:
        result =(result*i)
        if  (result*i)%result==0:
           result =(result*i)//result
    else:
        result =(result*i)
        if  (result*i)%i==0:
           result =(result*i)//i


    


print(result)