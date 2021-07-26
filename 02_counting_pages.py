from fpdf import FPDF
import os
import sys

'''Create FPDF object.'''
pdf = FPDF('P', 'mm', format='A5')
pdf.set_margins(left=20, top=30, right=20)
pdf.set_font('Courier')

'''Render code.'''
with open(os.getcwd()+'/'+__file__) as f:
    txt = f.read()

pdf.add_page()
pdf.set_font_size(10)
pdf.multi_cell(160, 4, txt=txt)

'''Count pages starting with 2.'''
pdf.set_font_size(30)
for page_number in range(2,10):
    pdf.add_page()
    pdf.ln(150)
    pdf.cell(0, 0, txt=str(page_number), align='C')

'''Save PDF.'''
filename = sys.argv[0]
filename = filename.replace('.py', '.pdf')
pdf.output(filename)
