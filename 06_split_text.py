from fpdf import FPDF
import os
import sys
import requests

'''Create FPDF object.'''
pdf = FPDF('P', 'mm', format='A5')
pdf.set_margins(left=20, top=20, right=20)
pdf.set_font('Courier')

'''Render code.'''
with open(os.getcwd()+'/'+__file__) as f:
    txt = f.read()

pdf.add_page()
pdf.set_font_size(10)
pdf.multi_cell(148-40, 4, txt=txt, align='L')

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
pdf.multi_cell(w=148-40, h=5, txt=txt, align='L')

'''Save PDF.'''
filename = sys.argv[0]
filename = filename.replace('.py', '.pdf')
pdf.output(filename)
