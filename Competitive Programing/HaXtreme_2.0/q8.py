
def binaryTodecimal(n, exp = 1):
    if n == 0:
        return 0
    rem = n%10
    rem = rem*exp
    return rem + binaryTodecimal(n//10,exp*2)


initial = "110100.111001.110010"
if len(initial) != 3:
 int(initial).extend(["000000"] * (3 - len(initial)))

x, y, z = initial
x1=str(x)
y1=str(y)
z1=str(z)

x11=x1[:2]
x12=x1[3:]

y11=y1[:2]
y12=y1[3:]

z11=z1[:2]
z12=z1[3:]

numx1 = int(int(x11), 2)
numx2 = int(int(x12), 2)
numx3 = int(int(y11), 2)
numx4 = int(int(y12), 2)
numx5 = int(int(z11), 2)
numx6 = int(int(z12), 2)

u1=str(numx1)+str(numx2)
u2=str(numx3)+str(numx4)
u3=str(numx5)+str(numx6)

print(u1+"-"+u2+"-"+u3)

