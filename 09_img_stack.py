from fpdf import FPDF
import random
from PIL import Image
import glob
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


'''Add an image on top on each new page.'''

pdf.set_margins(left=0, top=0, right=0)
stack = []
images = glob.glob('images/*')

for img_path in images:
    # img_path = 'images/' + image
    img = Image.open(img_path)
    w, h = img.size
    size_factor = random.randint(1,5)/15
    w = int(w * size_factor)
    h = int(h*size_factor)
    x = random.randint(-30,80)
    y = random.randint(-30,150)
    stack.append({'img_path':img_path, 'w':w, 'h':h, 'x':x, 'y':y})

for i in range(len(stack)):
    pdf.add_page()
    for j in range(i+1):
        d = stack[j]
        pdf.image(d.get('img_path'), x=d.get('x'), y=d.get('y'),
            w=d.get('w'), h=d.get('h'))


'''Save PDF.'''

filename = filename.replace('.py', '.pdf')
pdf.output('pdf/' + filename)
