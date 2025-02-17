from report import Report


class ReportRepository:
    def __init__(self, report_file):
        self.report_file = report_file

    def get_all(self) -> list[Report]:
        with open(self.report_file, "r") as file:
            reports = []
            for report in file:
                levels = list(map(int, report.split()))
                reports.append(Report(levels))

            return reports


class TestReportRepository:
    def test_get_all_the_reports(self):
        expected_reports = [
            Report([7, 6, 4, 2, 1]),
            Report([1, 2, 7, 8, 9]),
            Report([9, 7, 6, 2, 1]),
            Report([1, 3, 2, 4, 5]),
            Report([8, 6, 4, 4, 1]),
            Report([1, 3, 6, 7, 9])
        ]
        report_repository = ReportRepository("fixture_input.txt")


        assert expected_reports == report_repository.get_all()