import re


def bills_validator(table_row):
    # Not the best date validation
    valid_pattern_data = r'[0-3][0-9].[0,1][0-9].[2][0][0-9][0-9]'
    valid_status = True
    try:
        int(table_row['№'])
    except ValueError as e:
        valid_status = False
        return valid_status

    try:
        float(table_row['sum'].replace(',', '.'))
    except ValueError:
        valid_status = False
        return valid_status

    if isinstance(table_row['service'], float) or table_row['service'] == '-':
        valid_status = False
        return valid_status

    elif re.search(valid_pattern_data, str(table_row['date'])) == None:
        valid_status = False
        return valid_status

    if isinstance(table_row['client_org'], float)\
    or isinstance(table_row['client_name'], float):
        valid_status = False

    return valid_status


def clients_validator(clients):
    valid_status = True

    if isinstance(clients, float):
        valid_status = False
    return valid_status