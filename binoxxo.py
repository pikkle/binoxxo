class Binoxxo:
	def __init__(self, size):
		if (size % 2 != 0):
			raise AttributeError("Binoxxo should be an even size matrix")
		self._size = size
		self._matrix = [[' ' for x in range(0, size)] for x in range(0, size)]

	def size(self):
		return self._size

	def at(self, i, j):
		if (i < 0 or j < 0 or i >= self._size or j >= self._size):
			return '!'
		return self._matrix[i][j]

	def get_row(self, i):
		return self._matrix[i]

	def get_column(self, j):
		return [row[j] for row in self._matrix]

	def set(self, i, j, val):
		if (val not in ['x', 'o']):
			raise AssertionError("val is not valid (can be 'x' or 'o')")
		if (i < 0 or j < 0 or i >= self._size or j >= self._size):
			raise AssertionError("(i, j) is not in the matrix")
		if (not self.check(i, j, val)):
			raise AssertionError("move is not valid !")
		self._matrix[i][j] = val

	def rule1(self, i, j, val):
		"""
		Rule °1: Cannot have more than two consecutive x's or o's in each row and column
		:param binoxxo: the initial valid binoxxo
		:param i: x axis position in the matrix of the move
		:param j: y axis position in the matrix of the move
		:param val: the value to insert into the binoxxo
		:return: True or False, wether the move is correct or not for the rule °1
		"""
		down = not (val == self.at(i + 1, j) and val == self.at(i + 2, j))
		up = not (val == self.at(i - 1, j) and val == self.at(i - 2, j))
		right = not (val == self.at(i, j + 1) and val == self.at(i, j + 2))
		left = not (val == self.at(i, j - 1) and val == self.at(i, j - 2))
		return down and up and right and left

	def rule2(self, i, j, val):
		"""
		Rule °2: On each complete row or column, there must be half x's and half o's
		:param self: the initial valid binoxxo
		:param i: x axis position in the matrix of the move
		:param j: y axis position in the matrix of the move
		:param val: the value to insert into the binoxxo
		:return: True or False, wether the move is correct or not for the rule °2
		"""
		return self.get_row(i).count(val) + 1 <= self.size() / 2 and self.get_column(j).count(
			val) + 1 <= self.size() / 2

	def rule3(self, i, j, val):
		"""
		Rule °3: Each row and column is different from one another
		:param self: the initial valid binoxxo
		:param i: x axis position in the matrix of the move
		:param j: y axis position in the matrix of the move
		:param val: the value to insert into the binoxxo
		:return: True or False, wether the move is correct or not for the rule °3
		"""
		row = self.get_row(i).copy()
		row[j] = val
		col = self.get_column(j).copy()
		col[i] = val

		for x in range(0, self.size()):
			rowx = self.get_row(x)
			colx = self.get_column(x)
			if ((x != i and rowx == row and ' ' not in rowx) or (x != j and colx == col and ' ' not in colx)):
				return False
		return True

	def check(self, i, j, val):
		"""
		Checks the validity of a binoxxo's move
		:param binoxxo: the initial valid binoxxo
		:param i: x axis position in the matrix of the move
		:param j: y axis position in the matrix of the move
		:param val: the value to insert into the binoxxo
		:return: True or False, wether the move is correct or not
		"""

		if self.at(i, j) != ' ':
			raise AssertionError("Binoxxo already has a value in ({}, {})".format(i, j))

		r1 = self.rule1(i, j, val)
		r2 = self.rule2(i, j, val)
		r3 = self.rule3(i, j, val)
		return r1 and r2 and r3

	def __str__(self):
		rep = ((2 * self.size() + 1) * "-") + "\n"
		for row in self._matrix:
			rep += '|'
			for elem in row:
				rep += elem + '|'
			rep += "\n" + ((2 * self.size() + 1) * "-") + "\n"
		return rep

	def is_complete(self):
		for row in self._matrix:
			if ' ' in row:
				return False
		return True

	def get_empty_spots(self):
		empty_spots = []
		for i in range(0, self._size):
			for j in range(0, self._size):
				if (self._matrix[i][j] == ' '):
					empty_spots += [(i, j)]
		return empty_spots
