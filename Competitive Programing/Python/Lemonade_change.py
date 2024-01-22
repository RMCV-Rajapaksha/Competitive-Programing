
def lemonadeChange( bills):
        
        cc5=0
        cc10=0
        cc20=0

        for i in bills:
            if i==5:
                cc5=cc5+1
            elif i==10:
                cc10=cc10+1
                cc5=cc5-1
            elif i==20:
                cc20=cc20+1
                cc10=cc10-1
                cc5=cc5-1
            
        if cc5>=0 and cc10>=0 and cc20>=0 :
            return True
        else:
            return False
            

print(lemonadeChange([5,5,5,5,10,5,10,10,10,20]))



        