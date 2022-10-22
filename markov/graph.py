class Graph:
	def __init__(self):
		self._matrix = []
		self._name_to_index_maps = dict()
		self._index_to_name_maps = dict()
		self._states = dict()
		None

	def __dump__(self):
		return self._matrix

	def addState(self, *args):
		for state in args:
			Graph._addStateToAdjacencyMatrix(
				self._matrix,
				self._states,
				self._name_to_index_maps,
				self._index_to_name_maps,
				state
				)

	def addTransition(self, fromState, toState, transition):
		if not self._hasState(fromState):
			self.addState(fromState)
		if not self._hasState(toState):
			self.addState(toState)
		
		self.updateTransition(
			fromState,
			toState,
			transition
			)

	def updateTransition(self, fromState, toState, transition):
		row = self._getStateIndex(fromState)
		col = self._getStateIndex(toState)

		self._matrix[row][col] = transition

	def removeTransition(self, fromState, toState):
		self.updateTransition(fromState, toState, None)

	def getTransitions(self, fromState):
		row = self._matrix[self._getStateIndex(fromState)]
		transitions = dict()

		for index in range(len(row)):
			transition = row[index]
			if (transition != None):
				name = self._index_to_name_maps.get(index)
				transitions.update({name: transition})

		return transitions

	def _getStateIndex(self, state):
		name = Graph._getStateNameOrDefault(state)
		return self._name_to_index_maps.get(name)

	def _hasState(self, state):
		name = Graph._getStateNameOrDefault(state)
		return self._name_to_index_maps.get(name) != None


	@staticmethod
	def _addStateToAdjacencyMatrix(
		matrix,
		states,
		name_to_index_maps,
		index_to_name_maps, state):

		## register new state

		name = Graph._getStateNameOrDefault(state)
		states.update({name: state})

		## add new state name to index mapping

		index = len(matrix)
		name_to_index_maps.update({name: index})
		index_to_name_maps.update({index: name})

		## add a new column to the adjacency matrix

		for row in matrix:
			row.append(None)

		## add a new row to the adjacency matrix

		count = index + 1
		newRow = [None] * count
		matrix.append(newRow)


	@staticmethod
	def _getStateNameOrDefault(state):
		if isinstance(state, dict) and state.get('name') != None:
			return state['name']
		if isinstance(state, str):
			return str(state)

