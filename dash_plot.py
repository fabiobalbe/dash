import dash
from dash import dcc
from dash import html
import plotly.graph_objs as go
import numpy as np

app = dash.Dash()

np.random.seed(42)
random_x = np.random.randint(1, 101, 100)
random_y = np.random.randint(1, 101, 100)

app.layout = html.Div([dcc.Graph(id='scatter-plot',
                                 figure={
                                     'data': [go.Scatter(
                                         x=random_x,
                                         y=random_y,
                                         mode='markers',
                                         marker={
                                             'size': 10,
                                             'color': 'rgb(13,273,17)',
                                             'symbol': 'pentagon',
                                             'line': {'width': 2}}
                                     )],
                                     'layout': go.Layout(
                                         title='Titulo',
                                         xaxis={'title': 'Titulo X'},
                                         yaxis={'title': 'Titulo Y'},
                                     )}
                                 ),
                       dcc.Graph(id='scatter-plot2',
                                 figure={
                                     'data': [go.Scatter(
                                         x=random_x,
                                         y=random_y,
                                         mode='markers',
                                         marker={
                                             'size': 10,
                                             'color': 'rgb(143,73,107)',
                                             'symbol': 'circle',
                                                       'line': {'width': 2}}
                                     )],
                                     'layout': go.Layout(
                                         title='Titulo 2',
                                         xaxis={'title': 'Titulo X'},
                                         yaxis={'title': 'Titulo Y'},
                                     )}
                                 )])

if __name__ == '__main__':
    app.run_server(debug=True)
