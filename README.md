# Prettify JSON

Скрипт, который выводит json в консоль в читаемом виде

## Требования

*Python3.5*

## Как запустить

```sh
python pprint_json.py <path to file>
```

## Пример запуска

```sh
python pprint_json.py
usage: pprint_json.py [-h] file
pprint_json.py: error: the following arguments are required: file
```

```sh
python pprint_json.py file.txt
usage: pprint_json.py [-h] file
pprint_json.py: error: argument file: invalid file format

```

```sh
python pprint_json.py file.json
{
    "geometry": {
        "coordinates": [
            37.61230620948003,
            55.73473489837388
        ],
    }
}
```

## Цели проекта

Код создан в учебных целях. В рамках учебного курса по веб-разработке  - [DEVMAN.org](https://devman.org)
