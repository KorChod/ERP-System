""" Common module
implement commonly used functions here
"""
import random
from ui import *


def generate_random(table):
    """
    Generates random and unique string. Used for id/key generation:
         - at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letter
         - it must be unique in the table (first value in every row is the id)

    Args:
        table (list): Data table to work on. First columns containing the keys.

    Returns:
        string: Random and unique string
    """

    def generate():
        list_of_id_symbols = []
        list_of_id_symbols.append(chr(random.randint(65, 90)))  # upper case letter
        list_of_id_symbols.append(chr(random.randint(97, 122)))  # lower case letter
        list_of_id_symbols.append(str(random.randint(0, 9)))  # number
        list_of_id_symbols.append(str(random.randint(0, 9)))  # number
        list_of_id_symbols.append(chr(random.randint(65, 90)))  # upper case letter
        list_of_id_symbols.append(chr(random.randint(97, 122)))  # lower case letter
        list_of_id_symbols.append(chr(random.randint(33, 47)))  # special characters
        list_of_id_symbols.append(chr(random.randint(33, 47)))  # special characters
        id_word = ''.join(list_of_id_symbols)
        return id_word

    id_word = generate()
    list_of_unique_id = [table[n][0] for n in range(len(table))]
    while id_word in list_of_unique_id:
        id_word = generate()
    generated = id_word

    return generated


def general_start_module(list_of_options, title):
    print_menu(title, list_of_options, 'Exit to main menu')
    answer = get_inputs(['Please enter a number'], '')[0]
    return answer


def get_appropriate_list(file_name):
    with open(file_name) as f:
        table = list(f.readlines())
        table = [element.rstrip('\n') for element in table]
        table = [i.split(';') for i in table]
        return table


def general_add(table, input_list):
    id_and_input_list = [generate_random(table)]
    input_list = id_and_input_list + input_list
    table.append(input_list)
    return table


def general_remove(table, id_):
    list_of_indexes = [table[n][0] for n in range(len(table))]
    for i in range(len(list_of_indexes)):
        if list_of_indexes[i] == id_:
            del table[i]
    return table


def general_update(table, id_, things):
    update_list = [id_]
    input_list = update_list + list(things)
    for i in range(len(table)):
        if table[i][0] == id_:
            table[i] = input_list
    return table


def check_for_int(try_labels):
    input_list = []
    for i in range(len(try_labels)):
        while True:
            try:
                check_list = [try_labels[i]]
                check = int(get_inputs(check_list, '')[0])
                check = str(check)
                input_list.append(check)
                break
            except ValueError:
                print_error_message(f'{try_labels[i]} has to be a number')
    return input_list
