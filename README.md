Run the following commands:

```sh
> python -m venv .
> source bin/activate
> pip install -r requirements.txt

> pytest tests/test_graph.py
> pytest tests/test_chain.py
```

## Markov

```python
from markov import chain

c = chain.Chain()
c.addTransition('E', 'E', 0.3)
c.addTransition('E', 'A', 0.7)
c.addTransition('A', 'E', 0.4)
c.addTransition('A', 'A', 0.6)

next = c.getNextState('E')
```
