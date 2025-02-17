class Report:
    def __init__(self, report_data):
        self.report_data = report_data

    def is_safe(self) -> bool:
        return True


class TestReport:
    def test_given_a_report_where_levels_decrease_on_one_or_two_per_level_then_the_report_is_secure(self):
        report = Report([7, 6, 4, 2, 1])

        assert True == report.is_safe()

