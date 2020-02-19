""" Accounting module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * month (number): Month of the transaction
    * day (number): Day of the transaction
    * year (number): Year of the transaction
    * type (string): in = income, out = outflow
    * amount (int): amount of transaction in USD
"""

import ui
import data_manager
import common

file_name = 'accounting/items.csv'


def start_module():
    """
    Starts this module and displays its menu.
     * User can access default special features from here.
     * User can go back to main menu from here.

    Returns:
        None
    """
    option_list = ['Show table', 'Add', 'Remove', 'Update', 'Average Sales in a year']
    title = 'Acccounting Module'
    accounting_table = data_manager.get_table_from_file('accounting/items.csv')

    while True:
        option = common.general_start_module(option_list, title)
        if option == "1":
            show_table(accounting_table)
        elif option == "2":
            add(accounting_table)
        elif option == "3":
            message = 'Enter item\'s ID you want to delete'
            item_to_delete = ui.get_inputs([message], '')[0]
            remove(accounting_table, item_to_delete)
        elif option == "4":
            message = 'Enter item\'s ID you want to update'
            item_to_update = ui.get_inputs([message], '')[0]
            update(accounting_table, item_to_update)
        elif option == "5":
            message = 'Enter a year: '
            year = str(common.check_for_int(['year'])[0])
            ui.print_result(avg_amount(accounting_table, year), f'Average sales in {year}: ')
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
    titles = ['id', 'month', 'day', 'year', 'type', 'amount']
    ui.print_table(table, titles)


def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table (list): table to add new record to

    Returns:
        list: Table with a new record
    """

    labels = ['type']
    title = 'New recipt:'
    input_string = ui.get_inputs(labels, title)[0]
    try_labels = ['month', 'day', 'year', 'amount']
    input_list = common.check_for_int(try_labels)

    input_list.insert(3, input_string)
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

    table = common.general_remove(table, id_)
    data_manager.write_table_to_file(file_name, table)
    return table


def update(table, id_):
    """
    Updates specified record in the table. Ask users for new data.

    Args:
        table (list): list in which record should be updated
        id_ (str): id of a record to update

    Returns:
        list: table with updated record
    """

    things_to_change = ['type']
    input_string = ui.get_inputs(things_to_change, '')[0]
    try_labels = ['month', 'day', 'year', 'amount']
    input_list = common.check_for_int(try_labels)
    input_list.insert(3, input_string)
    common.general_update(table, id_, input_list)
    data_manager.write_table_to_file(file_name, table)

    return table


# special functions:
# ------------------


def avg_amount(table, year):
    """
    Question: What is the average (per item) profit in a given year? [(profit)/(items count)]

    Args:
        table (list): data table to work on
        year (number)

    Returns:
        number
    """
    list_of_year = [[row[4], row[5]] for row in table if row[3] == year]

    profit = [int(list_of_year[n][1]) if list_of_year[n][0] == 'in' else -int(list_of_year[n][1]) for n in
              range(len(list_of_year))]

    sum_ = 0
    for element in profit:
        sum_ += element

    average_profit = float(sum_ / len(table))
    return average_profit
