import pandas as pd
from sklearn.preprocessing import StandardScaler

def load_and_preprocess(filepath):
    df = pd.read_csv(filepath)
    df['Amount_scaled'] = StandardScaler().fit_transform(df[['Amount']])
    return df
