import numpy as np
import pandas as pd

def new_client_database(username, country, pack):
    try:
        existing_data = pd.read_csv('info_client.csv')
    except FileNotFoundError:
        existing_data = pd.DataFrame(columns=['Username Telegram', 'Country', 'Pack'])

    new_data = pd.DataFrame([[username, country, pack]], columns=['Username Telegram', 'Country', 'Pack'])
    updated_data = pd.concat([existing_data, new_data], ignore_index=True)

    updated_data.to_csv('info_client.csv', index=False)

    print(f"New client added : {username}, {country}, {pack}")