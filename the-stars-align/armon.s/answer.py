class Star:
    def __init__(self, xpos, ypos, xv, yv):
        self.xpos = xpos
        self.ypos = ypos
        self.xv = xv
        self.yv = yv
    def update(self):
        self.xpos +=self.xv
        self.ypos+= self.yv
        
import sys

path = sys.argv[1]
file = open(path, 'r')
stars = []
while True:
    content = file.readline()
    if not content:
        break
    stars.add(Star(content[10:16], content[18:24], content[36:38], content[39:42]))
    break

while True:
    stars.sort(key = lambda star: (star.ypos, star.xpos))
