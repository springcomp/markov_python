from markov import markov

if __name__ == '__main__':
	m = markov.ShipCourse(7, 30)
	m.forecast(10, courseToday = '090')
	
