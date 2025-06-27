Приложение которое ищет подходящий шаблон формы по переданным параметрам. Использует TinyDB.

## Как запустить:
python3 app.py get_tpl --customer="Иван Иванов" --дата_заказа="27.05.2025"

Типы данных:

email

phone (+7 ХХХ ХХХ ХХ ХХ)

date (DD.MM.YYYY или YYYY-MM-DD)

text (всё остальное)

Запуск тестов:

python3 test_requests.py

Структура проекта:

app.py — основной файл приложения

db.json — база шаблонов

init_db.py — генерация шаблонов

test_requests.py — тесты

README.md — описание проекта

Ссылка на репозиторий:

https://github.com/Dzhavad06/Template