import csv
from pathlib import Path
from typing import Sequence, Union


def read_text(path: Union[str, Path], encoding: str = "utf-8") -> str:
    path = Path(path) if isinstance(path, str) else path

    with open(path, 'r', encoding=encoding) as file:
        return file.read()


def write_csv(rows: Sequence, path: Union[str, Path], header: Union[Sequence, None] = None) -> None:

    if isinstance(path, str):
        path = Path(path)
    else:
        path = path

    with open(path, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)

        if header is not None:
            writer.writerow(header)

        for row in rows:
            writer.writerow(row)


