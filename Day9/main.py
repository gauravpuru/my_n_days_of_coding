class Bill:
    """
    Objects that contains the data about a bill, such as total amount
    and the period of the Bill.
    """
    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class Flatmate:
    """
    A person who lives in the flat and pays a
    share of the bill.
    """
    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self,bill):
        pass

class PdfReport:
    """
    create a pdf file that contains data about the flatmates such as
    thier names, their due amount and the period of their bill
    """
    def __init__(self,filename):
        self.filename = filename

    def generate(self,flatmate1, flatmate2, bill):
        pass
