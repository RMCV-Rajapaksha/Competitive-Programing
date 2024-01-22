
input_string = input().strip()
input_list = list(map(int, input_string.split()))


def find_largest_index(lst):
    largest = max(lst)
    index = lst.index(largest)
    return index

i=find_largest_index(input_list)
sum = 0

for x in range(0, len(input_list), 1):
    if x< i-2:
        sum = sum + input_list[x]
    elif x>i:
        sum = sum + input_list[x]
    else:
        sum = input_list[i]*(input_list[i-1]+input_list[i-2])

print(sum)