""" Customer Relationship Management (CRM) module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * name (string)
    * email (string)
    * subscribed (int): Is she/he subscribed to the newsletter? 1/0 = yes/no
"""

import ui
import data_manager
import common

file_name = 'crm/customers.csv'


def start_module():
    """
    Starts this module and displays its menu.
     * User can access default special features from here.
     * User can go back to main menu from here.

    Returns:
        None
    """

    option_list = ['Show table', 'Add', 'Remove', 'Update']
    title = 'CUSTOMER RELATIONSHIP MANAGMENT'
    crm_table = data_manager.get_table_from_file('crm/customers.csv')

    while True:
        option = common.general_start_module(option_list, title)
        if option == "1":
            show_table(crm_table)
        elif option == "2":
            add(crm_table)
        elif option == "3":
            message = 'Enter item\'s ID you want to delete'
            item_to_delete = ui.get_inputs([message], '')[0]
            remove(crm_table, item_to_delete)
        elif option == "4":
            message = 'Enter item\'s ID you want to update'
            item_to_update = ui.get_inputs([message], '')[0]
            update(crm_table, item_to_update)
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

    titles = ['id', 'name', 'email', 'subscribed']
    ui.print_table(table, titles)


def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table (list): table to add new record to

    Returns:
        list: Table with a new record
    """

    labels = ['name', 'email', 'subscribed']
    title = 'New client:'
    input_list = ui.get_inputs(labels, title)
    try:
        int(input_list[2])
        if int(input_list[2]) != 0 and int(input_list[2]) != 1:
            ui.print_error_message('Subscribed has to be 0 or 1')
        else:
            common.general_add(table, input_list)
            data_manager.write_table_to_file(file_name, table)
    except ValueError:
        ui.print_error_message('Subscribed has to be an integer 0 or 1')

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

    things_to_change = ['name', 'email', 'subscribed']
    data_up = ui.get_inputs(things_to_change, '')
    try:
        int(data_up[2])
        if int(data_up[2]) != 0 and int(data_up[2]) != 1:
            ui.print_error_message('Subscribed has to be 0 or 1')
        else:
            common.general_update(table, id_, data_up)
            data_manager.write_table_to_file(file_name, table)
    except ValueError:
        ui.print_error_message('Subscribed has to be an integer 0 or 1')

    return table
