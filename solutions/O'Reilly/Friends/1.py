# !/usr/bin/python
# -*- coding: utf-8 -*-

class Friends(object):
    def __init__(self, connections):
        super(Friends, self).__init__()
        self._data = {}
        self._add_connections(connections)

    def add(self, connection):
        is_exists = self.is_exists(connection)
        self._add_connection(connection)

        return (not is_exists)

    def remove(self, connection):
        is_exists = self.is_exists(connection)

        if (not is_exists):
            return False

        self._remove_connection(connection)

        return True

    def names(self):
        return self._data.keys()

    def connected(self, name):
        if (name not in self._data):
            return set()

        return self._data[name]

    def is_exists(self, connection):
        copy = connection.copy()
        first, second = copy.pop(), copy.pop()

        return (first in self._data and second in self._data[first])

    def _add_connection(self, connection):
        copy = connection.copy()
        first, second = copy.pop(), copy.pop()
        add = lambda i, x: self._data[i].add(x) if i in self._data else self._data.update({i: {x}})

        add(first, second)
        add(second, first)

    def _add_connections(self, connections):
        for connection in connections:
            self._add_connection(connection)

    def _remove_connection(self, connection):
        copy = connection.copy()
        first, second = copy.pop(), copy.pop()
        removeValue = lambda i, x: self._data[i].remove(x) if True else None
        removeKey = lambda i: self._data.pop(i) if not len(self._data[i]) else None

        removeValue(first, second)
        removeValue(second, first)
        removeKey(first)
        removeKey(second)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    letter_friends = Friends(({"a", "b"}, {"b", "c"}, {"c", "a"}, {"a", "c"}))
    digit_friends = Friends([{"1", "2"}, {"3", "1"}])
    assert letter_friends.add({"c", "d"}) is True, "Add"
    assert letter_friends.add({"c", "d"}) is False, "Add again"
    assert letter_friends.remove({"c", "d"}) is True, "Remove"
    assert digit_friends.remove({"c", "d"}) is False, "Remove non exists"
    assert letter_friends.names() == {"a", "b", "c"}, "Names"
    assert letter_friends.connected("d") == set(), "Non connected name"
    assert letter_friends.connected("a") == {"b", "c"}, "Connected name"
