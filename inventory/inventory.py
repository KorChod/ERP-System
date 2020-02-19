""" Inventory module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * name (string): Name of item
    * manufacturer (string)
    * purchase_year (number): Year of purchase
    * durability (number): Years it can be used
"""

import ui
import data_manager
import common

file_name = 'inventory/inventory.csv'


def start_module():
    """
    Starts this module and displays its menu.
     * User can access default special features from here.
     * User can go back to main menu from here.

    Returns:
        None
    """

    option_list = ['Show table', 'Add', 'Remove', 'Update']
    title = 'Inventory module'
    inv_table = data_manager.get_table_from_file('inventory/inventory.csv')

    while True:
        option = common.general_start_module(option_list, title)
        if option == "1":
            show_table(inv_table)
        elif option == "2":
            add(inv_table)
        elif option == "3":
            message = 'Enter item\'s ID you want to delete'
            item_to_delete = ui.get_inputs([message], '')[0]
            remove(inv_table, item_to_delete)
        elif option == "4":
            message = 'Enter item\'s ID you want to update'
            item_to_update = ui.get_inputs([message], '')[0]
            update(inv_table, item_to_update)
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

    titles = ['id', 'name', 'manufacturer', 'purchase year', 'durability']
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
    title = 'New recipt:'
    input_strings = ui.get_inputs(labels, title)
    try_labels = ['purchase year', 'durability']
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
        table (list): list in which record should be updated
        id_ (str): id of a record to update

    Returns:
        list: table with updated record
    """

    title = 'Update item:'
    labels = ['name', 'manufacturer']
    input_strings = ui.get_inputs(labels, title)
    try_labels = ['purchase year', 'durability']
    input_list = common.check_for_int(try_labels)

    input_list.insert(0, input_strings[0])
    input_list.insert(1, input_strings[1])
    common.general_update(table, id_, input_list)
    data_manager.write_table_to_file(file_name, table)

    return table
