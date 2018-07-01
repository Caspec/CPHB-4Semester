from myfun import get_reader


def run(f):
    result = avg_transaction_price(f)
    print('The average transaction price is: "' + str(result))


def avg_transaction_price(f):
    csv_data = get_reader(f)
    transactions_sum = 0
    counter = 0
    for row in csv_data:
        transactions_sum += float(row[5])
        counter += 1
    return transactions_sum / counter
