# chessclass.py

class Mak:
	def __init__(self,location,BOARD):
		self.board = BOARD
		self.location = location # A_1
		self.name = self.board.location[location]
		self.column = None
		self.row = None
		self.char()
		self.columns_key = {'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7}
		self.tables = []

	def char(self):
		self.column = self.location.split('_')[0]
		self.row = self.location.split('_')[1]


class Bia1(Mak):
	'''
	o x o
	  x 

	A_3

	'''
	def __init__(self,location,BOARD):
		super().__init__(location,BOARD)
		self.move_valid = [(0,1)]
		self.capture_valid = [(-1,1),(1,1)]
		self.currentindex = []

	def check_move(self,loc_to):
		# A_3 -> A_4
		# แปลงจาก A_3 เป็น index [5][0]
		currentindex = (self.row,self.columns_key[self.column])
		print(currentindex)		
		self.currentindex = currentindex
		

		
		
		



def NewChess(chess):
	if chess.split('-')[0] == 'bia1':
		new = Bia1()




columns = ['A','B','C','D','E','F','G','H']


table = [['ruer-1', 'ma-1', 'khon-1', 'med-1', 'khun-1', 'khon-1', 'ma-1', 'ruer-1'],
['-', '-', '-', '-', '-', '-', '-', '-'],
['bia1-1', 'bia1-1', 'bia1-1', 'bia1-1', 'bia1-1', 'bia1-1', 'bia1-1', 'bia1-1'],
['-', '-', '-', '-', '-', '-', '-', '-'],
['-', '-', '-', '-', '-', '-', '-', '-'],
['bia1-2', 'bia1-2', 'bia1-2', 'bia1-2', 'bia1-2', 'bia1-2', 'bia1-2', 'bia1-2'],
['-', '-', '-', '-', '-', '-', '-', '-'],
['ruer-2', 'ma-2', 'khon-2', 'khun-2', 'med-2', 'khon-2', 'ma-2', 'ruer-2']]




class Board:
	def __init__(self):
		self.columns = ['A','B','C','D','E','F','G','H']
		self.location = {}
		self.table = [['ruer-2', 'ma-2', 'khon-2', 'khun-2', 'med-2', 'khon-2', 'ma-2', 'ruer-2'],
					 ['-', '-', '-', '-', '-', '-', '-', '-'],
					 ['bia1-2', 'bia1-2', 'bia1-2', 'bia1-2', 'bia1-2', 'bia1-2', 'bia1-2', 'bia1-2'],
					 ['-', '-', '-', '-', '-', '-', '-', '-'],
					 ['-', '-', '-', '-', '-', '-', '-', '-'],
					 ['bia1-1', 'bia1-1', 'bia1-1', 'bia1-1', 'bia1-1', 'bia1-1', 'bia1-1', 'bia1-1'],
					 ['-', '-', '-', '-', '-', '-', '-', '-'],
					 ['ruer-1', 'ma-1', 'khon-1', 'med-1', 'khun-1', 'khon-1', 'ma-1', 'ruer-1']]


	def update_table(self):
		location = {}

		for i,row in enumerate(self.table,start=1):
			rw = []
			for j,col in enumerate(self.columns):
				loc_code = '{}_{}'.format(col,9-i)
				rw.append(loc_code)
				location[loc_code] = row[j]
			#print(rw)
		self.location = location
		allrow = []
		row = []
		count = 0
		for i,l in enumerate(location.values(),start=0):
			row.append(l)
			if count == 7:
				#print('ROW ADD:',row)
				allrow.append(row)
				row = []
				count = 0
			else:
				count += 1
		self.table = allrow

	def move(self,mak,loc_to):
		mak_loc = mak.location # A_3




BOARD = Board()
BOARD.update_table()
print(BOARD.table)

bia = Bia1('A_3',BOARD)
bia.check_move('A_4')


'''

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

'''

