# You have two files. The first one contains the current exchange rate of different currencies to BGN and the other
# contains different amounts of money. You have to pass the two file names and the output should be the amount of money
# for each currency in the second file. You have to skip the lines that contain only whitespaces.
# ("INVALID INPUT" is the only allowed message if something is wrong)

import os
import sys

# We check if the line contains anything else than whitespaces.
def skip_empty_rows(line):

    if not " " in line or not "\t" in line or not " \n" in line:
        return False
    return True


def read_exchange(file_name):

    exchange_list = {}

    with (open(os.path.abspath(file_name), "r")) as exchage_file:
        for exchange in exchage_file:

            # If we find empty row we skip it.
            if skip_empty_rows(exchange):
                continue

            exchange = exchange.strip("\n")

            # Here we are "unpacking" the two values. If there is a problem with the "unpacking" an exception will be
            # raised so we will know the file has.
            name, value = exchange.split(" ")
            value = float(value)

            # If the value can not be casted to float there will be exception raised also. If the name is not
            # instance of string we return "INVALID INPUT".
            if isinstance(name, str):
                exchange_list[name] = value
            else:
                return "INVALID INPUT"

    return exchange_list

def read_amount(file_name):

    amount_list = []

    with (open(os.path.abspath(file_name), "r")) as amount_file:
        for amount in amount_file:

            if skip_empty_rows(amount):
                continue

            amount = amount.strip("\n")

            # "Unpacking" again.
            money_amount, currency = amount.split(" ")
            money_amount = float(money_amount)
            if isinstance(currency, str):

                # The list is filled with dictionaries.
                amount_value = {currency: money_amount}
                amount_list.append(amount_value)
            else:
                return "INVALID INPUT"

    return amount_list

def main():

    # The names of the files are passed as command line arguments.
    exchange_file = sys.argv[1]
    amount_file = sys.argv[2]

    try:
        exchange_result = read_exchange(exchange_file)
        amount_result = read_amount(amount_file)

        # If something went wrong(exception raised) or one of the files returned "INVALID INPUT".
        if exchange_result == "INVALID INPUT" or amount_result == "INVALID INPUT":
            print("INVALID INPUT")
        else:
            for amount in amount_result:
                for key in amount.keys():

                    # The result is calculated and displayed by the second decimal place as valid price.
                    res = amount.get(key)/exchange_result.get(key)
                    print("{:.2f}".format(res))

    except Exception:
        print("INVALID INPUT")

if __name__ == '__main__':
    main()
