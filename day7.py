d = {"name": "jainam", "age": 18}

for key, value in d.items():
    print(f'key: {key}, value: {value}')

print('-------------------------------')

person = [
    {"name": "Alice", "age": 20},
    {"name": "Alice", "age": 29}
]

for p in person:
    for key, value in p.items():
        print(key, ":", value)
    print("---")
