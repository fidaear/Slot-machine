import random

ROWS =3
COLS=3

symbol_count={
    "A": 2,
    "B":4,
    "C":6,
    "D":6
}

symbol_value={
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2,

}


MAX_LINES=3
MAX_BET =100
MIN_BET =1
def checks_winnings(colums,lines,bet,values):
    winnings=0
    winning_lines=[]
    for line in range(lines):
        symbol=colums[0][line]
        for colum in colums:
            symbol_to_check=colum[line]
            if symbol!=symbol_to_check:
                break
        else:
            winnings += values[symbol] *bet
            winning_lines.append(line+1) 

    return winnings , winning_lines


def get_slot_machine_spin(rows,cols,symbols):
    all_symbols=[]
    for symbol,symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    colums=[]
    for _ in range(cols):
        colum=[]
        current_symbols=all_symbols[:]
        for _ in range(rows):
            value=random.choice(current_symbols)
            current_symbols.remove(value)
            colum.append(value)

        colums.append(colum)
    
    return colums


def print_slot_machine(colums):
    for row in range(len(colums[0])):
        for i,colum in enumerate(colums):
            if i!=len(colums)-1:
              print(colum[row], end=" | ")
            else:
                print(colum[row], end="|")

        print()

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

def spin(balance):
    lines=get_number_of_line()
    bet=get_bet()
    total_bet=bet*lines
    print(f"You are betting $ {bet} on {lines} lines . Total bet is equal to ${total_bet}")

    slots=get_slot_machine_spin(ROWS,COLS,symbol_count)
    print_slot_machine(slots)
    winnings,winning_lines=checks_winnings(slots,lines,bet,symbol_value)

    print(f"You WON $ {winnings}.")
    print(f"You won on lines  ", *winning_lines)
    return winnings -total_bet


def main():
    balance=deposit()
    while True:
        print(f"Current balance is : ${balance} ")
        answer=input("Press enter to play (q to quit) ")
        if answer =="q":
            break 
        balance+=spin(balance) 
    print(f"You left with $ {balance}")

main()
