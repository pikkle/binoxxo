import unittest
from binoxxo import Binoxxo


class TestBinoxxo(unittest.TestCase):
	def test_initiate_size(self):
		size = 2
		b = Binoxxo(size)
		self.assertEqual(size, b.size())

	def test_initiate_matrix(self):
		b = Binoxxo(2)
		self.assertEqual([[' ', ' '], [' ', ' ']], b._matrix)

	def test_uneven_size_binoxxo(self):
		with self.assertRaises(AttributeError):
			b = Binoxxo(3)

	def test_checks_invalid_position(self):
		b = Binoxxo(2)
		with self.assertRaises(AssertionError):
			b.check(-1, 0, 'x')

	def test_checks_valid_simple_move(self):
		b = Binoxxo(2)
		self.assertTrue(b.check(0, 0, 'x'))

	def test_checks_invalid_value(self):
		b = Binoxxo(2)
		with self.assertRaises(AssertionError):
			b.set(0, 0, 'z')




if __name__ == '__main__':
	suite = unittest.TestLoader().loadTestsFromTestCase(TestBinoxxo)
	unittest.TextTestRunner(verbosity=2).run(suite)
