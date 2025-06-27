from tinydb import TinyDB

db = TinyDB('templates.json')

db.insert({
    "name": "Форма заказа",
    "customer": "text",
    "order_id": "text",
    "дата_заказа": "date",
    "contact": "phone"
})

db.insert({
    "name": "Проба",
    "f_name1": "email",
    "f_name2": "date"
})
