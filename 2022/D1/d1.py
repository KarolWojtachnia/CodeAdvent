
lines = None
index = 1
scores = []
score = 0

with open('input.txt') as f:
    lines = f.readlines()

for id, line in enumerate(lines):
    if len(line.strip()) == 0 :
        scores.append(score)
        score = 0
        index += 1
        print (index)
    else:
        line.strip
        print(f"{id}) {line} {type(line)}")
        
        score += int(line)

scores.sort()
print(f"BEST: {scores[-1]}")
print(f"SUM OF 3 BEST: {scores[-1]+scores[-2]+scores[-3]}")
