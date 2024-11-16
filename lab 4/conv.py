# TODO импортировать необходимые молули
import csv, json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task(filename, delimiter=',', newline='\n'):
    with open(filename) as f:
        data_list = []
        is_header = True
        for row in f:
            list_rows = row.rstrip().split(newline)
            for line in list_rows:
                if is_header:
                    headers = line.split(delimiter)
                    is_header = False
                    continue
                data_list.append(dict(zip(headers, line.split(delimiter))))
    return data_list


if __name__ == '__main__':
    # Нужно для проверки
    data = task(INPUT_FILENAME)

    with open(OUTPUT_FILENAME, "w") as f:
        json.dump(data, f, indent=4)

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
