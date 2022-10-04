from datetime import timedelta, datetime
import re

DATA_FORMAT='%m/%d/%Y'

def get_dates_in_interval(start_date, end_date):
    result = []
    list_data = []
    try:
        start_date = datetime.strptime(start_date, DATA_FORMAT)
        end_date = datetime.strptime(end_date, DATA_FORMAT)
    except:
        return None

    if start_date == end_date:
        list_data.append(start_date)
        data_fil = filtro_handler(str(list_data))
        return f"{data_fil[1]}/{data_fil[2]}/{data_fil[0]}"

    if start_date < end_date:
        list_data.append(start_date)
        list_data.append(end_date)
        return days_between_dates(list_data,list_dates=[])

    # TODO: Solve normal use case
    return result

def days_between_dates(list_data, list_dates) -> list:

    for i in range((((list_data[1]-list_data[0])).days + 1)):

        data_dir = str(list_data[0] + timedelta(days=i))
        
        data_string=filtro_handler(data_dir)

        data_string=f"{data_string[1]}/{data_string[2]}/{data_string[0]}"
        list_dates.append(data_string)
        
    return list_dates

def filtro_handler(String) -> list:
    return [abs(int(s)) for s in re.findall(r'-?\d+\.?\d*', String)]