import random

from functools import partial
from markov import graph;

class Chain(graph.Graph):
	def __init__(self):
		super().__init__()
		random.seed()
		self._selector = Chain._randomProbabilitySelector
		None

	def getNextState(self, state):
		transitions = self.getTransitions(state)
		transition = self._selector(transitions)
		return transition

	@staticmethod
	def _randomProbabilitySelector(transitions):
		collection = list(transitions.items())
		weights = tuple(item[1] for item in collection)
		choices = random.choices(collection, weights=weights, k=1)
		(next, _) = choices[0]
		return next
