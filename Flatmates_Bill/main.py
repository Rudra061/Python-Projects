class Bill:
    """
        Object that contains data about a bill, such as
        total amount and period of a bill
    """

    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class Flatmates:
    """
        Creates a flatmate person who lives in the
        flat and pays a share of the bill
    """

    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill):
        pass