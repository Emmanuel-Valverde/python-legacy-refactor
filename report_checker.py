from io import StringIO

from report import Report
from test_report_repository import ReportRepository


# TODO: Remove StringIO dependency and encapsulate reding of the file on a repository
def check_report(report_repository: ReportRepository = ReportRepository("input.txt")):
	count = 0
	reports = report_repository.get_all()
	for report in reports:
		if report.is_safe():
			count += 1
	return count

if __name__ == "__main__":
	print(check_report())