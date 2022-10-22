from tests import unittest
from markov import graph

class TestGraph(unittest.TestCase):
	def setUp(self):
		self.graph = graph.Graph

if __name__ == '__main__':
	unittest.main()
