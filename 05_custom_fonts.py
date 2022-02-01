from fpdf import FPDF
import os
import sys

'''Create FPDF object.'''

pdf = FPDF('P', 'mm', format='A5')
pdf.set_margins(left=20, top=20, right=20)
pdf.set_font('Courier')


'''Render code.'''

filename = sys.argv[0]
with open(filename) as f:
    txt = f.read()

pdf.add_page()
pdf.set_font_size(10)
pdf.multi_cell(0, None, txt=txt)


'''Render text in different fonts.'''

pdf.add_page()
pdf.set_font_size(14)
path = 'fonts/'
fonts = os.listdir(path)
fonts = [font for font in fonts if font.endswith('.ttf')]
for font in fonts:
    font_name = font[:-4]
    txt = 'The quick brown fox jumps over the lazy dog'
    txt += '\n(' + font_name + ')'
    pdf.add_font(font_name, '', path+font, uni=True)
    pdf.set_font(font_name)
    pdf.multi_cell(w=148-40, h=5, txt=txt, align='L')
    pdf.ln(9)


'''Save PDF.'''

filename = filename.replace('.py', '.pdf')
pdf.output('pdf/' + filename)
