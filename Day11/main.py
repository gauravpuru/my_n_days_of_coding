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


    def pays(self,bill, Flatmate2):
        weight = self.days_in_house/(self.days_in_house + Flatmate2.days_in_house)
        to_pay = bill.amount * weight
        return to_pay

class PdfReport:
    """
    create a pdf file that contains data about the flatmates such as
    thier names, their due amount and the period of their bill
    """
    def __init__(self,filename):
        self.filename = filename

    def generate(self,flatmate1, flatmate2, bill):
        pass



the_bill = Bill(amount=120, period="March 2021")
john = Flatmate(name="John", days_in_house= 20)
merry = Flatmate(name="Merry",days_in_house=25)

print(john.pays(the_bill,merry))
print(merry.pays(the_bill,john))