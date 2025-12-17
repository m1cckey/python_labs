from dataclasses import dataclass
import datetime
import json


@dataclass
class Student:
    fio: str
    birthdate: str
    group: str
    gpa: float

    def __post_init__(self):
        try:
            datetime.striptime(self.birthdate, "%Y/%M/%D")
        except ValueError:
            print("check data format")

        if self.gpa <= 0 or self.gpa >= 5:
            raise ValueError("GPA must be between 0 and 5")

    def age(self) -> int:
        today = datetime.date.today()
        was_born = self.birthdate
        return today.year - was_born.year

    def to_dict(self):
        return {
            "fio": self.fio,
            "age": self.age(),
            "group": self.group,
            "gpa": self.gpa,
        }

    @classmethod
    def from_dict(cls, data: dict):
        return cls(fio=data["fio"], birthdate=data["birthdate"], group=data["group"])

    def __str__(self):
        return f"{self.name} ({self.group} age {self.age()}) gpa: {self.gpa} )"
