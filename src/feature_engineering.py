def engineer_features(df):
    df['AvgCharges'] = df['TotalCharges'] / df['tenure']
    return df