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

'''Sum up pages starting with 2.'''
pdf.set_font_size(30)
for page_number in range(2,10):
    pdf.add_page()
    pdf.ln(50)
    txt = '1' # store calculation
    for i in range(2, page_number+1):
        txt += ' + 1'
    txt += ' =\n' + str(page_number)
    pdf.multi_cell(w=148-40, h=20, txt=txt, align='C')

'''Save PDF.'''
filename = sys.argv[0]
filename = filename.replace('.py', '.pdf')
pdf.output(filename)
