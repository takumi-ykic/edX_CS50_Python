from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.image("./shirtificate.png", 10, 60, 190)
        self.set_font("helvetica", "", 40)
        self.cell(0, 50, "CS50 Shirtificate", align="C")
        self.ln(20)

def main():
    name = input("Name: ")
    create_shirt(name)

def create_shirt(name):
    pdf = PDF()
    pdf.add_page(orientation="portrait", format="A4")
    pdf.set_font("helvetica", size=20)
    pdf.set_text_color(255,255,255)
    pdf.cell(0, 200, f"{name}", align="C")
    pdf.output("shirtificate.pdf")

if __name__ == "__main__":
    main()
