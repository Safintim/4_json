import json
import sys


def load_data(filepath):
    with open(filepath, 'r') as f:
        return json.load(f)


def pretty_print_json(data):
    return json.dumps(data, indent=4, sort_keys=True)


def main():
    filepath = sys.argv[1]
    data = load_data(filepath)
    print(pretty_print_json(data))


if __name__ == '__main__':
    main()
