from typing import Hashable

a_set = {(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (2, 8), (3, 9)}
it_ob = [(1, 4), (1, 5), (1, 6), [1, 7], [3, 9], (10, 11, 12)]
for i, ob in enumerate(it_ob):
    if not isinstance(ob, Hashable):
        try:
            it_ob[i] = tuple(ob)
        except TypeError:
            continue
b_set = set(it_ob)
print(set.difference(a_set, b_set))
print(set.difference(b_set, a_set))
print((a_set - b_set) | (b_set - a_set) == set.symmetric_difference(a_set, b_set))


a_dict = dict({1: '1', 2: '2', 3: '3', 4: '4', 5: '5'})
print(a_dict.items())
print(a_dict.pop(3))
print(a_dict)
a_dict.clear()
print(a_dict)

