import os

def search_files(path, extension):
    csv_files= []

    for root,dirs, files in os.walk(path):
        [csv_files.append(os.path.join(root, file)) for file in files if file.endswith(extension)]  
    return csv_files

def read_data(files):

    list_data = [read_element(element, list_data) for element in files if os.path.exists(element)]
        
    return list_data

def read_element(element, list_data):
    with open(element, 'r') as file:
        data = file.read()
        list_data.append(data) if data is not None else 0

