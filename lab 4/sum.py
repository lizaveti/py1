# TODO решите задачу
import json


def task() -> float:
    file_path = "input.json"
    with open(file_path) as f:
        data = json.load(f)

    result = 0
    for dct in data:
        result += dct['score'] * dct['weight']

    return round(result, 3)


print(task())
