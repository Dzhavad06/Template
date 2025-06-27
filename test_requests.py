import os

def run_test(args):
    print(f"Тест: {' '.join(args)}")
    os.system("python3 app.py " + " ".join(args))

tests = [
    ["get_tpl", "--customer=John Smith", "--дата_заказа=27.05.2025"],
    ["get_tpl", "--f_name1=aaa@bbb.ru", "--f_name2=27.05.2025"],
    ["get_tpl", "--tumba=27.05.2025", "--yumba=+7 903 123 45 78"]
]

for test in tests:
    run_test(test)
