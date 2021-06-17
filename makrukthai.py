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
first = False
first_image = None
first_name = None

def Clear(event=None):
	global first
	first = False
	print(first)

BOARD.bind('<Escape>',Clear)



def Select(name):
	global first
	global first_image
	global first_name
	first = not first
	name = name.strip()
	
	print(name)
	global currentimage
	currentimage = location[name]['image']
	if first == True:
		first_image = location[name]['image']
		first_name = name
	else:
		#set new image
		location[name]['button'].configure(image=first_image)
		location[name]['image'] = first_image
		#clear old image
		location[first_name]['button'].configure(image=blank)
		location[first_name]['image'] = blank


	print('First: ',first)

allboard = {}

location = {}

rowname = ['A','B','C','D','E','F','G','H']
allcode = []
for j,rw in enumerate(rowname):
	row = []
	rowcode = []
	for i in range(8):
		t = f'{rw}_{i}'
		tname = f'{t:^{15}}'
		B = Button(MAIN,text=tname,image=blank,command=lambda x=t: Select(x),bg='#ffcd9c')
		row.append(B)
		rowcode.append(t)
		location[t] = {'code':t,'button':B,'image':blank,'chessname':''}
		B.grid(row=j,column=i)
	allboard[rw] = row
	allcode.append(rowcode)

pprint(location)

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

top_name = ['ruer-1','ma-1','khon-1','med-1','khun-1','khon-1','ma-1','ruer-1']
top_name2 = ['bia1-1','bia1-1','bia1-1','bia1-1','bia1-1','bia1-1','bia1-1','bia1-1']
bottom_name2 = ['bia1-2','bia1-2','bia1-2','bia1-2','bia1-2','bia1-2','bia1-2','bia1-2']
bottom_name = ['ruer-2','ma-2','khon-2','med-2','khun-2','khon-2','ma-2','ruer-2']

# สร้างแถวหมาก (ดำ)
for c,n in zip(allcode[0],top_name):
	print('IMAGE_BEFORE:',location[c]['image'])
	location[c]['image'] = PhotoImage(file=chess_pic[n])
	location[c]['button'].configure(image=location[c]['image'])
# สร้างแถวเบี้ย (ดำ)
for c,n in zip(allcode[2],top_name2):
	print('IMAGE_BEFORE:',location[c]['image'])
	location[c]['image'] = PhotoImage(file=chess_pic[n])
	location[c]['button'].configure(image=location[c]['image'])	

# สร้างแถวเบี้ย (แดง)
for c,n in zip(allcode[5],bottom_name2):
	print('IMAGE_BEFORE:',location[c]['image'])
	location[c]['image'] = PhotoImage(file=chess_pic[n])
	location[c]['button'].configure(image=location[c]['image'])	

# สร้างแถวหมาก (แดง)
for c,n in zip(allcode[7],bottom_name):
	print('IMAGE_BEFORE:',location[c]['image'])
	location[c]['image'] = PhotoImage(file=chess_pic[n])
	location[c]['button'].configure(image=location[c]['image'])

'''
for i,nm in enumerate(top_name):
	chessname = nm
	#allboard['A'][i].configure(text=f'{chessname: ^{15}}')
	allboard['A'][i].configure(command=lambda x=chessname: Select(x))
	#allboard['A'][i].configure(image=img)
	

# img = PhotoImage(file='h.png')
# allboard['A'][0].configure(image=img)
# allboard['A'][1].configure(image=img)

for i,nm in enumerate(top_name):
	chessname = nm
	#allboard['H'][i].configure(text=f'{chessname: ^{15}}')
	allboard['H'][i].configure(command=lambda x=chessname: Select(x))
'''
BOARD.mainloop()