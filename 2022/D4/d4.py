lines=None
with open('input.txt') as f:
    lines = f.readlines()
score_includes=0
score_overlaps=0

for line in lines:
    overlaps=False
    includes=False
    line=line.strip()
    elves = line.split(',')
    elf1=elves[0].split('-')
    elf2=elves[1].split('-')
    if (int(elf1[0]) >= (int(elf2[0])) and int(elf1[1]) <= (int(elf2[1]))):
        score_includes += 1
        score_overlaps += 1
    elif (int(elf1[0]) <= (int(elf2[0])) and int(elf1[1]) >= (int(elf2[1]))):
        score_includes += 1
        score_overlaps += 1
    elif (int(elf2[0]) >= (int(elf1[0])) and int(elf2[0]) <= (int(elf1[1]))):
        score_overlaps += 1
        overlaps = True

    elif(int(elf2[1]) >= (int(elf1[0])) and int(elf2[1]) <= (int(elf1[1]))):
        score_overlaps += 1
        overlaps = True
    # elif(int(elf1[0]))
    print(f"{line} {overlaps}")

print (score_includes)
print (score_overlaps)