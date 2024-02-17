import numpy as np
import pandas as pd

# data = np.array([['Alice', 'Smith'],
#                  ['Bob', 'Doe'],
#                  ['Charlie', 'Johnson']])

# new_row = np.array(['Jules', 'Dupont'])

# data = np.vstack([data, new_row])

# df = pd.DataFrame(data, columns=['Prénom', 'Nom'])
# print(df)

# new_row = np.array(['Verone', 'Sabb'])

# data = np.vstack([data, new_row])

# df = pd.DataFrame(data, columns=['Prénom', 'Nom'])
# print(df)

# # Conversion du tableau NumPy en DataFrame Pandas
# df = pd.DataFrame(data, columns=['Prénom', 'Nom'])

# # Enregistrement du DataFrame dans un fichier CSV nommé 'info_client.csv'
# df.to_csv('info_client.csv', index=False)

# print("Fichier CSV 'info_client.csv' créé avec succès.")

def new_client_database(username, country, pack):
    database = np.array(['.', '.', '.'])
    new_client = np.array([username, country, pack])
    database = np.vstack([database, new_client])
    dataframe = pd.DataFrame(database, columns=['Username Telegram', 'Country', 'Pack'])
    dataframe.to_csv('info_client.csv', index=False)
    print(dataframe)

