import json
import argparse


def main():
    parser = create_parser()
    namespace = parser.parse_args()
    if not namespace.file:
        exit('Укажите путь к файлу. Формат файла должен быть json')
    content_json_file = load_data(namespace.file)
    print(pretty_print_json(content_json_file))


def create_parser():
    parser = argparse.ArgumentParser(prefix_chars='-+/')
    parser.add_argument('file', nargs='?', default=False, type=is_json, help='Path to json file')
    return parser


def is_json(file_name):
    return file_name.lower().endswith('.json')


def load_data(filepath):
    with open(filepath, 'r') as file:
        return json.load(file)


def pretty_print_json(json_content):
    return json.dumps(json_content, indent=4, ensure_ascii=False, sort_keys=True)


if __name__ == '__main__':
    main()
