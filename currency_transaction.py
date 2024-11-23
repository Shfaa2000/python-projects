import os
import time

dollar = "    "
exchange_rates = {
    "": dollar, "USD": 1.0, "EUR": 0.85, "EGP": 30.9, "RMB": 6.5,}
def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")

def display_rates():
    print("Welcome to Cuerrency Converter:\n")
    for curency in exchange_rates:
        print(f"{curency}: {exchange_rates[curency]}")

def currency_converter():
    clear_terminal()
    display_rates()

    from_currency = input("\nChoose a currency to convert from: ").upper()
    while True:
        amount = float(input("Enter the amount: "))
        confirmation = input(f"\nYou entered {amount} {from_currency}. Confirm? (y/n): ").upper()
        if confirmation == "Y":
            break

    clear_terminal()
    display_rates()

    to_currency = input("\nChoose a currency to convert to: ").upper()

    print("Analyzing your request... Please wait.")
    time.sleep(2)
    print(f"Checking for {to_currency}'s best rates available .... Please wait")
    time.sleep(2)
    print(f"Getting a discount price for {from_currency} ... Please wait")
    time.sleep(2)

    #تحقق من اختيار العملات بشكل صحيح
    if from_currency not in exchange_rates or to_currency not in exchange_rates:
        print("Invaild currency. Convert canceled.")
        time.sleep(2)
        currency_converter()

    new_rates = exchange_rates[to_currency] / exchange_rates[from_currency]

    #حول العملة عن طريق معدل التحويل
    converted_amount = amount * new_rates
    clear_terminal()
    print(f"Preparing the deal from {from_currency} to {to_currency}........ Please wait\n")
    time.sleep(2)
    print(f"Exchange Rate: {from_currency} = {new_rates} {to_currency}\n\n")
    time.sleep(2)
    print(f"{amount} {from_currency} is equal to {round(converted_amount,2)} {to_currency}")
    time.sleep(1)

    accept_transaction = input(f"\nDo you accept this transaction? (y/n): ").upper()
    if accept_transaction == "Y":
        print("Transaction Sucessful!")
    else:
        print("Transaction Canceled.")

    another_conversion = input("\nDo you want to perform another conversion? (y/n): ").upper()
    if another_conversion == "Y":
        currency_converter()
    else:
        print("Thanks for using the currency converter!")

#start the currency converter
currency_converter()