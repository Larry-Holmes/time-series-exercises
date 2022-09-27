import pandas as pd
import requests




def get_items_data():
    base_url = 'https://python.zgulde.net'         
    endpoint = '/api/v1/items'
    items = []

    while True:
        url = base_url + endpoint
        response = requests.get(url)
        data = response.json()
        items.extend(data['payload']['items'])
        endpoint = data['payload']['next_page']
        if endpoint is None:
            break
                 
    items_df = pd.DataFrame(items)
    return items_df
            
            
            
def get_shop_data():
    base_url = 'https://python.zgulde.net'         
    endpoint = '/api/v1/stores'
    stores = []

    while True:
        url = base_url + endpoint
        response = requests.get(url)
        data = response.json()
        stores.extend(data['payload']['stores'])
        endpoint = data['payload']['next_page']
        if endpoint is None:
            break
    
    stores_df = pd.DataFrame(stores)
    return stores_df

            
def get_sales_data():
    base_url = 'https://python.zgulde.net'         
    endpoint = '/api/v1/sales'
    sales = []

    while True:
        url = base_url + endpoint
        response = requests.get(url)
        data = response.json()
        sales.extend(data['payload']['sales'])
        endpoint = data['payload']['next_page']
        if endpoint is None:
            break
    
    sales_df = pd.DataFrame(sales)
    return sales_df

def get_store_data():
    items_df = get_items_data()
    stores_df = get_shop_data()
    sales_df = get_sales_data()
    
    sales_df = sales_df.rename(columns={'item': 'item_id', 'store': 'store_id'})
    df = pd.merge(sales_df, items_df, how='left', on='item_id')
    df = pd.merge(df, stores_df, how='left', on='store_id')
    
    return df
    