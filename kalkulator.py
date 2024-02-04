import sys
import logging
logging.basicConfig(level=logging.DEBUG, format='%(message)s')

def calculator(action, a, b):
    if action == 1:
        return a + b
    elif action == 2:
        return a - b
    elif action == 3:
        return a * b
    elif action == 4:
        return a / b
    

if __name__ == '__main__':
    action = int(input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: "))
    first_num = float(input("Podaj pierwszą liczbę: "))
    second_num = float(input("Podaj drugą liczbę: "))

    if action == 1:
        logging.debug(f"Dodaję {first_num} i {second_num}")
    elif action == 2:
        logging.debug(f"Odejmuję {second_num} od {first_num}")
    elif action == 3:
        logging.debug(f"Mnożę {first_num} i {second_num}")
    elif action == 4:
        logging.debug(f"Dzielę {first_num} przez {second_num}")

    result = calculator(action, first_num, second_num)
    print(round(result, 2))




