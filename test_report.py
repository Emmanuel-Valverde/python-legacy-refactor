class Report:
    def __init__(self, levels):
        self.levels = levels

    def is_safe(self) -> bool:

        for indice in range(len(self.levels) - 1):
            next_level = self.levels[indice + 1]
            current_level = self.levels[indice]
            level_difference = next_level - current_level

            if self._is_increasing() and level_difference < 0:
                return False
        return True

    def _is_increasing(self):
        if self.levels[0] > self.levels[1]:
            return False
        if self.levels[0] < self.levels[1]:
            return True


class TestReport:
    def test_given_a_report_when_levels_decrease_on_one_or_two_per_level_then_the_report_is_secure(self):
        report = Report([7, 6, 4, 2, 1])

        assert True == report.is_safe()

    def test_given_a_report_when_levels_increase_and_decrease_then_the_report_is_unsecure(self):
        report = Report([1, 3, 2, 4, 5])

        assert False == report.is_safe()

    def test_given_an_increasing_report_when_levels_increase_over_five_levels_then_the_report_is_unsecure(self):
        report = Report([1, 2, 7, 8, 9])

        assert False == report.is_safe()