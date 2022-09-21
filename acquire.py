import pandas as pd
import requests

def acquire(link, target):
    '''
    Function takes in: 
    link = url
    target = endpoint
    '''
    response = requests.get(link)

    data = response.json()

    return pd.DataFrame(data['payload'][target])

while True:
    url = base_url + endpoint
    response = requests.get(url)
    data = response.json()
    print(f'Getting page {data['payload']['page']} of {data['payload'][]}
    items.extend(data['payload']['items']
    endpoint = data['payload']['next_page']
    if endpoint is None:
                 break
def add_pages(df, base_url, target, n):
    for i in range(2,n):
    point = f'/api/v1/{target}?page={i}'
    response = requests.get(base_url + point)
    data = response.json()

    current_page = data['payload']['page']
    max_page = data['payload']['max_page']
    next_page = data['payload']['next_page']
    

    df = pd.concat([df, pd.DataFrame(data['payload'][f'{target}'])])