def calculate_line_equation(x1, y1, x2, y2, distance):
   
    m = (y2 - y1) / (x2 - x1)
    
    c = y1 - m * x1
    

    m = round(m, 2)
    c = round(c, 2)
    
 
    return f"y = {m}x + {c}"

import re

input_string = input().strip()
split_data = re.split('[ ,]', input_string)
input_data = [(int(split_data[i]), int(split_data[i+1]), int(split_data[i+2])) for i in range(0, len(split_data), 3)]


for x in range(0, len(input_data), 1):
    (x,y,distance)= input_data[x]
    (x1,y1,distance1)= input_data[x+1]
    result = calculate_line_equation(x, y, x1, y1, distance)
    

