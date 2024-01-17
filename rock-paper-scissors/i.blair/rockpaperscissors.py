# rock-paper-scissors, advent of code day 2

file = open('rock-paper-scissors/i.blair/rpsinput.txt', 'r')
f = file.readlines()
file.close()

totalScore = 0

w = 6
d = 3
l = 0

wins = ['A Y\n', 'B Z\n', 'C X\n']
draws = ['A X\n', 'B Y\n', 'C Z\n']

shapes = {
    'X': 1,
    'Y': 2,
    'Z': 3
}

for i in range (0, len(f)):
    if f[i] in wins:
        totalScore += (w + shapes[f[0][2]])
    elif f[i] in draws:
        totalScore += (d + shapes[f[0][2]])
    else:
        totalScore += (l + shapes[f[0][2]])

print('total score is: ', totalScore)