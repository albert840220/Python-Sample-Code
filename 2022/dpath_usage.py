import dpath.util
x = {
    "a": {
        "b": {
            "3": 2,
            "43": 30,
            "c": [],
            "d": ['red', 'buggy', 'bumpers'],
        }
    }
}

print(x["a"]["b"]["3"])  # 2
print(dpath.util.get(x, '/a/b/3'))  # 2
