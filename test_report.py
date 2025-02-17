from report import Report


class TestReport:
    def test_given_a_report_when_levels_decrease_on_one_or_two_per_level_then_the_report_is_secure(self):
        report = Report([7, 6, 4, 2, 1])

        assert True == report.is_safe()
        
    def test_given_a_report_when_levels_increase_between_the_boundaries_then_the_report_is_secure(self):
        report = Report([1, 3, 6, 7, 9])

        assert True == report.is_safe()

    def test_given_a_report_when_levels_increase_and_decrease_then_the_report_is_unsecure(self):
        report = Report([1, 3, 2, 4, 5])

        assert False == report.is_safe()

    def test_given_an_increasing_report_when_levels_increase_over_five_levels_then_the_report_is_unsecure(self):
        report = Report([1, 2, 7, 8, 9])

        assert False == report.is_safe()

    def test_given_an_decreasing_report_when_levels_decrease_over_four_levels_then_the_report_is_unsecure(self):
        report = Report([9, 7, 6, 2, 1])

        assert False == report.is_safe()

    def test_given_a_report_when_levels_do_not_decrease_or_increase_then_the_report_is_unsecure(self):
        report = Report([8, 6, 4, 4, 1])

        assert False == report.is_safe()