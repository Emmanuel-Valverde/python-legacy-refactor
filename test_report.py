class Report:
    def __init__(self, report_data):
        self.report_data = report_data

    def is_safe(self) -> bool:
        return True


class TestReport:
    def test_given_a_report_when_levels_decrease_on_one_or_two_per_level_then_the_report_is_secure(self):
        report = Report([7, 6, 4, 2, 1])

        assert True == report.is_safe()

    def test_given_a_report_when_levels_increase_and_decrease_then_the_report_is_unsecure(self):
        report = Report([1, 3, 2, 4, 5])

        assert False == report.is_safe()