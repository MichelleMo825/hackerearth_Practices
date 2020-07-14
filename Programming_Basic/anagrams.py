cases = int(input())
result = ''
for _ in range(0, cases):
    a = list(input())
    b = list(input())
    adict = dict()
    bdict = dict()
    chars = set(a + b)

    for c in chars:
        adict[c] = 0
        bdict[c] = 0
    for i in a:
        adict[i] += 1
    for j in b:
        bdict[j] += 1
    
    diff = 0

    for c in chars:
        if(abs(adict[c] - bdict[c]) != 0):
            diff += abs(adict[c] - bdict[c])


    result = result + str(diff) + '\n'

print(result) 