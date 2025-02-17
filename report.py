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

            is_between_bounds = 0 < abs(level_difference) < 4
            if not is_between_bounds:
                return False
        return True

    def _is_increasing(self):
        if self.levels[0] > self.levels[1]:
            return False
        if self.levels[0] < self.levels[1]:
            return True