# Формы и шаблоны (Simple Template Matcher)
Приложение которое ищет подходящий шаблон формы по переданным параметрам. Использует TinyDB.

## Пример запуска:
```bash
python3 app.py get_tpl --customer="Иван Иванов"
```

## Типы данных:
- email
- phone (+7 ХХХ ХХХ ХХ ХХ)
- date (DD.MM.YYYY или YYYY-MM-DD)
- text (всё остальное)

## Запуск тестов:
```bash
python3 test_requests.py
```
