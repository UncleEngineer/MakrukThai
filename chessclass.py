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
		self.columns_key2 = {0:'A',1:'B',2:'C',3:'D',4:'E',5:'F',6:'G',7:'H'}
		self.tables = []

	def char(self):
		self.column = self.location.split('_')[0]
		self.row = int(self.location.split('_')[1])





class Makruk(Mak):
	
	def __init__(self,location,BOARD,TEAM):
		ruerlist = []
		ruerlist.extend([(0,i) for i in range(1,8)])
		ruerlist.extend([(0,-i) for i in range(1,8)])
		ruerlist.extend([(i,0) for i in range(1,8)])
		ruerlist.extend([(-i,0) for i in range(1,8)])
		self.team = TEAM
		self.makruk_validmove = {'ruer':ruerlist,
								 'ma':[(1,2),(2,1),(2,-1),(1,-2),(-1,-2),(-2,-1),(-2,1),(-1,2)],
								 'khon':[(0,1),(1,1),(-1,1),(1,-1),(-1,-1)],
								 'med':[(1,1),(-1,1),(1,-1),(-1,-1)],
								 'khun':[(0,1),(0,-1),(1,0),(-1,0),(1,1),(-1,1),(1,-1),(-1,-1)],
								 'bia1':[(0,1)],
								 'bia2':[(1,1),(-1,1),(1,-1),(-1,-1)]}
		super().__init__(location,BOARD)
		self.bia = False
		print('NAME:',self.name)
		self.move_valid = self.makruk_validmove[self.name.split('-')[0]]
		self.bia_capture_valid = [(-1,1),(1,1)]
		self.currentindex = ()

	def check_move(self,loc_to,show=True):
		# A_3 -> A_4
		# แปลงจาก A_3 เป็น index [5][0]
		currentindex = (self.columns_key[self.column],self.row)	
		self.currentindex = currentindex
		px,py = self.currentindex
		valid_move = []
		valid_checklist = []
		for mvx,mvy in self.move_valid:
			valid_move.append((mvx+px,8-(py+mvy)))
		#print('MOVE LIST',valid_move) # 0,4
		print('----{}-----can move to--------'.format(self.location))
		for vm in valid_move:
			try:
				code = '{}_{}'.format(self.columns_key2[vm[0]], 8 - vm[1])
				#print('Valid Location:', code)
				if code in self.board.location:
					valid_checklist.append(code)
			except:
				pass

		# for m in self.board.Mak.items():
		# 	print(m[0],m[1])
		# 	if m[1] != '-':
		# 		print(m[1].team)

		valid_canmove = []
		for v in valid_checklist:
			if self.board.Mak[v] != '-':
				#print('OK:',v, [self.board.Mak[v].team])
				if self.board.Mak[v].team == 'A':
					pass
				else:
					valid_canmove.append(v)
			else:
				valid_canmove.append(v)

		print('VALID:',valid_canmove)
		if loc_to in valid_canmove:
			if show:
				print('{} can move to {}'.format(self.name,loc_to))
			return True
		else:
			if show:
				print("{} can't move to {}".format(self.name,loc_to))
			return False

	def __str__(self):
		return self.name


class Board:
	def __init__(self):
		self.Mak = {}
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

		self.update_table()
		self.NewMakruk()

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
		#print(self.location)

	def update_newtable(self,show=True):
		
		allrow = []
		row = []
		count = 0
		for i,l in enumerate(self.Mak.values(),start=0):
			if l != '-':
				row.append(l.name)
			else:
				row.append('-')

			if count == 7:
				#print('ROW ADD:',row)
				allrow.append(row)
				row = []
				count = 0
			else:
				count += 1
		self.table = allrow
		if show == True:
			self.showtable()
			#print(self.location)


	def NewMakruk(self):

		for code,mak in self.location.items():
			if mak != '-':
				mak_name = mak.split('-')[0]
				team = mak.split('-')[1]
				if team == '1':
					team = 'A'
				else:
					team = 'B'
				newmak = Makruk(code,self,team)
				self.Mak[code] = newmak
			else:
				self.Mak[code] = '-'

	def move(self,loc_from,loc_to):
		if self.Mak[loc_from].check_move(loc_to):
			self.Mak[loc_to] = self.Mak[loc_from]
			self.Mak[loc_to].location = loc_to
			self.Mak[loc_to].char() # update location 
			#BOARD.update_newtable(False)
			#self.Mak[loc_to] = Makruk(loc_to,self,self.Mak[loc_to].team)
			self.Mak[loc_from] = '-'
			BOARD.update_newtable()
			

		
	def showtable(self):
		bd = '|' + f'{"-"*10:^{10}}'
		border = bd * 8 + '|'
		result = [border]
		for k,rw in enumerate(self.table):
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
			result.append(rowtext + '|  {}'.format(8-k))
			result.append(blankline)
			result.append(border)
		
		border = ''
		for c in self.columns:
			bd = ' ' + f'{c:^{10}}'
			border += bd
			
		result.append(border)
		for r in result:
			print(r)
		print()





if __name__ == '__main__':
	BOARD = Board()
	BOARD.showtable()
	
	#BOARD.move('A_3','A_6')
	

	for i in range(10):
		loc_from = input("Enter ['A_3'] Makruk Location from: ")
		loc_to = input("Enter ['A_4'] Makruk Location from: ")
		BOARD.move(loc_from,loc_to)
		print('----------------')











'''
x x x x x x x x
x x x x x x x x
x x x x x x x x
x x x x x x x x
x x x x x x x x
x x x x x x x x
x x x x x x x x
x x x x x x x x

ma
x x x x x x x x
x x x x x x x x
x x o x o x x x
x o x x x o x x
x x x M x x x x
x o x x x o x x
x x o x o x x x
x x x x x x x x

[(1,2),(2,1),(2,-1),(1,-2),(-1,-2),(-2,-1),(-2,1),(-1,2)]

'''








#print(BOARD.table)

# bia = Makruk('B_3',BOARD)
# check = bia.check_move('C_4')
