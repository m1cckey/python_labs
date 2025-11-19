import argparse
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname('C:/Users/sacre/PycharmProjects/python_labs/src/lib/text.py'))))
from src.lib.text import normalize, tokenize, count_freq, top_n

def read_file(file_path: str) -> str:
    """Чтение содержимого файла"""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Ошибка: Файл '{file_path}' не найден")
        exit(1)
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")
        exit(1)


def cat_command(input_file: str, number_lines: bool = False):
    """Реализация команды cat"""
    try:
        with open(input_file, 'r', encoding='utf-8') as file:
            lines = file.readlines()

            for i, line in enumerate(lines, 1):
                if number_lines:
                    print(f"{i:6d}\t{line.rstrip()}")
                else:
                    print(line.rstrip())

    except FileNotFoundError:
        raise FileNotFoundError("файл не найден")

def stats_command(input_file: str, top_count: int = 5):
    """Реализация команды stats"""
    try:
        # Читаем файл
        text = read_file(input_file)

        # Обрабатываем текст
        normalized_text = normalize(text)
        tokens = tokenize(normalized_text)
        frequencies = count_freq(tokens)
        top_words = top_n(frequencies, top_count)

        # Выводим результаты
        print(f"Всего слов: {len(tokens)}")
        print(f"Уникальных слов: {len(frequencies)}")
        print(f"\nТоп-{top_count} самых частых слов:")
        print("-" * 30)

        for i, (word, count) in enumerate(top_words, 1):
            print(f"{i:2d}. {word:<20} {count:>4}")

    except Exception as e:
        print(f"Ошибка при анализе текста: {e}")
        exit(1)


def main():
    parser = argparse.ArgumentParser(description="CLI‑утилиты лабораторной №6")
    subparsers = parser.add_subparsers(dest="command", required=True)

    cat_parser = subparsers.add_parser("cat", help="Вывести содержимое файла")
    cat_parser.add_argument("--input", required=True, help="Путь к входному файлу")
    cat_parser.add_argument("-n", action="store_true", help="Нумеровать строки")

    stats_parser = subparsers.add_parser("stats", help="Частоты слов")
    stats_parser.add_argument("--input", required=True, help="Путь к входному файлу")
    stats_parser.add_argument("--top", type=int, default=5, help="Количество топ-слов для вывода")

    args = parser.parse_args()

    if args.command == "cat":
        cat_command(args.input, args.n)
    elif args.command == "stats":
        stats_command(args.input, args.top)

if __name__ == "__main__":
    main()