# Setup

## Clone the repository

- Download [Git for Windows](https://git-scm.com/) if not already installed on the machine.
- Clone this repository in an empty working folder:

```
> git clone https://github.com/springcomp/markov_python markov
```

# Setup Python virtual environment

Run the following commands:

```sh
> python -m venv .
> source bin/activate
> pip install -r requirements.txt

> pytest tests/test_graph.py
> pytest tests/test_chain.py
> pytest tests/test_probabilities.py
```

# Usage

## Graph

```python
from markov import graph

g = graph.Graph()
g.addTransition('E', 'E', 0.3)
g.addTransition('E', 'A', 0.7)
g.addTransition('A', 'E', 0.4)
g.addTransition('A', 'A', 0.6)

c.getTransitions('E')
```

This returns:

```python
{'E': 0.3, 'A': 0.7}
```

## Markov Chain

```python
from markov import chain

c = chain.Chain()
c.addTransition('E', 'E', 0.3)
c.addTransition('E', 'A', 0.7)
c.addTransition('A', 'E', 0.4)
c.addTransition('A', 'A', 0.6)

next = c.getNextState('E')
```

This returns the next state based on weighted probabilities.
Run multiple times to see next states.

## Ship Course Forecast

```python
from markov import markov
markov.forecast(21)
```



