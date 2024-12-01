lines = None
score = 0
score_2 = 0
with open('input.txt') as f:
    lines = f.readlines()

def getValue(letter):
    if letter == '':
        return 0
    value = ord(letter)
    if (value>96):
        return value-96
    else:
        return value-38

# print (getValue('A'))
# print (getValue('a'))
# half = int(len(lines[0].strip())/2)
# print(half)
# print(lines[0][:half])
for i, line in enumerate(lines):
    
    half = (len(line.strip())/2)-1
    a = line[:int(half)+1].strip()
    b = line[int(half)+1:].strip()
    common = ''
    for w in set(a):
        if w in b:
            common += w
    value = getValue(common)
    score+=getValue(common)
    print(f'{i} {line.strip()} {a} {b} {common} {value}')

i=0
while i+2 < len(lines):
    a, b, c = lines[i].strip(), lines[i+1].strip(), lines[i+2].strip()
    common = ''.join(set(a).intersection(b))
    common = ''.join(set(common).intersection(c))
    score_2+=getValue(common)
    i+=3


print (score)
print(score_2)