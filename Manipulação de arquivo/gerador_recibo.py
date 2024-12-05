from fpdf import FPDF
from num2words import num2words
from datetime import date


cliente = input("digite o nome do paciente\n")
consulta = input("Informe o tipo da consulta\n")
valor = int(input("Informe o valor da consulta\n"))


valor_msg = f"{valor} reais"
valor_extenso = num2words(float(valor), lang='pt-br')
valor_extenso_msg = f"{valor_extenso} reais"
data = date.today()
day = data.day
month = data.month
year = data.year

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial","",20)
pdf.image("rec.jpg",x=0,y=0)
pdf.text(162,45,valor_msg)
pdf.text(80,86,cliente)
pdf.text(80,108, valor_extenso_msg)
pdf.text(80,135, consulta)
pdf.set_text_color(255,255,255)
pdf.text(30,193,str(day))
pdf.text(50,193,str(month))
pdf.text(70,193,str(year))
pdf.output(f"recibo do {cliente}-{str(day)}-{str(month)}-{str(year)}.pdf")
print("gerado com sucesso")

