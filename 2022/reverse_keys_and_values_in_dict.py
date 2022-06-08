old_dict = {"a": 1, "b": 2, "c": 3}

print(old_dict)  # {'a': 1, 'b': 2, 'c': 3}

new_dict = {k: v for v, k in old_dict.items()}

print(new_dict)  # {1: 'a', 2: 'b', 3: 'c'}
