from tests import unittest
from markov import graph

class TestGraph(unittest.TestCase):
	def setUp(self):
		self.graph = graph.Graph()

	def test_getStateNameOrDefault_from_dict_with_name(self):
		name = graph.Graph._getStateNameOrDefault({'name': 'name'})
		self.assertEqual(name, 'name')

	def test_getStateNameOrDefault_from_str(self):
		name = graph.Graph._getStateNameOrDefault('name')
		self.assertEqual(name, 'name')


	def test_addStateToAdjacencyMatrix_add_first_state(self):
		matrix = []
		states = dict()
		name_to_index_maps = dict()
		index_to_name_maps = dict()

		graph.Graph._addStateToAdjacencyMatrix(
			matrix,
			states,
			name_to_index_maps,
			index_to_name_maps,
			{'name': 'A'}
			)

		self.assertEqual(0, name_to_index_maps.get('A'))
		self.assertEqual({'name': 'A'}, states.get('A'))
		self.assertEqual(matrix, [[None]])


	def test_addStateToAdjacencyMatrix_add_second_state(self):
		matrix = [[None]]
		states = dict({'A': {'name': 'A'}})
		name_to_index_maps = dict({'A': 0})
		index_to_name_maps = dict({0: 'A'})

		graph.Graph._addStateToAdjacencyMatrix(
			matrix,
			states,
			name_to_index_maps,
			index_to_name_maps,
			{'name': 'B'}
			)

		self.assertEqual(1, name_to_index_maps.get('B'))
		self.assertEqual({'name': 'B'}, states.get('B'))
		self.assertEqual(matrix, [[None, None], [None, None]])


	def test_create_graph(self):
		self.graph.addTransition('A', 'B', 'A->B')
		self.graph.addTransition('A', 'C', 'A->C')
		self.graph.addTransition('C', 'A', 'C->A')

		##self.assertEqual(
		##	self.graph.__dump__(),
		##	[
		##		[None, 'A->B', 'A->C'],
		##		[None, None, None],
		##		['C->A', None, None]
		##	])

		transitions = self.graph.getTransitions('A')
		self.assertEqual(
			transitions,
			{'B': 'A->B', 'C': 'A->C'}
		)

		transitions = self.graph.getTransitions('C')
		self.assertEqual(
			transitions,
			{'A': 'C->A'}
		)

if __name__ == '__main__':
	unittest.main()
