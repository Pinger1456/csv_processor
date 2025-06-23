from typing import Tuple


# Разбор строки фильтрации: "rating>4.5" → ("rating", ">", "4.5")
def parse_condition(expr: str) -> Tuple[str, str, str]:
    for op in ['>=', '<=', '>', '<', '=']:
        if op in expr:
            column, value = expr.split(op)
            return column.strip(), op, value.strip()
    raise ValueError("Invalid filter expression")


# Разбор строки агрегации: "rating=avg" → ("rating", "avg")
def parse_aggregation(expr: str) -> Tuple[str, str]:
    if '=' in expr:
        column, func = expr.split('=')
        return column.strip(), func.strip()
    raise ValueError("Invalid aggregate expression")
