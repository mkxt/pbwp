from fpdf import FPDF
import sys


'''Create FPDF object.'''

pdf = FPDF('P', 'mm', format='A5') # 148 x 210 mm
pdf.set_margins(left=20, top=20, right=20)
pdf.set_font('Courier')


'''Render code.'''

filename = sys.argv[0]
with open(filename) as f:
    txt = f.read()

pdf.add_page()
pdf.set_font_size(10)
pdf.multi_cell(0, None, txt=txt)


''' Render lines from top to bottom.'''

pdf.set_margin(0)
line_width = 4
pdf.set_draw_color(0, 80, 180)
pdf.set_line_width(line_width)

y = 0
while y < (210 + line_width):
    pdf.add_page()
    pdf.line(x1=0, y1=y, x2=148, y2=y)
    y += line_width


'''Save PDF.'''

filename = filename.replace('.py', '.pdf')
pdf.output('pdf/' + filename)
