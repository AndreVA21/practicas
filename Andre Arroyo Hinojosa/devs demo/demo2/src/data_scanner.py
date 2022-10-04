
KEYS = ['serial_no', 'asset_type', 'hardware_standard', 'technical_specs', 'asset_status']
        
def search_asset_by_status(list_items=[], asset_status=''):
    result = []
    if asset_status:
        [result.append(item) for item in list_items if item.get('asset_status') == asset_status]                       
    else:
        return list_items
    return result

def search_asset_by_technical_specs(list_items=[], search_tokens=('', '')):
    result = []
    for item in list_items:
        specs = item.get('technical_specs').lower().split(' ')
        first_token, second_token = search_tokens
        if first_token.lower() in specs and second_token.lower() in specs:
            result.append([value for key, value in item.items() if key in KEYS])
    return result


