import webbrowser

from fpdf import FPDF


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
