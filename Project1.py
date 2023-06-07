# Slotting machine
import random

MIN_LINES = 1
MAX_LINES = 3

# max and min bet per line in dollar
MAX_BET = 100
MIN_BET = 1

# describing the slotting machine
ROWS = 3
COLS = 5

# symbols in the slot machine
symbol_count = {
    "A":2,
    "B":4,
    "C":6,
    "D":8,
    "E":10
}

# symbols value in the slot machine
symbol_value = {
    "A":5,
    "B":4,
    "C":3,
    "D":2,
    "E":1
}

def isfloat(x):
    try:
        float(x)
        return True
    except ValueError:
        return False

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
        
    return winnings, winning_lines


def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
            
    columns = []
    
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        
        columns.append(column)
        
    return columns
           
def display_slot_machine(rows, cols, columns):
    
    for i in range(cols):
        
        for j in range(rows):
            
            if j!=rows - 1:
                print(columns[i][j], end= " | ")
            else:
                print(columns[i][j])            
        
def deposit():
    while True:
        amount = input("What would you like to deposit? $")
        if isfloat(amount) and float(amount)>0:
            amount = float(amount)
            break
        else:
            print("ENTER a valid amount: ")
    
    return amount

def get_number_of_lines():
    while True:
        lines = input(f"Enter the number of lines to bet on ({1}-{MAX_LINES}): ")
        if lines.isdigit() and 1 <= int(lines) <= MAX_LINES:
            
            lines = int(lines)
            break
        else:
            print(f"ENTER a valid positive integer in the range: [{MIN_LINES}, {MAX_LINES}]: ")
    
    return lines
    
def get_bet():
    while True:
        amount = input("What would you like to BET on each line? $")
        if isfloat(amount) and float(amount)>0 and MIN_BET <= float(amount) <= MAX_BET:
            amount = float(amount)
            break
        else:
            print(f"ENTER a valid BET in the range:[${MIN_BET}, ${MAX_BET}]: ")
    
    return amount

def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        
        if total_bet > balance:
            print(f"You do not have enough to bet that amount, your CURRENT BALANCE is {balance}")
        else:
            break
    
    print(f"you are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")
        
    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    
    display_slot_machine(ROWS, COLS, slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    
    print(f"You won ${winnings}")
    print(f"You won on lines", *winning_lines)
    
    return winnings - total_bet
 
def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        reply = input("Press ENTER to spin (q to quit).")
        
        if reply == "q":
            break
        balance += spin(balance)
    
    print(f"You are left with ${balance}")

main()