scores_1 = {"A X":4, "A Y":8, "A Z":3, "B X":1, "B Y":5, "B Z":9, "C X":7, "C Y":2, "C Z":6}
scores_2 = {"A X":3, "A Y":4, "A Z":8, "B X":1, "B Y":5, "B Z":9, "C X":2, "C Y":6, "C Z":7}
lines = None
score_1 = 0
score_2 = 0
with open('input.txt') as f:
    lines = f.readlines()

for line in lines:
    score_1 += scores_1[line.strip()]
    score_2 += scores_2[line.strip()]
print (score_1)
print (score_2)