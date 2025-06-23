import argparse
from tabulate import tabulate
from processor import read_csv, apply_filter, apply_aggregate
from utils import parse_condition, parse_aggregation


def main():
    # Настраиваем аргументы командной строки
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', required=True)
    parser.add_argument('--where')
    parser.add_argument('--aggregate')
    args = parser.parse_args()

    rows = read_csv(args.file)

    # Применяем фильтрацию, если указано --where
    if args.where:
        column, op, value = parse_condition(args.where)
        rows = apply_filter(rows, column, op, value)

    # Если указана агрегация — применяем, иначе выводим таблицу
    if args.aggregate:
        column, func = parse_aggregation(args.aggregate)
        result = apply_aggregate(rows, column, func)
        print(tabulate([result], headers="keys", tablefmt="grid"))
    else:
        print(tabulate(rows, headers="keys", tablefmt="grid"))


if __name__ == "__main__":
    main()
