import csv
from typing import List, Dict


def read_csv(file_path: str) -> List[Dict[str, str]]:
    with open(file_path, encoding='utf-8') as f:
        return list(csv.DictReader(f))


# Фильтрация строк по одному условию
def apply_filter(
    rows: List[Dict[str, str]],
    column: str,
    op: str,
    value: str
) -> List[Dict[str, str]]:
    def match(row):
        cell = row[column]
        try:
            cell_val = float(cell)
            value_val = float(value)
        except ValueError:
            cell_val = cell
            value_val = value
        if op == '=':
            return cell_val == value_val
        elif op == '>':
            return cell_val > value_val
        elif op == '<':
            return cell_val < value_val
        else:
            raise ValueError("Unknown operator")
    return list(filter(match, rows))


# Агрегация значений по столбцу: avg, min, max
def apply_aggregate(
    rows: List[Dict[str, str]],
    column: str,
    func: str
) -> Dict[str, float]:
    values = [float(row[column]) for row in rows]
    if func == 'avg':
        result = sum(values) / len(values)
    elif func == 'min':
        result = min(values)
    elif func == 'max':
        result = max(values)
    else:
        raise ValueError("Unsupported function")
    return {func: round(result, 2)}
