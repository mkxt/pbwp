from fpdf import FPDF
import os
import sys
import random

'''Create FPDF object.'''
pdf = FPDF('P', 'mm', format='A5')
pdf.set_margins(left=20, top=20, right=20)
pdf.set_font('Courier')
pdf.set_draw_color(0)

'''Render code.'''
with open(os.getcwd()+'/'+__file__) as f:
    txt = f.read()

pdf.add_page()
pdf.set_font_size(10)
pdf.multi_cell(148-40, 4, txt=txt)

''' Render lines from top to bottom.'''
pdf.set_margin(0)
line_width = 2
pdf.set_draw_color(0, 80, 180)
pdf.set_line_width(line_width)
# A5 = 148 x 210 mm
y = 0
while y <= 210:
    pdf.add_page()
    pdf.line(x1=0, y1=y, x2=148, y2=y)
    y += line_width

'''Save PDF.'''
filename = sys.argv[0]
filename = filename.replace('.py', '.pdf')
pdf.output(filename)
