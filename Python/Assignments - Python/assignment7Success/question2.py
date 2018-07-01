import iso8601
from myfun import get_reader


def run(f):
    csv_reader = get_reader(f)
    transaction_counts = {}
    for row in csv_reader:
        date = iso8601.parse_date(row[1])
        key = str(date.year) + "-0" + str(date.month) + "-0" + str(date.day) + " 0" + str(date.hour) + ":00"
        transaction_counts.setdefault(key, 0)
        transaction_counts[key] += 1
    for item in transaction_counts.items():
        print(item[0], " -> ", item[1], " transactions")
