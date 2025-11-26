import csv
from pathlib import Path

import openpyxl


def csv_to_xlsx(csv_path: str, xlsx_path: str) -> None:

    path = Path(csv_path)

    if not path.exists():
        raise FileNotFoundError(f"CSV файл не найден")

    if path.suffix.lower() != ".csv":
        raise ValueError(f"Неверный тип файла: ожидается .csv, получен {path.suffix}")

    with open(csv_path, "r", encoding="utf-8") as csv_file:
        reader = csv.reader(csv_file)
        data = list(reader)

    if not data:
        raise ValueError("CSV файл пуст")

    if not data[0]:
        raise ValueError("Первая строка CSV пуста")

    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.title = "Sheet1"

    for row_idx, row in enumerate(data, 1):
        for col_idx, value in enumerate(row, 1):
            sheet.cell(row=row_idx, column=col_idx, value=value)

    for column in sheet.columns:
        max_length = 0
        column_letter = column[0].column_letter

        for cell in column:
            try:
                if cell.value:
                    max_length = max(max_length, len(str(cell.value)))
            except:
                pass

        adjusted_width = max(max_length + 2, 8)
        sheet.column_dimensions[column_letter].width = adjusted_width

    workbook.save(xlsx_path)


print(
    csv_to_xlsx(
        "C:/Users/sacre/PycharmProjects/python_labs/data/lab05/samples/cities.csv",
        "C:/Users/sacre/PycharmProjects/python_labs/data/lab05/out/people.xlsx",
    )
)
