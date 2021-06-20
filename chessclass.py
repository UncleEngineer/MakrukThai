# chessclass.py

class Mak:
	def __init__(self,location,name):

		self.location = location # A_1
		self.name = name
		self.column = ''
		self.row = None
		self.char()

	def valid_location(self,push_loc,tables):
		print('valid_location')

	def char(self):
		self.column = self.location.split('_')[0]
		self.row = self.location.split('_')[1]


class Bia1(Mak):
	'''
	o x o
	  x     
	'''
	def __init__(self,location,name):
		super().__init__(location,name)
		self.move_valid = [(0,1)]
		self.capture_valid = [(-1,1),(1,1)]


x = Bia1('A_3','bia1')
x.valid_location('A_4',[])
print(x.location)


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


allchess = {}

for i,row in enumerate(table,start=1):
	rw = []
	for j,col in enumerate(columns):
		loc_code = '{}_{}'.format(col,9-i)
		rw.append(loc_code)
		allchess[loc_code] = row[j]
	#print(rw)

print(allchess)

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

