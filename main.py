import random

ROWS =3
COLS=3

symbol_count={
    "A": 2,
    "B":4,
    "C":6,
    "D":6

}

MAX_LINES=3
MAX_BET =100
MIN_BET =1

def get_slot_machine_spin(rows,cols,symbols):
    all_symbols=[]
    for symbol,symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    colums=[]
    for col in range(cols):
        colum=[]
        for row in range(rows):
            value=random.choice(all_symbols)

def deposit():
    while True:
        amount=input("what do you like deposit? $ ")
        if amount.isdigit():
            amount=int(amount)
            if amount>0:
                break
            else:
                print("amount must be greater than 0.")
        else:
            print("please enter a number")

    return amount

def get_number_of_line():
    while True:
        lines=input("Enter the number of lines to bet on (1-"+str(MAX_LINES)+")? ")
        if lines.isdigit():
            lines=int(lines)
            if 1<=lines<=MAX_LINES:
                break
            else:
                print("Enter a valid number of lines")
        else:
            print("please enter a number")

    return lines
def get_bet():
    while True:
        amount = input("What would you like to bet on each line? $ ")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount should be between ${MIN_BET} and ${MAX_BET}.")
        else:
            print("Please enter a valid number.")

    return amount


def main():
    balance=deposit()
    lines=get_number_of_line()
    bet=get_bet()
    total_bet=bet*lines
    print(f"You are betting $ {bet} on {lines} lines . Total bet is equal to ${total_bet}")
    
main()
