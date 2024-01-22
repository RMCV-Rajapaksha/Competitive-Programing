def longestMountain(arr):
    max_val = max(arr)
    count = arr.index(max_val)

    if count !=0 and count !=len(arr)-1:
        temp = 0
        for u in range(count, len(arr) - 1):
            if arr[u] < arr[u + 1]:
                temp = u
                if temp != 0:
                    break

        temp1 = 0
        for t in range(count, 0, -1):
            if arr[t] < arr[t - 1]:
                temp1 = t
                if temp1 != 0:
                    break

        if temp1 != 0:
            print(abs(temp1 - temp) + 1)
        else:
            print(0)

    else:
        print(0)

longestMountain([1, 2, 34, 5, 6, 5, 3])
