"""Exact bounded event-token adapter; source detector and pulse control are assumed."""
from itertools import product
import json

CELLS = ("A", "B")
CAPACITY = 2

class Controller:
    def __init__(self):
        self.words = [None] * CAPACITY
        self.pending = []
        self.next_ordinal = {c: 1 for c in CELLS}
        self.rejected = []

    def root(self, cell):
        assert cell in CELLS
        if None not in self.words:
            self.rejected.append(cell)
            return False
        token = (cell, self.next_ordinal[cell])
        self.next_ordinal[cell] += 1
        slot = self.words.index(None)
        # Assumed pulse: a prepared blank slot is mapped to an orthogonal token word.
        self.words[slot] = token
        self.pending.append(token)
        return True

    def ack(self, token):
        if not self.pending or self.pending[0] != token:
            return False
        self.pending.pop(0)
        return True


def run():
    mapping = {}
    for n in range(CAPACITY + 1):
        for history in product(CELLS, repeat=n):
            c = Controller()
            for cell in history:
                assert c.root(cell)
            words = tuple(c.words)
            assert words not in mapping or mapping[words] == history
            mapping[words] = history
            assert tuple(c.pending) == tuple(w for w in words if w is not None)
            if n:
                assert not c.ack(("A", 999))
                assert c.ack(c.pending[0])
                assert not c.ack(words[0])  # Duplicate acknowledgment.
            if n == CAPACITY:
                before = tuple(c.words)
                assert not c.root("A")
                assert tuple(c.words) == before
                assert c.rejected == ["A"]
    assert len(mapping) == 1 + 2 + 4
    assert mapping[(('A', 1), ('B', 1))] == ('A', 'B')
    assert mapping[(('B', 1), ('A', 1))] == ('B', 'A')
    assert mapping[(('A', 1), ('A', 2))] == ('A', 'A')
    return {"status":"PASS", "cells":len(CELLS), "capacity":CAPACITY,
            "distinct_histories_checked":len(mapping),
            "collision_count":len(mapping)-len(set(mapping)),
            "scope":"resolved token inputs; prepared orthogonal slots; external pulse; no native root or backreaction law"}

if __name__ == '__main__':
    print(json.dumps(run(), indent=2))
