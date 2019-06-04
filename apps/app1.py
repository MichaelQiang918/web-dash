from app import app
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import plotly.plotly as py
import plotly.graph_objs as go
import numpy as np
# 折线图
N_line = 10
random_x_line = np.linspace(0, 1, N_line)
random_y_line = np.random.randn(N_line)

# Create a trace
trace_line = go.Scatter(
    x=random_x_line,
    y=random_y_line
)

data_line = [trace_line]
# 散点图
N_scatter = 500

trace0_scatter = go.Scatter(
    x=np.random.randn(N_scatter),
    y=np.random.randn(N_scatter)+2,
    name='Above',
    mode='markers',
    marker=dict(
        size=10,
        color='rgba(152, 0, 0, .8)',
        line=dict(
            width=2,
            color='rgb(0, 0, 0)'
        )
    )
)

trace1_scatter = go.Scatter(
    x=np.random.randn(N_scatter),
    y=np.random.randn(N_scatter)-2,
    name='Below',
    mode='markers',
    marker=dict(
        size=10,
        color='rgba(255, 182, 193, .9)',
        line=dict(
            width=2,
        )
    )
)

data_scatter = [trace0_scatter, trace1_scatter]

layout_scatter = dict(title='Styled Scatter',
                      yaxis=dict(zeroline=False),
                      xaxis=dict(zeroline=False)
                      )

# 柱状图
data_bar = [go.Bar(
    x=['giraffes', 'orangutans', 'monkeys','giraffes1', 'orangutans1', 'monkeys1', 'giraffes2'],
    y=[20, -14, 23, 99, 100, -11, 19]
)]


layout = html.Div(
    id='app1',
    style={
        'height': '100%',
        'display': 'grid',
        'grid-template-columns': '1fr 1fr',
        'grid-template-rows': '1fr 1fr',
        'gap': '10px',
        'padding': '10px',
    },
    children=[
        html.Div(
            style={
                'color': 'rgba(0, 0, 0, 0.87)',
                'width': '100%',
                'background': '#FFF',
                'box-shadow': '0 1px 4px 0 rgba(0, 0, 0, 0.14)',
                'border-radius': '6px',
            },
            children=[
                dcc.Graph(
                    figure=go.Figure(
                        data=data_line,
                        layout=go.Layout(
                            title='US Export of Plastic Scrap',
                            showlegend=True,
                            legend=go.layout.Legend(
                                x=0,
                                y=1.0
                            ),
                            margin=go.layout.Margin(l=40, r=0, t=40, b=30)
                        )
                    ),
                    style={'height': 300},
                    id='my-graph-1'
                )
            ]
        ),
        html.Div(
            style={
                'color': 'rgba(0, 0, 0, 0.87)',
                'width': '100%',
                'background': '#FFF',
                'box-shadow': '0 1px 4px 0 rgba(0, 0, 0, 0.14)',
                'border-radius': '6px',
            },
            children=[
                dcc.Graph(
                    figure=go.Figure(
                        data=data_scatter,
                        layout=layout_scatter,
                    ),
                    style={'height': 300},
                    id='my-graph-2'
                )
            ]
        ),
        html.Div(
            style={
                'color': 'rgba(0, 0, 0, 0.87)',
                'width': '100%',
                'background': '#FFF',
                'box-shadow': '0 1px 4px 0 rgba(0, 0, 0, 0.14)',
                'border-radius': '6px',
            },
            children=[
                dcc.Graph(
                    figure=go.Figure(
                        data=data_bar,
                        layout=go.Layout(
                            title='US Export of Plastic Scrap',
                            showlegend=True,
                            legend=go.layout.Legend(
                                x=0,
                                y=1.0
                            ),
                            margin=go.layout.Margin(l=40, r=0, t=40, b=30)
                        )
                    ),
                    style={'height': 300},
                    id='my-graph-3'
                )
            ]
        ),
        html.Div(
            style={
                'color': 'rgba(0, 0, 0, 0.87)',
                'width': '100%',
                'background': '#FFF',
                'box-shadow': '0 1px 4px 0 rgba(0, 0, 0, 0.14)',
                'border-radius': '6px',
            },
            children=[
                dcc.Graph(
                    figure=go.Figure(
                        data=[
                            go.Bar(
                                x=[1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003,
                                   2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012],
                                y=[219, 146, 112, 127, 124, 180, 236, 207, 236, 263,
                                   350, 430, 474, 526, 488, 537, 500, 439],
                                name='Rest of world',
                                marker=go.bar.Marker(
                                    color='rgb(55, 83, 109)'
                                )
                            ),
                            go.Bar(
                                x=[1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003,
                                   2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012],
                                y=[16, 13, 10, 11, 28, 37, 43, 55, 56, 88, 105, 156, 270,
                                   299, 340, 403, 549, 499],
                                name='China',
                                marker=go.bar.Marker(
                                    color='rgb(26, 118, 255)'
                                )
                            )
                        ],
                        layout=go.Layout(
                            title='US Export of Plastic Scrap',
                            showlegend=True,
                            legend=go.layout.Legend(
                                x=0,
                                y=1.0
                            ),
                            margin=go.layout.Margin(l=40, r=0, t=40, b=30)
                        )
                    ),
                    style={'height': 300},
                    id='my-graph-4'
                )
            ]
        ),
    ]
)


@app.callback(
    Output('app-1-display-value', 'children'),
    [Input('app-1-dropdown', 'value')])
def display_value(value):
    return 'You have selected "{}"'.format(value)
