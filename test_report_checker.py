import io
from unittest.mock import patch

from report import Report
from report_checker import check_report
from test_report_repository import ReportRepository


class TestReportChecker:
    def test_multiple_reports_at_one_report_file(self):
        expected_secure_reports = 2
        repository__reports = [
            Report([7, 6, 4, 2, 1]),
            Report([1, 2, 7, 8, 9]),
            Report([9, 7, 6, 2, 1]),
            Report([1, 3, 2, 4, 5]),
            Report([8, 6, 4, 4, 1]),
            Report([1, 3, 6, 7, 9])
        ]

        with patch.object(ReportRepository, 'get_all', return_value=repository__reports):
            assert expected_secure_reports == check_report(ReportRepository("a_file_that_does_not_exist"))

