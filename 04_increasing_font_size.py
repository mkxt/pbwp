from fpdf import FPDF
import os
import sys

'''Create FPDF object.'''

pdf = FPDF('P', 'mm', format='A5')
pdf.set_margins(left=20, top=30, right=20)
pdf.set_font('Courier')


'''Render code.'''

filename = sys.argv[0]
with open(filename) as f:
    txt = f.read()

pdf.add_page()
pdf.set_font_size(10)
pdf.multi_cell(0, None, txt=txt)


'''Render page number in corresponding pt.'''

for page_number in range(2,101):
    pdf.add_page()
    pdf.ln(150)
    pdf.set_font_size(page_number)
    txt = str(page_number)
    pdf.multi_cell(0, None, txt=txt, align='R')


'''Save PDF.'''

filename = filename.replace('.py', '.pdf')
pdf.output('pdf/' + filename)
