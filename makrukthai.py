from tkinter import *
from pprint import pprint


BOARD = Tk()
BOARD.geometry('650x650+200+0')
BOARD.title('Makrukthai by Uncle Games')
MAIN = Frame(BOARD)
MAIN.pack(pady=20)

blank = PhotoImage(file='blank.png')

global first
global first_image
global first_name
global chessname
first = False
first_image = None
first_name = None
chessname = None

def Clear(event=None):
	global first
	first = False
	print(first)

BOARD.bind('<Escape>',Clear)

def Select(name):
	global first
	global first_image
	global first_name
	global chessname
	first = not first
	
	
	print('NAME:',name)
	global currentimage
	currentimage = location[name]['image']
	if first == True:
		first_image = location[name]['image']
		chessname = location[name]['chessname']
		first_name = name
	else:
		#set new image
		location[name]['button'].configure(image=first_image)
		location[name]['image'] = first_image
		location[name]['chessname'] = chessname
		#clear old image
		location[first_name]['button'].configure(image=blank)
		location[first_name]['image'] = blank
		location[first_name]['chessname'] = 'blank'


	print('First: ',first)
	showtable()


global location
location = {}

columns = ['A','B','C','D','E','F','G','H']
allcode = []



for j,rw in enumerate(reversed(range(1,9))):
	rowcode = []
	for i,col in enumerate(columns):
		t = f'{col}_{rw}'
		B = Button(MAIN,text=t,image=blank,command=lambda x=t: Select(x),bg='#ffcd9c')
		rowcode.append(t)
		location[t] = {'code':t,'button':B,'image':blank,'chessname':'blank'}
		B.grid(row=j,column=i)
	allcode.append(rowcode)
	

current = StringVar()

global currentimage
currentimage = None



# top_name = ['เรือ','ม้า','โคน','เม็ด','ขุน','โคน','ม้า','เรือ']
# bottom_name = ['เรือ','ม้า','โคน','ขุน','เม็ด','โคน','ม้า','เรือ']
chess_pic = {'ruer-1':'ruer-1.png',
			 'ma-1':'ma-1.png',
			 'khon-1':'khon-1.png',
			 'med-1':'med-1.png',
			 'khun-1':'khun-1.png',
			 'ruer-2':'ruer-2.png',
			 'ma-2':'ma-2.png',
			 'khon-2':'khon-2.png',
			 'med-2':'med-2.png',
			 'khun-2':'khun-2.png',
			 'bia1-1':'bia1-1.png',
			 'bia1-2':'bia1-2.png',
			 'bia2-1':'bia2-1.png',
			 'bia2-2':'bia2-2.png'}

class Chess:
	def __init__(self,location,name):

		self.location = location # A_1
		self.name = name
		self.column = ''
		self.row = None
		self.char()

	def valid_location(push_loc,tables):
		pass

	def char(self):
		self.column = self.location.split('_')[0]
		self.row = self.location.split('_')[1]






top_name = ['ruer-1','ma-1','khon-1','med-1','khun-1','khon-1','ma-1','ruer-1']
top_name2 = ['bia1-1','bia1-1','bia1-1','bia1-1','bia1-1','bia1-1','bia1-1','bia1-1']
bottom_name2 = ['bia1-2','bia1-2','bia1-2','bia1-2','bia1-2','bia1-2','bia1-2','bia1-2']
bottom_name = ['ruer-2','ma-2','khon-2','khun-2','med-2','khon-2','ma-2','ruer-2']

# สร้างแถวหมาก (ดำ)
for c,n in zip(allcode[0],top_name):
	#print('IMAGE_BEFORE:',location[c]['image'])
	location[c]['chessname'] = n
	location[c]['image'] = PhotoImage(file=chess_pic[n])
	location[c]['button'].configure(image=location[c]['image'])
# สร้างแถวเบี้ย (ดำ)
for c,n in zip(allcode[2],top_name2):
	#print('IMAGE_BEFORE:',location[c]['image'])
	location[c]['chessname'] = n
	location[c]['image'] = PhotoImage(file=chess_pic[n])
	location[c]['button'].configure(image=location[c]['image'])	

# สร้างแถวเบี้ย (แดง)
for c,n in zip(allcode[5],bottom_name2):
	#print('IMAGE_BEFORE:',location[c]['image'])
	location[c]['chessname'] = n
	location[c]['image'] = PhotoImage(file=chess_pic[n])
	location[c]['button'].configure(image=location[c]['image'])	

# สร้างแถวหมาก (แดง)
for c,n in zip(allcode[7],bottom_name):
	#print('IMAGE_BEFORE:',location[c]['image'])
	location[c]['chessname'] = n
	location[c]['image'] = PhotoImage(file=chess_pic[n])
	location[c]['button'].configure(image=location[c]['image'])


print('--------SHOW LOC---------')


def showtable():

	allrow = []
	row = []
	count = 0
	for i,l in enumerate(location.values(),start=0):
		#print(l['code'],l['chessname'])
		if l['chessname'] != 'blank':
			row.append(l['chessname'])
		else:
			row.append('-')

		if count == 7:
			print('ROW ADD:',row)
			allrow.append(row)
			row = []
			count = 0
			#count += 1
		else:
			count += 1

	bd = '|' + f'{"-"*10:^{10}}'
	border = bd * 8 + '|'
	result = [border]
	for rw in allrow:
		rowtext = ''
		for i,r in enumerate(rw,start=0):
			text = '|'+ f'{r:^{10}}'
			rowtext += text 
		tx = '|' + f'{" ":^{10}}'
		bd = '|' + f'{"-"*10:^{10}}'
		blankline = tx * 8 + '|'
		border = bd * 8 + '|'
		result.append(blankline)
		result.append(blankline)
		result.append(rowtext + '|')
		result.append(blankline)
		result.append(border)
	for r in result:
		print(r)
	

showtable()

BOARD.mainloop()