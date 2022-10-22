import operator
from re import X

from tests import unittest
from markov import chain

class TestChain(unittest.TestCase):
	def setUp(self):
		self.chain = chain.Chain()
		self.chain._selector = TestChain._highestProbabilitySelector

	def test_getNextState(self):
		self.chain.addTransition('E', 'E', 0.3)
		self.chain.addTransition('E', 'A', 0.7)
		self.chain.addTransition('A', 'E', 0.4)
		self.chain.addTransition('A', 'A', 0.6)

		next = self.chain.getNextState('E')
		self.assertEqual('A', next)

		next = self.chain.getNextState(next)
		self.assertEqual('A', next)

	def test_highestProbabilitySelector(self):
		transitions = {'E': 0.3, 'A': 0.7}
		selector = TestChain._highestProbabilitySelector
		state = selector(transitions)
		self.assertEqual('A', state)

	@staticmethod
	def _getProbability(transition):
		(_, probability) = transition
		return probability

	@staticmethod
	def _highestProbabilitySelector(transitions):
		collection = list(transitions.items())
		(next, _) = max(collection, key=lambda item: item[1]);
		return next

if __name__ == '__main__':
	unittest.main()
