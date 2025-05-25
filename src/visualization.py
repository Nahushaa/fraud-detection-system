import matplotlib.pyplot as plt
import seaborn as sns

def plot_histograms(df):
    df.hist(figsize=(10, 8))
    plt.savefig('visualizations/histograms.png')

def plot_heatmap(df):
    corr = df.corr()
    sns.heatmap(corr, annot=True, cmap='coolwarm')
    plt.savefig('visualizations/heatmap.png')