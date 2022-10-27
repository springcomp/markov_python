import numpy as np
import random as rm

from markov import chain

carte=[
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

c = chain.Chain()

c.addTransition('000', '000', 0.55)
c.addTransition('000', '045', 0.214)
c.addTransition('000', '090', 0.022)
c.addTransition('000', '135', 0)
c.addTransition('000', '180', 0)
c.addTransition('000', '225', 0)
c.addTransition('000', '270', 0.024)
c.addTransition('000', '315', 0.19)
c.addTransition('045', '000', 0.19)
c.addTransition('045', '045', 0.55)
c.addTransition('045', '090', 0.214)
c.addTransition('045', '135', 0.022)
c.addTransition('045', '180', 0)
c.addTransition('045', '225', 0)
c.addTransition('045', '270', 0)
c.addTransition('045', '315', 0.024)
c.addTransition('090', '000', 0.022)
c.addTransition('090', '045', 0.19)
c.addTransition('090', '090', 0.55)
c.addTransition('090', '135', 0.214)
c.addTransition('090', '180', 0.024)
c.addTransition('090', '225', 0)
c.addTransition('090', '270', 0)
c.addTransition('090', '315', 0)
c.addTransition('135', '000', 0)
c.addTransition('135', '045', 0.022)
c.addTransition('135', '090', 0.19)
c.addTransition('135', '135', 0.55)
c.addTransition('135', '180', 0.214)
c.addTransition('135', '225', 0.024)
c.addTransition('135', '270', 0)
c.addTransition('135', '315', 0)
c.addTransition('180', '000', 0)
c.addTransition('180', '045', 0)
c.addTransition('180', '090', 0.022)
c.addTransition('180', '135', 0.19)
c.addTransition('180', '180', 0.55)
c.addTransition('180', '225', 0.214)
c.addTransition('180', '270', 0.024)
c.addTransition('180', '315', 0)
c.addTransition('225', '000', 0)
c.addTransition('225', '045', 0)
c.addTransition('225', '090', 0)
c.addTransition('225', '135', 0.022)
c.addTransition('225', '180', 0.19)
c.addTransition('225', '225', 0.55)
c.addTransition('225', '270', 0.214)
c.addTransition('225', '315', 0.024)
c.addTransition('270', '000', 0.022)
c.addTransition('270', '045', 0)
c.addTransition('270', '090', 0)
c.addTransition('270', '135', 0)
c.addTransition('270', '180', 0.024)
c.addTransition('270', '225', 0.19)
c.addTransition('270', '270', 0.55)
c.addTransition('270', '315', 0.214)
c.addTransition('315', '000', 0.214)
c.addTransition('315', '045', 0.022)
c.addTransition('315', '090', 0)
c.addTransition('315', '135', 0)
c.addTransition('315', '180', 0)
c.addTransition('315', '225', 0.024)
c.addTransition('315', '270', 0.19)
c.addTransition('315', '315', 0.55)

def _dir(state):
    directions = {
        '000': u'\u21d2',
        '045': u'\u21d8',
        '090': u'\u21d3',
        '135': u'\u21d9',
        '180': u'\u21d0',
        '225': u'\u21d6',
        '270': u'\u21d1',
        '315': u'\u21d7',
    }
    return directions[state]

class ShipCourse:
    def __init__(self, initA = 7, initB = 30):
        self._pos = (initA, initB) # x coordinate, y coordinate
        self._recalc_neighbourhood()

    def forecast(self, ndays, courseToday = '090'):

        print("Initial status: {} {}".format(self._pos, _dir(courseToday)))

        courseList = self.calc_forecast(courseToday, ndays)

        print("Possible states: " + str(courseList))
        print("End state after {} days: {}".format(ndays, courseList[ndays - 1]))
        print("End position: {}".format(self._pos))


    def calc_forecast(self, initial_course, ndays):
        courses = []

        next = initial_course
        for nday in range(ndays):

            print('>> current_status[{}]: {} {}'.format(nday, self._pos, _dir(next)))

            next = self.forecast_next_change(next)
            courses.append(next)

            self._recalc_position(next)
            self._recalc_neighbourhood()

            print('<< course_change[{}]: {} {}'.format(nday, _dir(next), self._pos))
            print('')

        return courses


    def forecast_next_change(self, state):
        next = c.getNextState(state, self.select_transition)
        return next

    def select_transition(self, transitions):
        # by default a Markov chain will apply
        # weighted random selection of the next transition
        # using the default algorithm or by using a custom
        # selector like the following commented line:
        #
        # return chain.Chain._randomProbabilitySelector(transitions)

        # instead, we need to take into account the state of the world
        # some transitions might not be possible in the current state
        # some those must be eliminated from the set of transitions
        # and the remaining probabilities updated accordingly

        print('>> {}'.format(ShipCourse._format_transitions(transitions)))

        self._pop_impossible_transitions(transitions)

        updated_transitions_with_probabilities = \
            ShipCourse._rebalance_probabilities(transitions)

        print('<< {}'.format(ShipCourse._format_transitions(updated_transitions_with_probabilities)))

        return chain.Chain._randomProbabilitySelector(updated_transitions_with_probabilities)
    
    def _recalc_neighbourhood(self):
        self.B = self._pos[0] - 1 # Sud
        self.C = self._pos[0] + 1  # Nord
        self.M = self._pos[1] - 1  # West
        self.N = self._pos[1] + 1  # East

    def _pop_impossible_transitions(self, transitions):

        x = self._pos[0]
        y = self._pos[1]

        neighbourhoods = {
            '000': carte[y + 0][x + 1], # East
            '045': carte[y + 1][x + 1], # South-East
            '090': carte[y + 1][x + 0], # South
            '135': carte[y + 1][x - 1], # South-West
            '180': carte[y + 0][x - 1], # West
            '225': carte[y - 1][x - 1], # North-West
            '270': carte[y - 1][x + 0], # North 
            '315': carte[y - 1][x + 1], # North-East
        }

        impossible_neighbours = [neighbourhood[0] for neighbourhood in list(neighbourhoods.items()) if neighbourhood[1] == 0]
        for impossible_neighbour in impossible_neighbours:
            transitions.pop(impossible_neighbour)

    def _recalc_position(self, next):
        recalcer = {
            '000': lambda p: (p[0] + 1, p[1] + 0),
            '045': lambda p: (p[0] + 1, p[1] + 1),
            '090': lambda p: (p[0] + 0, p[1] + 1),
            '135': lambda p: (p[0] - 1, p[1] + 1),
            '180': lambda p: (p[0] - 1, p[1] + 0),
            '225': lambda p: (p[0] - 1, p[1] - 1),
            '270': lambda p: (p[0] + 0, p[1] - 1),
            '315': lambda p: (p[0] + 1, p[1] - 1),
        }
        self._pos = recalcer[next](self._pos)

    @staticmethod
    def _format_transitions(transitions, formatter = _dir, probaber = lambda x: round(x, 3)):
        collection = list(transitions.items())
        formatted = [(formatter(item[0]), probaber(item[1])) for item in collection]
        return dict(formatted)

    @staticmethod
    def _rebalance_probabilities(transitions):
        remaining = sum(item for item in transitions.values())
        if (remaining == 1.0):
            return transitions

        if (remaining == 0):
            print('_rebalance_probabilities: seems there is no possible next state')
            return ShipCourse._format_transitions(
                transitions,
                lambda course: course,
                lambda _: 0
            )

        return ShipCourse._format_transitions(
            transitions,
            lambda course: course,
            lambda probability: round(probability/remaining, 3)
        )
