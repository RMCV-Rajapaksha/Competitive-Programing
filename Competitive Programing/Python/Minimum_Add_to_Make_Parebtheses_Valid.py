
def minAddToMakeValid(s):
    
    
    a=''
    a1=''
    c=0
    c1=0
    l=len(a)
    y=0
    y1=0
    ys=0
    if s[1]=='(':
        for i in s:
            if(s=='('):
                a=a+i
                c=c+1
            if c>0 and s==')':
                break

        for u in range(c-1,l-c):
            if s[u]==')':
                y=y+1
            if s[u]=='(':
                break
        if c<=y:
            return c
        elif c>=y:
            return y
        

    else:
        for i in s:
            if i==')':
                a1=a1+i
                c1=c1+1
            if c1>0 and s=='(':
                break
        for u in range(c1-1,l-c1):
            if s[u]=='(':
                y1=y1+1
            if s[u]==')':
                break

        for u in range(c-1,l-c):
            if s[u]==')':
                ys=ys+1
            if s[u]=='(':
                break


        if y1<=ys:
            return y1
        elif c1>=ys:
            return ys



    
    



    

        