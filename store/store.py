""" Store module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * title (string): Title of the game
    * manufacturer (string)
    * price (number): Price in dollars
    * in_stock (number)
"""

import ui
import data_manager
import common

file_name = 'store/games.csv'


def start_module():
    """
    Starts this module and displays its menu.
     * User can access default special features from here.
     * User can go back to main menu from here.

    Returns:
        None
    """

    option_list = ['Show table', 'Add', 'Remove', 'Update', 'Get counts by manufacturers',
                   'Get average by manufacturer']
    title = 'Store Module'
    store_table = data_manager.get_table_from_file('store/games.csv')
    while True:
        option = common.general_start_module(option_list, title)
        if option == "1":
            show_table(store_table)
        elif option == "2":
            add(store_table)
        elif option == "3":
            message = 'Enter item\'s ID you want to delete'
            item_to_delete = ui.get_inputs([message], '')[0]
            remove(store_table, item_to_delete)
        elif option == "4":
            message = 'Enter item\'s ID you want to update'
            item_to_update = ui.get_inputs([message], '')[0]
            update(store_table, item_to_update)
        elif option == "5":
            ui.print_result(get_counts_by_manufacturers(store_table), 'Count by manufacturer: ')
        elif option == "6":
            message = 'Enter manufacture to display average'
            manufacturer = ui.get_inputs([message], '')[0]
            ui.print_result(get_average_by_manufacturer(store_table, manufacturer), 'Average: ')
        elif option == "0":
            break
        else:
            raise KeyError("There is no such option.")


def show_table(table):
    """
    Display a table

    Args:
        table (list): list of lists to be displayed.

    Returns:
        None
    """

    titles = ['id', 'title', 'manufacturer', 'price', 'in-stock']
    ui.print_table(table, titles)


def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table (list): table to add new record to

    Returns:
        list: Table with a new record
    """

    labels = ['name', 'manufacturer']
    title = 'New item:'
    input_strings = ui.get_inputs(labels, title)
    try_labels = ['price', 'in-stock']
    input_list = common.check_for_int(try_labels)

    input_list.insert(0, input_strings[0])
    input_list.insert(1, input_strings[1])
    common.general_add(table, input_list)
    data_manager.write_table_to_file(file_name, table)
    return table


def remove(table, id_):
    """
    Remove a record with a given id from the table.

    Args:
        table (list): table to remove a record from
        id_ (str): id of a record to be removed

    Returns:
        list: Table without specified record.
    """

    common.general_remove(table, id_)
    data_manager.write_table_to_file(file_name, table)
    return table


def update(table, id_):
    """
    Updates specified record in the table. Ask users for new data.

    Args:
        table: list in which record should be updated
        id_ (str): id of a record to update

    Returns:
        list: table with updated record
    """

    title = 'New recipt:'
    labels = ['name', 'manufacturer']
    input_strings = ui.get_inputs(labels, title)
    try_labels = ['price', 'in-stock']
    input_list = common.check_for_int(try_labels)

    input_list.insert(0, input_strings[0])
    input_list.insert(1, input_strings[1])
    common.general_update(table, id_, input_list)
    data_manager.write_table_to_file(file_name, table)
    return table


# special functions:
# ------------------

def get_counts_by_manufacturers(table):
    """
    Question: How many different kinds of game are available of each manufacturer?

    Args:
        table (list): data table to work on

    Returns:
         dict: A dictionary with this structure: { [manufacturer] : [count] }
    """
    (manufacture) = 2
    list_of_manufactures = [table[n][manufacture] for n in range(len(table))]
    unique_manufactures = list(set(list_of_manufactures))
    list_of_counts = [0 for n in range(len(unique_manufactures))]
    for n in range(len(unique_manufactures)):
        for i in range(len(list_of_manufactures)):
            if unique_manufactures[n] == list_of_manufactures[i]:
                list_of_counts[n] += 1
    dict_of_manuf_count = dict(zip(unique_manufactures, list_of_counts))
    return dict_of_manuf_count
    # your code


def get_average_by_manufacturer(table, manufacturer):
    """
    Question: What is the average amount of games in stock of a given manufacturer?

    Args:
        table (list): data table to work on
        manufacturer (str): Name of manufacturer

    Returns:
         number
    """
    (games_in_stock, manufacture) = -1, 2
    list_of_games_in_stock = [float(table[n][games_in_stock]) for n in range(len(table)) if
                              table[n][manufacture] == manufacturer]
    sum_of_games_in_stock = 0
    for n in range(len(list_of_games_in_stock)):
        sum_of_games_in_stock += list_of_games_in_stock[n]
    try:
        average = float(sum_of_games_in_stock / len(list_of_games_in_stock))
        return average
    except ZeroDivisionError:
        ui.print_error_message(" There is no such manufacture")
