#How Do You Check The Presence Of A Key In A Dictionary?
d = {"key1": 10, "key2": 23}

if "key1" in d:
    print("this will execute")

if "nonexistent key" in d:
    print("this will not")


d = dict()

for i in range(100):
    key = i % 10
    d[key] = d.get(key, 0) + 1


from collections import defaultdict

d = defaultdict(int)

for i in range(100):
    d[i % 10] += 1
