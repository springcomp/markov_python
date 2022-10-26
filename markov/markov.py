import numpy as np
import random as rm

from markov import chain

## TO RUN THIS PROGRAM
## > python
## >>> from markov import markov
## >>> m = markov.ShipCourse()
## >>> m.forecast(21)
##
## TO TEST
## > python
## >>> from markov import markov; m = markov.ShipCourse(); m.forecast(21)
## 

carte=[
[0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0],
[0,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	0],
[0,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	0],
[0,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	0],
[0,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	0],
[0,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	0],
[0,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	0],
[0,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	0],
[0,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	0],
[0,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	0,	0,	0,	0,	0,	0,	1,	1,	1,	1,	0,	0,	0,	0,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	0],
[0,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	0,	0,	0,	0,	0,	0,	1,	1,	1,	1,	0,	0,	0,	0,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	0],
[0,	1,	1,	1,	1,	1,	1,	1,	1,	0,	0,	0,	0,	0,	0,	1,	1,	1,	1,	1,	1,	0,	0,	0,	0,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	0,	0,	0,	0,	0],
[0,	1,	1,	1,	1,	1,	1,	1,	1,	0,	0,	0,	0,	0,	0,	1,	1,	1,	1,	1,	1,	0,	0,	0,	0,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	0,	0,	0,	0,	0],
[0,	1,	1,	1,	1,	1,	1,	1,	1,	0,	0,	0,	0,	0,	0,	0,	0,	1,	1,	1,	1,	1,	1,	0,	0,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	0,	0,	0,	0,	0,	0,	0],
[0,	1,	1,	1,	1,	1,	1,	1,	1,	0,	0,	0,	0,	0,	0,	0,	0,	1,	1,	1,	1,	1,	1,	0,	0,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	0,	0,	0,	0,	0,	0,	0],
[0,	1,	1,	1,	1,	1,	1,	0,	0,	0,	0,	0,	0,	0,	0,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	0,	0,	0,	0,	0,	0,	0],
[0,	1,	1,	1,	1,	1,	1,	0,	0,	0,	0,	0,	0,	0,	0,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	0,	0,	0,	0,	0,	0,	0],
[0,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	0,	0,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	0,	0,	0,	0,	0],
[0,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	0,	0,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	0,	0,	0,	0,	0],
[0,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	0,	0,	0,	0,	0],
[0,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	0,	0,	0,	0,	0],
[0,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	0,	0,	0,	0,	0],
[0,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	0,	0,	0,	0,	0],
[0,	0,	0,	1,	1,	1,	1,	1,	1,	0,	0,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	0,	0,	0,	0,	0,	0,	0,	0,	0],
[0,	0,	0,	1,	1,	1,	1,	1,	1,	0,	0,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	0,	0,	0,	0,	0,	0,	0,	0,	0],
[0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0],
[0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0],
[0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	0,	0,	0,	0,	0,	0,	0,	0,	0],
[0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	0,	0,	0,	0,	0,	0,	0,	0,	0],
[0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	0,	0,	0,	0,	0],
[0,	0,	0,	0,	0,	0,	0,	1,	0,	0,	0,	0,	0,	0,	0,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	0,	0,	0,	0,	0],
[0,	0,	0,	1,	1,	0,	1,	1,	0,	0,	0,	0,	0,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	0],
[0,	0,	0,	1,	1,	0,	1,	1,	0,	0,	0,	0,	0,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	0],
[0,	1,	1,	1,	1,	1,	0,	0,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	0,	0,	0,	0,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	0],
[0,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	0,	0,	0,	0,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	0],
[0,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	0,	0,	0,	0,	0,	0,	0,	0,	1,	1,	1,	1,	1,	1,	1,	1,	0],
[0,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	0,	0,	0,	0,	0,	0,	0,	0,	1,	1,	1,	1,	1,	1,	1,	1,	0],
[0,	0,	0,	0,	0,	1,	1,	1,	1,	1,	1,	0,	0,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	0,	0,	1,	1,	1,	1,	1,	1,	0,	0,	0,	0,	1,	1,	1,	1,	1,	1,	1,	1,	0],
[0,	0,	0,	0,	0,	1,	1,	1,	1,	1,	1,	0,	0,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	0,	0,	1,	1,	1,	1,	1,	1,	0,	0,	0,	0,	1,	1,	1,	1,	1,	1,	1,	1,	0],
[0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	1,	1,	1,	1,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0],
[0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	1,	1,	1,	1,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0],
[0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	1,	1,	1,	1,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0],
[0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	1,	1,	1,	1,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0],
[0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0]
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


class ShipCourse:
    def __init__(self, initA = 7, initB = 30):
        self.A = initA  # x coordinate
        self.O = initB  # y coordinate
        self._recalc_neighbourhood()

    def forecast(self, ndays):
        courseToday = '090'

        print("Start state: " + courseToday)
        print("Initial position: ({}, {})".format(self.A, self.O))

        courseList = self.calc_forecast(courseToday, ndays)

        print("Possible states: " + str(courseList))
        print("End state after {} days: {}".format(ndays, courseList[ndays - 1]))
        print("End position: ({}, {})".format(self.A, self.O))


    def calc_forecast(self, initial_course, ndays):
        courses = []

        next = initial_course
        for nday in range(ndays):

            print('>> course[{}]: {}'.format(nday, next))
            print('>> pos[{}] ({}, {})'.format(nday, self.A, self.O))

            next = self.forecast_next_change(next)
            courses.append(next)

            print('>> next_course[{}]: {}'.format(nday, next))

            self._recalc_position(next)
            self._recalc_neighbourhood()

            print('<< pos[{}] ({}, {})'.format(nday, self.A, self.O))
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

        v000 = carte[self.O][self.C]
        v045 = carte[self.N][self.C]
        v090 = carte[self.N][self.A]
        v135 = carte[self.N][self.B]
        v180 = carte[self.O][self.B]
        v225 = carte[self.M][self.B]
        v270 = carte[self.M][self.A]
        v315 = carte[self.M][self.C]

        print('>> {}'.format(transitions))
        if v000 == 0:
            transitions.pop('000')
        if v045 == 0:
            transitions.pop('045')
        if v090 == 0:
            transitions.pop('090')
        if v135 == 0:
            transitions.pop('135')
        if v180 == 0:
            transitions.pop('180')
        if v225 == 0:
            transitions.pop('225')
        if v270 == 0:
            transitions.pop('270')
        if v315 == 0:
            transitions.pop('315')

        updated_transitions_with_probabilities = \
            ShipCourse._rebalance_probabilities(transitions)

        print('<< {}'.format(updated_transitions_with_probabilities))

        return chain.Chain._randomProbabilitySelector(updated_transitions_with_probabilities)

    def _recalc_position(self, next):
        if next == "000":
            self.A = self.A+1
        if next == "045":
            self.A = self.A+1
            self.O = self.O+1
        if next == "090":
            self.O = self.O+1
        if next == "135":
            self.A = self.A-1
            self.O = self.O+1
        if next == "180":
            self.A = self.A-1
        if next == "225":
            self.A = self.A-1
            self.O = self.O-1
        if next == "270":
            self.O = self.O-1
        if next == "315":
            self.A = self.A+1
            self.O = self.O-1

    def _recalc_neighbourhood(self):
        self.B = self.A - 1 # Sud
        self.C = self.A + 1  # Nord
        self.M = self.B - 1  # West
        self.N = self.B + 1  # East

    @staticmethod
    def _rebalance_probabilities(transitions):
        collection = list(transitions.items())
        remaining = sum(item[1] for item in collection)
        updated = [(item[0], round(item[1]/remaining, 3)) for item in collection]
        return dict(updated)
