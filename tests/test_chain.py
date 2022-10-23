import operator
from re import X

from tests import unittest
from markov import chain

class TestChain(unittest.TestCase):
	def setUp(self):
		self.chain = chain.Chain()
		self.chain.addTransition('E', 'E', 0.3)
		self.chain.addTransition('E', 'A', 0.7)
		self.chain.addTransition('A', 'E', 0.4)
		self.chain.addTransition('A', 'A', 0.6)

		# default selector is to apply weighted probabilities
		# to calculate the next state. We change it here for
		# test purposes and always select the highest probability

		self.chain._selector = TestChain._highestProbabilitySelector

	def test_getNextState(self):
		next = self.chain.getNextState('E', TestChain._lowestProbabilitySelector)
		self.assertEqual('E', next)
		next = self.chain.getNextState(next)
		self.assertEqual('A', next)
		next = self.chain.getNextState(next)
		self.assertEqual('A', next)

	def test_lowestProbabilitySelector(self):
		self._test_selector(
			{'E': 0.3, 'A': 0.7},
			TestChain._lowestProbabilitySelector,
			'E')

	def test_highestProbabilitySelector(self):
		self._test_selector(
			{'E': 0.3, 'A': 0.7},
			TestChain._highestProbabilitySelector,
			'A')

	def _test_selector(self, transitions, selector, expected):
		state = selector(transitions)
		self.assertEqual(expected, state)

	@staticmethod
	def _getProbability(transition):
		(_, probability) = transition
		return probability

	@staticmethod
	def _lowestProbabilitySelector(transitions):
		collection = list(transitions.items())
		(next, _) = min(collection, key=lambda item: item[1])
		return next

	@staticmethod
	def _highestProbabilitySelector(transitions):
		collection = list(transitions.items())
		(next, _) = max(collection, key=lambda item: item[1])
		return next

if __name__ == '__main__':
	unittest.main()
