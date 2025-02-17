from test_report_repository import ReportRepository


def check_report(report_repository: ReportRepository):
	reports = report_repository.get_all()
	safe_reports = [report for report in reports if report.is_safe()]
	return len(safe_reports)


if __name__ == "__main__":
	print(check_report(ReportRepository("input.txt")))