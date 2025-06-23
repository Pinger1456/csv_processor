import sys
import os
# Добавляем путь к корневой папке, чтобы видеть модули
sys.path.insert(
    0,
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), '..')
    )
)

from processor import apply_aggregate


rows = [
    {'rating': '4.0'},
    {'rating': '5.0'}
]


def test_avg():
    assert apply_aggregate(rows, 'rating', 'avg') == {'avg': 4.5}


def test_min():
    assert apply_aggregate(rows, 'rating', 'min') == {'min': 4.0}


def test_max():
    assert apply_aggregate(rows, 'rating', 'max') == {'max': 5.0}
