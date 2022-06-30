from collections import Counter


def read_file() -> str:
    with open('text.txt', 'r') as file:
        count_values = Counter([is_valid_password(line.strip()) for line in file if line.strip()])
        return f'Quantity valid passwords: {count_values[True]}'


def is_valid_password(string: str) -> bool:
    data = string.split()
    try:
        symbol, start_count, end_count, new_string = data[0], int(data[1]), int(data[3]), ''.join(data[4:])
    except ValueError as e:
        # print(f'Wrong value --> {e}!')
        return False

    symbols_from_str = [i for i in new_string if i == symbol]
    return start_count <= len(symbols_from_str) <= end_count


if __name__ == "__main__":
    print(read_file())
