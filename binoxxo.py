from copy import deepcopy


def double_depth_copy(dl):
	c = []
	for row in dl:
		c.append(list(row))
	return c

def looks_like(a, b, neutral):
	for i in range(0, len(a)):
		if (a[i] != neutral or b[i] != neutral) and a[i] != b[i]:
			return False
	return True

class Binoxxo:
	def __init__(self, size):
		if (size % 2 != 0):
			raise AttributeError("Binoxxo should be an even size matrix")
		self._size = size
		self._matrix = [[' ' for x in range(0, size)] for x in range(0, size)]
		self._history = []

	def size(self):
		return self._size

	def at(self, i, j):
		if 0 <= i < self.size() and 0 <= j < self.size():
			return self._matrix[i][j]
		return '!'

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

		b = Binoxxo(self._size)
		b._matrix = double_depth_copy(self._matrix)
		b._matrix[i][j] = val
		b._history = list(self._history)
		b._history.append(self)
		return b

	def revert(self):
		if not self._history:
			raise AssertionError("history is empty, no previous state exist")
		return self._history.pop()

	def rule1(self, i, j, val):
		"""
		Rule °1: Cannot have more than two consecutive x's or o's in each row and column
		:param binoxxo: the initial valid binoxxo
		:param i: x axis position in the matrix of the move
		:param j: y axis position in the matrix of the move
		:param val: the value to insert into the binoxxo
		:return: True or False, wether the move is correct or not for the rule °1
		"""

		return not (val == self.at(i + 1, j) and val == self.at(i + 2, j)) and \
		       not (val == self.at(i - 1, j) and val == self.at(i - 2, j)) and \
		       not (val == self.at(i, j + 1) and val == self.at(i, j + 2)) and \
		       not (val == self.at(i, j - 1) and val == self.at(i, j - 2))

	def rule2(self, i, j, val):
		"""
		Rule °2: On each complete row or column, there must be half x's and half o's
		:param self: the initial valid binoxxo
		:param i: x axis position in the matrix of the move
		:param j: y axis position in the matrix of the move
		:param val: the value to insert into the binoxxo
		:return: True or False, wether the move is correct or not for the rule °2
		"""
		return self.get_row(i).count(val) + 1 <= self.size() / 2 and \
		       self.get_column(j).count(val) + 1 <= self.size() / 2

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
			return False

		return self.rule1(i, j, val) and self.rule2(i, j, val) and self.rule3(i, j, val)

	def __str__(self):
		# rep = ((2 * self.size() + 1) * "-") + "\n"
		rep = ""
		for row in self._matrix:
			# rep += '|'
			for elem in row:
				rep += elem
			rep += "\n"
			# rep += "\n" + ((2 * self.size() + 1) * "-") + "\n"
		return rep

	def is_complete(self):
		for row in self._matrix:
			if ' ' in row:
				return False
		return True

	def get_possible_next_moves(self):
		possibilities = []
		for i in range(0, self._size):
			for j in range(0, self._size):
				for val in ['x', 'o']:
					if self.check(i, j, val):
						possibilities.append(self.set(i, j, val))
				if len(possibilities):
					return possibilities
		return possibilities

	def is_viable(self):
		for x in range(0, self.size()):
			rowx = self.get_row(x)
			colx = self.get_column(x)

			if rowx.count(' ') == 1:
				if not self.check(x, rowx.index(' '), 'x' if rowx.count('x') < rowx.count('o') else 'o'):
					return False
			if rowx.count('x') == self.size()/2:
				for y in range(0, self.size()):
					if x != y and looks_like(rowx, self.get_row(y), '_'):
						return False

			if colx.count(' ') == 1:
				if not self.check(colx.index(' '), x, 'x' if colx.count('x') < colx.count('o') else 'o'):
					return False
			if colx.count('x') == self.size() / 2:
				for y in range(0, self.size()):
					if x != y and looks_like(colx, self.get_column(y), '_'):
						return False
		return True

