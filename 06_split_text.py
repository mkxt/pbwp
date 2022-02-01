from fpdf import FPDF
import os
import sys
import requests

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


'''Request http content.'''

url = 'https://loremipsum.de/downloads/original.txt'
r = requests.get(url)
txt = r.text


'''Render text with increasing spaces.'''

word_list = txt.split(' ')
txt = ''
for index, word in enumerate(word_list):
    txt += ' ' * index
    txt += word

pdf.add_page()
pdf.add_font('Vollkorn', '', 'fonts/Vollkorn-Regular.ttf', uni=True)
pdf.set_font('Vollkorn')
pdf.multi_cell(w=0, h=5, txt=txt, align='L')


'''Save PDF.'''

filename = filename.replace('.py', '.pdf')
pdf.output('pdf/' + filename)
