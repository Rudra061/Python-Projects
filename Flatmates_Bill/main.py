import webbrowser
from fpdf import FPDF

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

    def pays(self, bill, flatmate2):

        weight = self.days_in_house / (self.days_in_house + flatmate2.days_in_house)
        to_pay = bill.amount * weight

        return to_pay




class PdfReport:
    """
        Generates a PDF report showing the amount
        to be paid by different flatmates
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):

        flatmate1_pay = str(round(flatmate1.pays(bill, flatmate2),2))
        flatmate2_pay = str(round(flatmate2.pays(bill, flatmate1),2))

        pdf = FPDF(orientation="P", unit='pt', format="A4")
        pdf.add_page()

        #add icon
        pdf.image("house.png", w=30, h=30)

        # insert title
        pdf.set_font(family="Times", size=24, style="B")
        pdf.cell(w=0, h=80, txt="Flatmates Bill", border=0, align="C", ln=1)

        #insert period label and value
        pdf.set_font(family="Times", size=14, style="B")
        pdf.cell(w=100, h=40, txt="Period", border=0, align="C")
        pdf.cell(w=120, h=40, txt=bill.period, border=0, align="C", ln=1)

        #insert the flatmate name and amount to be paid
        pdf.set_font(family="Times", size=12)
        pdf.cell(w=100, h=40, txt=flatmate1.name, border=0, align="C")
        pdf.cell(w=120, h=40, txt= flatmate1_pay, border=0, align="C", ln=1)

        pdf.cell(w=100, h=40, txt=flatmate2.name, border=0, align="C")
        pdf.cell(w=120, h=40, txt=flatmate2_pay, border=0, align="C", ln=1)

        pdf.output(self.filename)
        webbrowser.open(self.filename)


amount = float(input("Hey! enter the bill amount : "))
period = input("Enter the period E.g. May 2023 : ")

name1 = input("Enter name : ")
days_in_house1 = int(input(f"How many days {name1} stayed in house : "))

name2 = input("Enter name : ")
days_in_house2 = int(input(f"How many days {name2} stayed in house : "))

the_bill = Bill(amount, period)
flatmate1 = Flatmates(name1, days_in_house1)
flatmate2 = Flatmates(name2, days_in_house2)

print(flatmate1.pays(the_bill, flatmate2))
print(flatmate2.pays(the_bill, flatmate1))

pdf_report = PdfReport(filename=f"{the_bill.period}.pdf")
pdf_report.generate(flatmate1, flatmate2, bill=the_bill)
