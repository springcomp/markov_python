import numpy as np
import random as rm

from markov import chain

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

def forecast(ndays):
    courseToday = '090'
    courseList = calc_forecast(courseToday, ndays)

    print("Start state: " + courseToday)
    print("Possible states: " + str(courseList))
    print("End state after "+ str(ndays) + " days: " + courseToday)

def calc_forecast(initial_course, ndays):
    courses = []
    next = initial_course
    for _ in range(ndays):
        next = forecast_next_change(next)
        courses.append(next)

    return courses

def forecast_next_change(state):
    next = c.getNextState(state, select_transition)
    return next

def select_transition(transitions):
    return chain.Chain._randomProbabilitySelector(transitions)
