def main():

	rows = []
	score = 0

	raw_line = "00"
	print("Enter Lines:")
	while(raw_line != ""):
		
		raw_line = input("")
		if raw_line != "":
			rows.append(raw_line)

	for i in range(len(rows)):
		arr = rows[i].split(" ")
		first = arr[0]
		last = arr[1]

		if last == "X": #rock
			score += 1
			if first == "A":
				score += 3
			elif first == "C":
				score += 6
		elif last == "Y": #paper
			score += 2
			if first == "B":
				score += 3
			elif first == "A":
				score += 6
		else: #scissor
			score += 3
			if first == "C":
				score += 3
			elif first == "B":
				score += 6
	print(f"Score: {score}")





if __name__ == '__main__':
	main()
