import argparse
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname('C:/Users/sacre/PycharmProjects/python_labs/src/lib/json_help.py'))))
from src.lib.json_help import json_to_csv, csv_to_json, csv_to_xlsx
def main():
    parser = argparse.ArgumentParser(description="Конвертеры данных")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p1 = sub.add_parser("json2csv")
    p1.add_argument("--in", dest="input", required=True, help="Входной JSON файл")
    p1.add_argument("--out", dest="output", required=True, help="Выходной CSV файл")

    p2 = sub.add_parser("csv2json")
    p2.add_argument("--in", dest="input", required=True, help="Входной CSV файл")
    p2.add_argument("--out", dest="output", required=True, help="Выходной JSON файл")

    p3 = sub.add_parser("csv2xlsx")
    p3.add_argument("--in", dest="input", required=True, help="Входной CSV файл")
    p3.add_argument("--out", dest="output", required=True, help="Выходной XLSX файл")

    args = parser.parse_args()


    if args.cmd == "json2csv":
        json_to_csv(args.input, args.output)
        print(f"Успешно конвертирован {args.input} в {args.output}")

    elif args.cmd == "csv2json":
        csv_to_json(args.input, args.output)
        print(f"Успешно конвертирован {args.input} в {args.output}")

    elif args.cmd == "csv2xlsx":
        csv_to_xlsx(args.input, args.output)
        print(f"Успешно конвертирован {args.input} в {args.output}")




if __name__ == "__main__":
    main()