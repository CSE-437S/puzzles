import re
with open('/Users/tarek/puzzles/puzzles_done/puzzles/elbialy.t/starsalign.txt') as f:
    Lines = f.readlines()
dict={}
for line in Lines:
    new_s = re.findall('[-+]?\d+', line.replace(' ', ''))
    a,b,c,d =new_s
    dict[int(a),int(b)] = {int(c),int(d)}
for r in range(22):
    for c in range(16):
        my_tuple = (r-11, c-8)
        if dict.get(my_tuple) is not None:
            print(" # ", end = '')
        else:
            print(" . ", end = '')
    print()
print(dict)