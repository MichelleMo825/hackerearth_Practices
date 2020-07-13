

def getFacingSeatAndType(n):
    
    factor = int(n / 12)
    seat = n % 12
    if seat == 0:
        seat = 12
        factor = factor - 1
    
    facing = (13 - seat) + factor * 12
    remainder = seat % 6
   
    if remainder == 2 or remainder == 5:
        return str(facing) + ' ' + 'MS\n'
    if remainder == 3 or remainder == 4:
        return str(facing) + ' ' + 'AS\n'
    
    return str(facing) + ' ' + 'WS\n'


cases = int(input())
result = ''
for i in range (0, cases):
    number = int(input())
    result = result + getFacingSeatAndType(number)
print(result)