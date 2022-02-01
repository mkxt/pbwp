from fpdf import FPDF
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


'''Render an image with increasing size.'''

img_path = 'images/Ghostscript_Tiger.png'
size = 1

for i in range(14):
    pdf.add_page()
    pdf.image(img_path, x = (148-size)/2, y = (210-size)/2, w = size, h = size)
    size *= 2


'''Save PDF.'''

filename = filename.replace('.py', '.pdf')
pdf.output('pdf/' + filename)
