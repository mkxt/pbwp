from fpdf import FPDF
import os
import sys

'''Create FPDF object.'''
pdf = FPDF('P', 'mm', format='A5')
pdf.set_margins(left=20, top=20, right=20)
pdf.set_font('Courier')

'''Render code.'''
with open(os.getcwd()+'/'+__file__) as f:
    txt = f.read()

pdf.add_page()
pdf.set_font_size(10)
pdf.multi_cell(148-40, 4, txt=txt)

'''Render text in different fonts.'''
pdf.add_page()
pdf.set_font_size(14)
fonts = os.listdir(os.getcwd()+'/fonts')
fonts = [font for font in fonts if font.endswith('.ttf')]
for font in fonts:
    font_name = os.path.splitext(font)[0]
    font_path = 'fonts/' + font
    txt = 'The quick brown fox jumps over the lazy dog'
    txt += '\n(' + font_name + ')'
    pdf.add_font(font_name, '', font_path, uni=True)
    pdf.set_font(font_name)
    pdf.multi_cell(w=148-40, h=5, txt=txt, align='L')
    pdf.ln(9)

'''Save PDF.'''
filename = sys.argv[0]
filename = filename.replace('.py', '.pdf')
pdf.output(filename)
