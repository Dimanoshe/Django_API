import re


def validator(table_row):
    valid_pattern_data = r'[0-3][0-9].[0,1][0-9].[2][0][0-9][0-9]'

    valid_status = True
    print("Start validator")
    print(table_row['client_name'])
    # print(re.search(valid_pattern_data, str(table_row['date'])) == None)

    try:
        int(table_row['number'])
    except KeyError as e:
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
    
    if isinstance(table_row['client_name'], float)\
    or isinstance(table_row['client_org'], float):
        valid_status = False
        return valid_status

    return valid_status