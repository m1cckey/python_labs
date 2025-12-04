import json
from models import student


def students_to_json(students: list[student], path: str):
    data = [s.to_dict() for s in students]
    with open(path, "w", encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def studentd_from_json(path: str) -> list[student]:
    with open(path, "r", encoding='utf-8') as f:
        data = json.load(f)
        return [student.from_dict(i) for i in data]

