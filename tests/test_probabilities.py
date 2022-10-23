from tests import unittest

from markov import markov

class TestProbabilities(unittest.TestCase):
	def setUp(self):
		None

	def test_rebalance_propabilities(self):
		# this is a set of transitions from a Markov chain
		# the transition {'C': 0.4} has been removed
		# probabilities must be rebalance equitably
		transitions = {
			'A': 0.3,
			'B': 0.3,
		}

		transitions = markov._rebalance_probabilities(transitions)

		self.assertEqual(
			transitions,
			{'A': 0.5, 'B': 0.5}
		)


if __name__ == '__main__':
	unittest.main()
