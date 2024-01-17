import point

def main():
	raw_lines = []

	print("Enter Points: ")

	line = "0"
	while(line != ""):
		line = input("")
		if line != "":
			raw_lines.append(line)

	print(raw_lines)


	points = []
	for i in range(len(raw_lines)):
		raw_line = raw_lines[i]
		x = raw_line.split("<")[1].split(",")[0]
		y = raw_line.split("<")[1].split(",")[1].split(">")[0]
		xv = raw_line.split("velocity")[1].split("<")[1].split(",")[0]
		yv = raw_line.split("velocity")[1].split(",")[1].split(">")[0]
		points.append(point.Point(x,y,xv,yv))

def draw():
	minX = findMinX(points)
	maxX = findMaxX(points)
	minY = findMinY(points)
	maxY = findMaxY(points)

	for y in range(maxY, minY-1, -1):
		for x in range(minX, maxX+1):
			#if there is not a point write ". "
			#if there is a point here write "# "

#add a loop that calls move on all the points, then draws the points and keeps updating

def findMinX(points):
	min = 9999999
	for i in range(len(points)):
		if points.x < min:
			min = points.x
	return min

def findMinY(points):
	min = 9999999
	for i in range(len(points)):
		if points.y < min:
			min = points.y
	return min

def findMaxX(points):
	max = -9999999
	for i in range(len(points)):
		if points.x > max:
			max = points.x
	return max

def findMaxY(points):
	max = -9999999
	for i in range(len(points)):
		if points.y > max:
			max = points.y
	return max


if __name__ == '__main__':
	main()