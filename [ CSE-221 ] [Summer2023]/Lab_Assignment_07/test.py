actors = [
    { "name": "Sakib", "age": 45 },
    {"name": "Salman", "age": 50},
    {"name": "Shahrukh", "age": 55}
]
juniors = filter(lambda x : x["age"] < 50, actors)
print(actors)
print(list(juniors))