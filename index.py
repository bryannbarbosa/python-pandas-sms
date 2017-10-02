import pandas as pd
import re

def analyse_cell(cell):
    value = str(cell)
    value = re.sub("\D", "", value)
    cell = value
    ddi = '55'
    ddd = '11'
    digit = '9'

    nextel = [70, 77, 78, 79]
    fixed = []

    for x in range(10, 50):
        fixed.append(x)
    if int(value[0]) == 0:
        value = value[1:]
    if len(value) <= 7:
        return None
    if len(value) == 8:
        if int(value[0:2]) in nextel:
            cell = ddi + ddd + value
        if int(value[0:2]) in fixed:
            return None
        if int(value[0:2]) not in nextel and int(value[0:2]) not in fixed:
            cell = ddi + ddd + digit + value
    if len(value) == 9:
        if int(value[0:1]) == 9:
            if int(value[1:3]) in nextel:
                cell = ddi + ddd + number[1:]
            if int(value[1:3]) in fixed:
                return None
            if int(value[1:3]) not in nextel and int(value[1:3]) not in fixed:
                cell = ddi + ddd + value
    if len(value) == 10:
        if int(value[0:2]) >= 50:
            if int(value[2:4]) in nextel:
                sub_ddi = value[0:2]
                cell = sub_ddi + ddd + value[2:]
            if int(value[2:4]) in fixed:
                return None
            if int(value[2:4]) not in nextel and int(value[2:4]) not in fixed:
                sub_ddi = value[0:2]
                cell = sub_ddi + ddd + digit + value[2:]
        if int(value[0:2]) < 50:
            if int(value[2:4]) in nextel:
                sub_ddd = value[0:2]
                cell = ddi + sub_ddd + value[2:]
            if int(value[2:4]) in fixed:
                return None
            if int(value[2:4]) not in nextel and int(value[2:4]) not in fixed:
                sub_ddd = value[0:2]
                cell = ddi + sub_ddd + digit + value[2:]
    if len(value) == 11:
        if int(value[0:2]) >= 50:
            if int(value[2]) == 9:
                if int(value[3:5]) in nextel:
                    sub_ddi = value[0:2]
                    cell = sub_ddi + ddd + value[3:]
                if int(value[3:5]) in fixed:
                    return None
                if int(value[3:5]) not in nextel and int(value[3:5]) not in fixed:
                    sub_ddi = value[0:2]
                    cell = sub_ddi + ddd + value[2:]
            if int(value[2]) < 9:
                return None
        if int(value[0:2]) < 50:
            if int(value[2]) == 9:
                if int(value[3:5]) in nextel:
                    sub_ddd = value[0:2]
                    cell = ddi + sub_ddd + value[3:]
                if int(value[3:5]) in fixed:
                    return None
                if int(value[3:5]) not in nextel and int(value[3:5]) not in fixed:
                    sub_ddd = value[0:2]
                    cell = ddi + sub_ddd + value[2:]
            if int(value[2]) < 9:
                return None
    if len(value) == 12:
        if int(value[0:2]) >= 50:
            if int(value[4:6]) in fixed:
                return None
            if int(value[4:6]) not in nextel and int(value[4:6]) not in fixed:
                sub_ddi = value[0:2]
                sub_ddd = value[2:4]
                cell = sub_ddi + sub_ddd + digit + value[4:]
    if len(value) == 13:
        if int(value[0:2]) >= 50 and int(value[2:4]) < 50:
            if int(value[4]) == 9:
                if int(value[5:7]) in nextel:
                    sub_ddi = value[0:2]
                    sub_ddd = value[2:4]
                    cell = sub_ddi + sub_ddd + value[5:]
                if int(value[5:7]) in fixed:
                    return None
            if int(value[4]) < 9:
                return None
        if int(value[0:2]) < 50 and int(value[2:4]) > 50:
            return None
    if len(value) > 13:
        return None

    return cell

def process_file(path):

    # Initialize dataframe and open file
    df = pd.read_excel(path, converters = { 0: analyse_cell }, header = None)
    # Drop rows with NaN or Empty cells
    df.dropna(inplace = True)
    # Convert first column to int
    df[0] = df[0].astype(int)
    # Save the dataframe
    df.to_excel('//home//bryann//Área de Trabalho//excel//test//test01.xlsx', header=None,index=False)


path = 'test.xlsx'

process_file(path)
