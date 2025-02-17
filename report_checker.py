from io import StringIO

def check_report(reports_file: StringIO):
	count = 0
	for report in reports_file:
		levels = list(map(int, report.split()))

		if levels[0] > levels[1]:
			increases = -1

		if levels[0] < levels[1]:
			increases = 1


		for indice in range(len(levels) - 1):
			next_level = levels[indice + 1]
			current_level = levels[indice]

			if 0 < (next_level - current_level) * increases < 4:
				t = True
			else:
				t = False
				break

		if t:
			count += 1
	return count



if __name__ == "__main__":
	with open("input.txt", "r") as file:
		print(check_report(file))