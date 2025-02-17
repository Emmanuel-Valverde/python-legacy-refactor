from io import StringIO

def check_report(reports_file: StringIO):
	count = 0
	for report in reports_file:
		levels = list(map(int, report.split()))

		if levels[0] > levels[1]:
			increases = -1
			is_report_increasing = False

		if levels[0] < levels[1]:
			increases = 1
			is_report_increasing = True

		if is_report_valid(increases, levels, is_report_increasing):
			count += 1
	return count


def is_report_valid(increases, levels, is_report_increasing):
	for indice in range(len(levels) - 1):
		next_level = levels[indice + 1]
		current_level = levels[indice]
		level_difference = next_level - current_level

		if is_report_increasing and level_difference < 0:
			return False

		is_between_bounds = 0 < abs(level_difference) < 4
		if is_between_bounds:
			t = True
		else:
			t = False
			break
	return t


if __name__ == "__main__":
	with open("input.txt", "r") as file:
		print(check_report(file))