import numpy as np
import pandas as pd

import os

from cyberbullying.utils import clean_df


class Data:
    def __init__(self):
        self.path_file = os.path.dirname(__file__) # no funciona en jupyter
        self.path_raw_data = os.path.join(self.path_file, '../raw_data/')
        self.path_data = os.path.join(self.path_file, 'data/')

        self.file_names = os.listdir(path=self.path_raw_data)
        self.files = {file.replace('_parsed', '').replace('_dataset','').replace('.csv',''): file for file in self.file_names if file.endswith('.csv')}

    def get_data(self, datasets='all'):
        """
        Importa los .csv seleccionados que están contenidos en la carpeta 'raw data'
        datasets: {'all', ['toxicity', 'aggression', 'twitter', 'twitter_sexism', 'twitter_racism', 'youtube', 'kaggle']}
        """
        all_datasets = self.files

        if datasets == 'all':
            datasets_dict = all_datasets

        else:
            if isinstance(datasets, str):
                datasets = [datasets]

                print(datasets)

                for dataset in datasets:
                    if dataset not in all_datasets.keys():
                        print('Error en nombre de dataset')
                        return

            datasets_dict = {key:value for key, value in all_datasets.items() if key in datasets}

        data = {name: pd.read_csv(self.path_raw_data+file, usecols=['Text', 'oh_label']) for name, file in datasets_dict.items()}
        print(data.keys())

        def reorder_df(df):
            df = df.copy()
            df.rename(columns={'Text': 'text', 'oh_label':'target'}, inplace=True)
            df = df[['text', 'target']]
            return df

        def limit_length(text):
            if ' ' in text:
                text = len(text.split()) <=1000
            return text

        for name in data.keys():
            data[name] = reorder_df(data[name])
            #data[name] = data[name][data[name]['text'].map(limit_length)] # no funciona
        print([dataset for dataset in data.keys()])
        df = pd.concat([dataset for dataset in data.values()], ignore_index=True).dropna().drop_duplicates().reset_index(drop=True)

        return df

    def get_data_classification(self):
        """Importa los 3 csv de classification"""

        df1 = pd.read_csv(self.path_raw_data+'/classification/cyberbullying_tweets.csv')
        df1 = df1.rename(columns={'tweet_text':'text', 'cyberbullying_type':'type'})
        df1 = df1[df1['type']!='not_cyberbullying']
        df1['type'] = df1['type'].str.replace('_cyberbullying', '')

        df2 = pd.read_csv(self.path_raw_data+self.files['twitter_racism'], usecols=['Text', 'oh_label'])
        df2 = df2.rename(columns={'Text':'text'})
        df2 = df2[df2['oh_label']==1]
        df2['type']='ethnicity'
        df2 = df2.drop(columns='oh_label')

        df3 = pd.read_csv(self.path_raw_data+self.files['twitter_sexism'], usecols=['Text', 'oh_label'])
        df3 = df3.rename(columns={'Text':'text'})
        df3 = df3[df3['oh_label']==1]
        df3['type']='gender'
        df3 = df3.drop(columns='oh_label')

        df = pd.concat([df1, df2, df3])

        return df

    def save_data(self):
        self.df.to_csv(f'{self.path_data}dataset.csv', index=False)

    # no se usa para entrenar
    def get_clean_data(self, datasets='all'):
        if datasets == 'all':
            return pd.read_csv(f'{self.path_data}dataset.csv')
