word = raw_input()

zs = word.replace('o', '')
os = word.replace('z', '')

if len(zs) * 2 == len(os):
    print('Yes')
else:
    print('No')
