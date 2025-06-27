import re
from datetime import datetime
from tinydb import TinyDB
import sys

def is_date(val):
    for fmt in ("%d.%m.%Y", "%Y-%m-%d"):
        try:
            datetime.strptime(val, fmt)
            return True
        except ValueError:
            continue
    return False

def is_phone(val):
    return bool(re.fullmatch(r"\+7 \d{3} \d{3} \d{2} \d{2}", val))

def is_email(val):
    return bool(re.fullmatch(r"[^@]+@[^@]+\.[^@]+", val))

def get_type(val):
    if is_date(val):
        return "date"
    if is_phone(val):
        return "phone"
    if is_email(val):
        return "email"
    return "text"

def parse_args(args):
    result = {}
    for arg in args:
        if arg.startswith("--") and "=" in arg:
            key, val = arg[2:].split("=", 1)
            result[key] = val
    return result

def find_template(db, params):
    best_match = None
    best_score = 0

    for tpl in db:
        if "name" not in tpl:
            continue

        matched = 0
        total = 0
        for key in tpl:
            if key == "name":
                continue
            total += 1
            if key in params and get_type(params[key]) == tpl[key]:
                matched += 1

        score = matched / total if total > 0 else 0

        if score > best_score:
            best_score = score
            best_match = tpl["name"]

    return best_match if best_score > 0 else None

if __name__ == "__main__":
    db = TinyDB("templates.json")
    params = parse_args(sys.argv[2:])

    tpl_name = find_template(db.all(), params)

    if tpl_name:
        print(tpl_name)
    else:
        result = {k: get_type(v) for k, v in params.items()}
        print(result)
