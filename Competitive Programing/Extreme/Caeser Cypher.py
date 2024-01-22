

import math
import os
import random
import re
import sys

def caesarCipher(s, k):
   

    ans=""
    a=ord("a")
    z=ord("z")
    A=ord("A")
    Z=ord("Z")
    val=k%26
    for i in s:
        c=ord(i)
        if A<=c<=Z:
            if c+val<=Z:
                ans+=chr(c+val)
            else:
                ans+=chr(c+val-Z+A-1)
        elif a<=c<=z:
            if c+val<=z:
                ans+=chr(c+val)
            else:
                ans+=chr(c+val-z+a-1)
        else:
            ans+=chr(c) 
    return ans
        


if __name__ == '__main__':

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    print(result)

