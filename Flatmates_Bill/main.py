from flats import Bill, Flatmates
from reports import PdfReport

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
