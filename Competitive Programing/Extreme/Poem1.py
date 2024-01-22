n, m = list(map(int, input().split()))

scheme = []
poem = []


for _ in range(n):
    scheme.append(set(input().strip().split()))  

input()  


for _ in range(m):
    poem.append(input().strip())

def find_rhyme_scheme(scheme, poem):
    rhyme_scheme = []

    for line in poem:
        found = False

        for i, rhyming_words in enumerate(scheme):
            if line.lower() in rhyming_words:
                if i < len(rhyme_scheme):
                    rhyme_scheme.append(rhyme_scheme[i])
                else:
                    rhyme_scheme.append(chr(65 + len(rhyme_scheme) - len(set(rhyme_scheme))))
                found = True
                break

        if not found:
            rhyme_scheme.append('X')

    return rhyme_scheme


rhyme_scheme = find_rhyme_scheme(scheme, poem)


print(''.join(rhyme_scheme))
