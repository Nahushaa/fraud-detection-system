import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd

# Load the dataset
df = pd.read_csv('data/creditcard.csv')

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Fraud Detection Dashboard"),
    dcc.Graph(id='class-distribution',
              figure=px.histogram(df, x='Class', title='Transaction Class Distribution'))
])

if __name__ == '__main__':
    app.run_server(debug=True)
