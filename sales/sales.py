""" Sales module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * title (string): Title of the game sold
    * price (number): The actual sale price in USD
    * month (number): Month of the sale
    * day (number): Day of the sale
    * year (number): Year of the sale
"""

import ui
import data_manager
import common

file_name = 'sales/sales.csv'


def start_module():
    """
    Starts this module and displays its menu.
     * User can access default special features from here.
     * User can go back to main menu from here.

    Returns:
        None
    """

    option_list = ['Show table', 'Add', 'Remove', 'Update', 'Get lowest price item id']
    title = 'Sales module'
    sales_table = data_manager.get_table_from_file('sales/sales.csv')

    while True:
        option = common.general_start_module(option_list, title)
        if option == "1":
            show_table(sales_table)
        elif option == "2":
            add(sales_table)
        elif option == "3":
            message = 'Enter item\'s ID you want to delete'
            item_to_delete = ui.get_inputs([message], '')[0]
            remove(sales_table, item_to_delete)
        elif option == "4":
            message = 'Enter item\'s ID you want to update'
            item_to_update = ui.get_inputs([message], '')[0]
            update(sales_table, item_to_update)
        elif option == "5":
            ui.print_result(get_lowest_price_item_id(sales_table), 'Lowest price item is: ')
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

    titles = ['id', 'title', 'price', 'month', 'day', 'year']
    ui.print_table(table, titles)


def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table (list): table to add new record to

    Returns:
        list: Table with a new record
    """

    labels = ['title']
    title = 'New sale:'
    input_string = ui.get_inputs(labels, title)[0]
    try_labels = ['price', 'month', 'day', 'year']
    input_list = common.check_for_int(try_labels)

    input_list.insert(0, input_string)
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
        table (list): list in which record should be updated
        id_ (str): id of a record to update

    Returns:
        list: table with updated record
    """

    things_to_change = ['title']
    input_string = ui.get_inputs(things_to_change, '')[0]
    try_labels = ['price', 'month', 'day', 'year']
    input_list = common.check_for_int(try_labels)
    input_list.insert(0, input_string)
    common.general_update(table, id_, input_list)
    data_manager.write_table_to_file(file_name, table)
    return table


# special functions:
# ------------------

def get_lowest_price_item_id(table):
    """
    Question: What is the id of the item that was sold for the lowest price?
    if there are more than one item at the lowest price, return the last item by alphabetical order of the title

    Args:
        table (list): data table to work on

    Returns:
         string: id
    """
    (id_, price, price_) = 0, 2, 1
    list_of_id_price = [(table[n][id_], float(table[n][price])) for n in range(len(table))]
    min_ = int(list_of_id_price[0][price_])
    lowest_ptice_id = list_of_id_price[0][id_]
    for i in range(len(lowest_ptice_id)):
        if list_of_id_price[i][price_] < min_:
            min_ = list_of_id_price[i][price_]
            lowest_ptice_id = list_of_id_price[i][id_]
    return lowest_ptice_id
