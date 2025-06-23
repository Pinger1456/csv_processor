import sys
import os
# Добавляем путь к корневой папке, чтобы видеть модули
sys.path.insert(
    0,
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), '..')
    )
)

from processor import apply_filter

rows = [
    {'name': 'A', 'rating': '4.5', 'brand': 'apple'},
    {'name': 'B', 'rating': '4.9', 'brand': 'xiaomi'},
]


def test_filter_gt():
    res = apply_filter(rows, 'rating', '>', '4.6')
    assert res == [rows[1]]


def test_filter_eq():
    res = apply_filter(rows, 'brand', '=', 'apple')
    assert res == [rows[0]]
