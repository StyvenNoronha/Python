from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font('Arial','B',18)
pdf.cell(40,10,'Hello World')
pdf.output('exemplo.pdf', 'F')