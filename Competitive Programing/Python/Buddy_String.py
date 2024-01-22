
from collections import Counter

def buddyStrings(self, s: str, goal: str) -> bool:
    count =0
    count1 =0
    if s==goal:
        return False
    else:
        
        a=Counter(s)
        b=Counter(goal)
        to_array1 = [char for char in s]
        to_array2 = [char for char in goal]
        a_key=list(a.keys())
        b_keys=list(b.keys())
        if len(a_key)!=len(to_array1):
            return False
        if len(b_keys)!=len(to_array2):
            return False
        if len(a_key)==len(b_keys):
            for i in range(0,len(b_keys)-1):
                if a.keys[i]==b.keys[i]:
                    count =count+1
                else:
                    count = count -1
            if count == len(b_keys)-1:
                for i in range(0,len(b_keys)-1):
                    if a[a.keys[i]]==b[b.keys[i]]:
                        count1 = count1+1
                    else:
                        count1 =count-1

        if count1 == len(s):
            return True       




            