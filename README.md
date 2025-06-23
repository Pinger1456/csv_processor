# 📦 CSV Processor

CLI-утилита на Python для обработки CSV-файлов с возможностью фильтрации и агрегации данных.

---

## 🚀 Возможности

- 📌 Фильтрация строк по одному условию (`--where`)
- 📊 Агрегация (`--aggregate`) по одному числовому столбцу: `avg`, `min`, `max`
- 🧮 Совмещение фильтрации и агрегации
- 🧪 Покрытие критических функций unit-тестами (`pytest`)
- 🧹 Чистый код, соответствующий PEP8 + аннотации типов

---

## 📂 Пример CSV-файла

```csv
name,brand,price,rating
iphone 15 pro,apple,999,4.9
galaxy s23 ultra,samsung,1199,4.8
redmi note 12,xiaomi,199,4.6
poco x5 pro,xiaomi,299,4.4
````
---

## 🖼 Примеры выполнения
📋 Показ таблицы:
![Все товары](Examples/Products.jpg)

🔍 Фильтрация по бренду `Xiaomi`:
![Фильтрация по "Xiaomi" ](Examples/Min_rating_of_brand.jpg)

📊 Агрегация среднего значения рейтинга:
![Агрегация avg](Examples/Average_rating.jpg)

📑 Сортировка по рейтингу больше 4,5:
![Сортировка рейтинга](Examples/Sort_more_then_4,5.jpg)

---

## ⚙️ Установка

```bash
git clone https://github.com/your-username/csv-processor.git
cd csv-processor
python -m venv venv
source venv/bin/activate        # Linux/macOS
venv\Scripts\activate           # Windows

pip install -r requirements.txt
```

---

## 💻 Примеры запуска

📋 Показать весь файл:

```bash
python main.py --file products.csv
```

🔎 Фильтрация (по числовому значению):

```bash
python main.py --file products.csv --where "rating>4.7"
```

🔍 Фильтрация (по тексту):

```bash
python main.py --file products.csv --where "brand=apple"
```

📊 Агрегация:

```bash
python main.py --file products.csv --aggregate "rating=avg"
```

🔀 Фильтрация + агрегация:

```bash
python main.py --file products.csv --where "brand=xiaomi" --aggregate "rating=min"
```

---

## 🧪 Запуск тестов

```bash
pytest
```

---

## 📌 Заметки

* Фильтрация поддерживает `=`, `>`, `<`
* Агрегация работает только с числовыми колонками
* Используются только библиотеки стандартной библиотеки + `tabulate` и `pytest`


```
