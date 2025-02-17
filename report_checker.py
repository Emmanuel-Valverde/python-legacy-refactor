from io import StringIO

from report import Report


def check_report(reports_file: StringIO):
	count = 0
	for report in reports_file:
		levels = list(map(int, report.split()))

		report = Report(levels)

		if report.is_safe():
			count += 1
	return count

if __name__ == "__main__":
	with open("input.txt", "r") as file:
		print(check_report(file))