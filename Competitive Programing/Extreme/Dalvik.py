
v0 = 10  
v1 = 5   
v2 = 20  
v3 = 1


v4 = v3 - v3
v5 = v4 - v3
v6 = v3
v7 = v4
v7 -= v1
v8 = v0
v9 = v0
v9 += v1
v10 = v4
v11 = v4
v12 = v3

while True:
    v11 += v1
    v10 += v0
    v13 = v10
    v14 = v4
    v15 = v4

  
    while True:
        v16 = v13 + v13
        if v16 <= v1:
            break
        v13 -= v1
        v14 += v3
        v15 += v1

   
    if v13 <= v4:
        v13 = v4

    v17 = v4
    v18 = v3

 
    while True:
        v17 += v13
        v18 += v3
        if v18 <= v6:
            break

    v18 = v3

   
    while True:
        v17 -= v9
        v18 += v3
        if v18 <= v12:
            break

    if v17 >= v4:
        v5 = v14
        v6 = v12
        v7 = v15
        v8 = v10
        v9 = v13

    v12 += v3
    if v12 <= v2:
        continue

    break


print(v6)  
