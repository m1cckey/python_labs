import csv
import json
from pathlib import Path



def json_to_csv(json_path: str, csv_path: str) -> None:

    path = Path(json_path)

    if not path.exists():
        raise FileNotFoundError("JSON файл не найден")

    if path.suffix.lower() != '.json':
        raise ValueError("Неверный тип файла")

    try:
        with open(json_path, 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
    except json.JSONDecodeError:
        raise ValueError("Ошибка декодирования JSON")

    if not isinstance(data, list):
        raise ValueError("JSON должен содержать список объектов")

    if not data:
        raise ValueError("JSON файл пуст")


    all_fields = set()
    for item in data:
        if not isinstance(item, dict):
            raise ValueError("Все элементы JSON должны быть словарями")
        all_fields.update(item.keys())

    fieldnames = sorted(all_fields)

    try:
        with open(csv_path, 'w', encoding='utf-8', newline='') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()


            for item in data:
                row = {field: item.get(field, '') for field in fieldnames}
                writer.writerow(row)

    except Exception as e:
        raise ValueError(f"Ошибка записи CSV: {e}")


def csv_to_json(csv_path: str, json_path: str) -> None:

    path = Path(csv_path)

    if not path.exists():
        raise FileNotFoundError(f"CSV файл не найден")

    if path.suffix.lower() != '.csv':
        raise ValueError(f"получено разрешение {path.suffix} a не .csv")

    try:
        with open(csv_path, 'r', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file)

            if reader.fieldnames is None:
                raise ValueError("CSV файл не содержит заголовков")

            data = list(reader)

    except Exception as e:
        raise ValueError(f"Ошибка чтения CSV: {e}")

    if not data:
        raise ValueError("CSV файл пуст`")

    try:
        with open(json_path, 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, ensure_ascii=False, indent=2)
    except Exception as e:
        raise ValueError(f"Ошибка записи JSON: {e}")


json_to_csv("C:/Users/sacre/PycharmProjects/python_labs/data/lab05/samples/people.json", "C:/Users/sacre/PycharmProjects/python_labs/data/lab05/out/people_from_json.csv")


csv_to_json("C:/Users/sacre/PycharmProjects/python_labs/data/lab05/samples/people.csv", "C:/Users/sacre/PycharmProjects/python_labs/data/lab05/out/cities_from_csv.json")
