import sys

'''добавляем нужный нам путь в список путей откуда мложно импортировать модули'''
sys.path.append("C:/Users/sacre/PycharmProjects/python_labs/src/lib")
from src.lib.text import normalize, tokenize, count_freq, top_n
from io_txt_csv import read_text, write_csv
from pathlib import Path
import argparse

current_dir = Path(__file__).parent
project_root = current_dir.parent.parent



'''Функция которая читает содержимое файла'''
def read_file_content(file_path: Path, encoding: str = "utf-8") -> str:
    try:

        return read_text(file_path, encoding=encoding)
    except FileNotFoundError:
        raise FileNotFoundError(f'Ошибка: файл {file_path} не найден')

    except UnicodeDecodeError as error:
        raise UnicodeDecodeError(f'Ошибка кодировки: {error}. Попробуйте указать другую кодировку')

'''Всё что связано с третьей лабой'''
def calculate_word_frequencies(text: str) -> dict[str, int]:
    if not text.strip():
        return {}

    normalized_text = normalize(text, casefold=True, yo2e=True)
    tokens = tokenize(normalized_text)
    frequencies = count_freq(tokens)
    top = top_n(frequencies)
    return top

'''Запись в csv'''
def text_to_csv(rows, path = str(project_root / 'data' / 'lab04' / 'output.txt'), header=("word_count")) -> None:
    return write_csv(rows, path=path, header=header)

'''То что мне надо вывести в консоль'''
def console(text: str) -> str:

    tokens = tokenize(normalize(text))
    top_words = top_n(count_freq(tokens))
    res = f"Всего слов: {len(tokens)}"
    res += f"\nУникальных слов: {len(set(tokens))}"
    res += "\nТоп-5:"
    for word, count in top_words:
        res += f"\n{word}:{count}"

    return res


text_content = read_file_content(str(project_root / 'data' / 'lab04' / 'input.txt'))
text_to_csv(calculate_word_frequencies(text_content))
print(console(text_content))