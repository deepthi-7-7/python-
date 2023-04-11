import random

MAXLINES=3
MAXBET=100
MINBET=1
COLS=3
ROWS=3
symbol_count={
    'A':2,
    'B':4,
    'C':6,
    'D':8}
symbol_value={
    'A':5,
    'B':4,
    'C':3,
    'D':2}


def check_winning(columns,lines,bet,values):
    winning=0
    winning_lines=[]
    for line in range(lines):
        symbol=columns[0][line]
        for column in columns:
            symbol_to_check=column[line]
            if symbol !=symbol_to_check:
                break
        else:
            winning+=values[symbol]*bet
            winning_lines.append(line+1)
    return winning,winning_lines


def get_slot_machine(rows,cols,symbols):
    all_symbols=[]
    for symbol,symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    
    columns=[]
    for _ in range(cols):
        column=[]
        current_Symbols=all_symbols[:]
        for _ in range(rows):
            value=random.choice(current_Symbols)
            current_Symbols.remove(value)
            column.append(value)

        columns.append(column)
    
    return columns



def slot_machine(columns):
    for row in range(len(columns[0])):
        for i,column in enumerate(columns):
            if i!=len(column)-1:
                print(column[row],end=" | ")
            else:
                print(column[row],end="")

        print()


def deposit():
    while True:
        amount=input('enter what would you like to deposit here: $')
        if amount.isdigit():
            amount=int(amount)
            if amount>0:
                break
            else:
                print("amount should be greater than 0")
        else:
            print("please enter a number")
    return amount



def get_number_of_lines():
    while True:
        lines=input("enter the number of lines you want to bet on (1-"+str(MAXLINES)+")? ")
        if lines.isdigit():
            lines=int(lines)
            if 1<=lines<=MAXLINES:
                break
            else:
                print("enter a valid number of lines")
        else:
            print("please enter a number")

    return lines



def get_bet():
    while True:
        amount=input("enter the amount you want to bet on each line: $")
        if amount.isdigit():
            amount=int(amount)
            if MINBET<=amount<=MAXBET:
                break
            else:
                print(f"the bet must be in between ${MINBET} and ${MAXBET}")
        else:
            print("please enter a number")
    return amount

def spin(balance):
    lines=get_number_of_lines()
    while True:
        bet=get_bet()
        total_bet=bet * lines
        if total_bet>balance-bet:
            print(f"you don't have enough money to bet. Your current balance is ${balance}")
        else:
            break
    print(f"You are betting ${bet} on {lines} lines. Your total bet is ${total_bet}")

    slots=get_slot_machine(ROWS,COLS,symbol_count)
    slot_machine(slots)
    
    winning,winning_lines=check_winning(slots,lines,bet,symbol_value)
    print(f"you won ${winning}")
    print(f'you won on the lines: ',*winning_lines)

    return winning - total_bet


def main():
    balance=deposit()
    while True:
        print(f"your current balance is ${balance}")
        answer=input("press enter to paly (q to quit)")
        if answer=='q':
            break
        balance += spin(balance)

    print(f"you left with ${balance}")

main()
