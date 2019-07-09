import json
import sys


def load_data(filepath):
    with open(filepath, 'r') as file:
        return json.load(file)


def pretty_print_json(json_content):
    return json.dumps(json_content, indent=4, sort_keys=True)


def main():
    filepath = sys.argv[1]
    json_content = load_data(filepath)
    print(pretty_print_json(json_content))


if __name__ == '__main__':
    main()
