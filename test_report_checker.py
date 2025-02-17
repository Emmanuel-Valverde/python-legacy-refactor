import io

from report_checker import check_report


class TestReportChecker:
    def test_multiple_reports_at_one_report_file(self):
        expected_secure_reports = 2
        report_file = io.StringIO("""7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9""")


        assert expected_secure_reports == check_report()

