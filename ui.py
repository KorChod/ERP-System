""" User Interface (UI) module """


def print_table(table, title_list):
    """
    Prints table with data.

    Example:
        /-----------------------------------\
        |   id   |      title     |  type   |
        |--------|----------------|---------|
        |   0    | Counter strike |    fps  |
        |--------|----------------|---------|
        |   1    |       fo       |    fps  |
        \-----------------------------------/

    Args:
        table (list): list of lists - table to display
        title_list (list): list containing table headers

    Returns:
        None: This function doesn't return anything it only prints to console.
    """

    table_with_titles = [title_list] + table
    columns_width = []

    for column in range(len(title_list)):
        columns_width.append(max([len(item[column]) for item in table] + [len(title_list[column])]))
    columns_width = [width + 2 for width in columns_width]

    separator1 = [(width * '━' + '┳') for width in columns_width[:-1]]
    separator1.insert(0, '┏')
    separator1.append(columns_width[-1] * '━' + '┓')
    separator1 = ''.join(separator1)

    separator2 = [(width * '━' + '╋') for width in columns_width[:-1]]
    separator2.insert(0, '┣')
    separator2.append(columns_width[-1] * '━' + '┫')
    separator2 = ''.join(separator2)

    separator3 = [(width * '━' + '┻') for width in columns_width[:-1]]
    separator3.insert(0, '┗')
    separator3.append(columns_width[-1] * '━' + '┛')
    separator3 = ''.join(separator3)

    for row in range(len(table_with_titles)):
        if row == 0:
            print(separator1)
            for element in range(len(table_with_titles[row])):
                box = (table_with_titles[row][element]).center(columns_width[element])
                print('┃' + box, end='')
            print('┃')
        elif row == len(table_with_titles) - 1:
            print(separator2)
            for element in range(len(table_with_titles[row])):
                box = (table_with_titles[row][element]).center(columns_width[element])
                print('┃' + box, end='')
            print('┃')
            print(separator3)
        else:
            print(separator2)
            for element in range(len(table_with_titles[row])):
                box = (table_with_titles[row][element]).center(columns_width[element])
                print('┃' + box, end='')
            print('┃')


def print_result(result, label):
    """
    Displays results of the special functions.

    Args:
        result: result of the special function (string, list or dict)
        label (str): label of the result

    Returns:
        None: This function doesn't return anything it only prints to console.
    """
    if type(result) is str:
        print(f'{label.title()}: {result}')
    elif type(result) is list:
        print(label.title())
        for i in result:
            print(i)
    elif type(result) is dict:
        print(label.title())
        for key, value in result.items():
            print(f'{key}: {value}')
    else:
        print(f'{label.title()}: {result}')


def print_menu(title, list_options, exit_message):
    """
    Displays a menu. Sample output:
        Main menu:
            (1) Store manager
            (2) Human resources manager
            (3) Inventory manager
            (4) Accounting manager
            (5) Sales manager
            (6) Customer relationship management (CRM)
            (0) Exit program

    Args:
        title (str): menu title
        list_options (list): list of strings - options that will be shown in menu
        exit_message (str): the last option with (0) (example: "Back to main menu")

    Returns:
        None: This function doesn't return anything it only prints to console.
    """

    print(title.upper())
    for i in range(len(list_options)):
        print(f'({i + 1}) \t {list_options[i].title()}')
    print(f'(0) \t {exit_message.title()}')


def get_inputs(list_labels, title):
    """
    Gets list of inputs from the user.
    Sample call:
        get_inputs(["Name","Surname","Age"],"Please provide your personal information")
    Sample display:
        Please provide your personal information
        Name <user_input_1>
        Surname <user_input_2>
        Age <user_input_3>

    Args:
        list_labels (list): labels of inputs
        title (string): title of the "input section"

    Returns:
        list: List of data given by the user. Sample return:
            [<user_input_1>, <user_input_2>, <user_input_3>]
    """
    inputs = []
    print(title)
    for i in range(len(list_labels)):
        inputs.append(input(f'{list_labels[i]}: '))

    return inputs


def print_error_message(message):
    """
    Displays an error message (example: ``Error: @message``)

    Args:
        message (str): error message to be displayed

    Returns:
        None: This function doesn't return anything it only prints to console.
    """

    print(f'Error: {message}')


def print_llama():
    print('''
                                           
                                                        ░░▒▒░░    ░░░░        
                                                      ░░▒▒░░    ░░▒▒░░        
                                                    ░░▒▒▒▒    ░░▒▒░░          
                                                    ▒▒▒▒    ░░▒▒              
                                                  ░░▒▒▒▒  ░░▒▒▒▒              
                                                  ▒▒▒▒▒▒▒▒▒▒▒▒▒▒              
                                                ░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒          
                                              ▒▒▓▓▒▒▒▒▒▒      ▒▒▒▒▒▒▒▒▒▒      
                                              ▒▒▓▓▓▓▒▒▒▒    ▓▓▒▒▒▒▓▓▓▓▒▒▒▒    
                                              ▒▒▒▒▓▓▓▓▒▒      ▒▒▒▒▓▓▒▒▒▒▒▒▒▒  
                                              ▒▒▒▒▒▒▓▓▓▓▓▓▒▒▒▒▒▒▒▒▓▓▒▒▒▒▒▒▒▒  
                                              ▒▒▒▒▒▒▒▒▒▒▓▓▓▓▒▒▒▒▒▒▓▓▒▒        
                                              ▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒
                                              ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░▒▒▒▒▒▒▒▒░░
                                              ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒      ░░░░░░░░  
                                              ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒                
                                              ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒                
                                              ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░              
                                                ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒              
                                                ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒            
                                                ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒            
                                                ░░▒▒░░▒▒░░▒▒▒▒▒▒▒▒            
                              ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░▒▒▒▒            
                  ▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓░░░░░░░░░░░░░░░░            
            ▓▓  ▓▓▓▓▓▓▓▓▓▓▓▓▒▒                ▒▒▓▓▓▓▓▓░░▓▓░░▓▓▓▓░░            
          ▓▓  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒      ▓▓▓▓      ▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓            
        ▓▓  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒    ▓▓▓▓▓▓▓▓    ▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓            
    ''')
