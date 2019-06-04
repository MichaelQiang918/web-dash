import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app

import pandas as pd
import numpy as np

import plotly.graph_objs as go
import plotly.figure_factory as ff

# error bar
data_error_bar = [
    go.Scatter(
        x=[1, 2, 3, 4, 5, 6, 7],
        y=[-4, -3, 0, 3, -1, 6, 0],
        error_y=dict(
            type='percent',
            symmetric=False,
            value=15,
            valueminus=25
        )
    )
]
# distplots
# Add histogram data
x1_distplots = np.random.randn(200)-2
x2_distplots = np.random.randn(200)
x3_distplots = np.random.randn(200)+2
x4_distplots = np.random.randn(200)+4

# Group data together
hist_data_distplots = [x1_distplots, x2_distplots, x3_distplots, x4_distplots]

group_labels_distplots = ['Group 1', 'Group 2', 'Group 3', 'Group 4']

# Create distplot with custom bin_size
fig_distplots = ff.create_distplot(
    hist_data_distplots, group_labels_distplots, bin_size=[.1, .25, .5, 1])


# box plots
x_box_plots = ['day 1', 'day 1', 'day 1', 'day 1', 'day 1', 'day 1',
               'day 2', 'day 2', 'day 2', 'day 2', 'day 2', 'day 2']

trace0_box_plots = go.Box(
    y=[0.2, 0.2, 0.6, 1.0, 0.5, 0.4, 0.2, 0.7, 0.9, 0.1, 0.5, 0.3],
    x=x_box_plots,
    name='kale',
    marker=dict(
        color='#3D9970'
    )
)
trace1_box_plots = go.Box(
    y=[0.6, 0.7, 0.3, 0.6, 0.0, 0.5, 0.7, 0.9, 0.5, 0.8, 0.7, 0.2],
    x=x_box_plots,
    name='radishes',
    marker=dict(
        color='#FF4136'
    )
)
trace2_box_plots = go.Box(
    y=[0.1, 0.3, 0.1, 0.9, 0.6, 0.6, 0.9, 1.0, 0.3, 0.6, 0.8, 0.5],
    x=x_box_plots,
    name='carrots',
    marker=dict(
        color='#FF851B'
    )
)
data_box_plots = [trace0_box_plots, trace1_box_plots, trace2_box_plots]
layout_box_plots = go.Layout(
    yaxis=dict(
        title='normalized moisture',
        zeroline=False
    ),
    boxmode='group'
)
fig_box_plots = go.Figure(data=data_box_plots, layout=layout_box_plots)

# Contour
data_contour = [
    go.Contour(
        z=[[10, 10.625, 12.5, 15.625, 20],
           [5.625, 6.25, 8.125, 11.25, 15.625],
           [2.5, 3.125, 5., 8.125, 12.5],
           [0.625, 1.25, 3.125, 6.25, 10.625],
           [0, 0.625, 2.5, 5.625, 10]]
    )
]

layout = html.Div(
    id='app2',
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
                    id='example-graph-1',
                    style={'height': 300},
                    figure=go.Figure(
                        data=data_error_bar,
                        layout=go.Layout(
                            title='US Export of Plastic Scrap',
                            showlegend=True,
                            legend=go.layout.Legend(
                                x=0,
                                y=1.0
                            ),
                            margin=go.layout.Margin(l=40, r=0, t=40, b=30)
                        )
                    )
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
                        data=fig_distplots,
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
                    id='example-graph-3',
                    style={'height': 300},
                    figure=fig_box_plots,
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
                        data=data_contour,
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
    Output('app-2-display-value', 'children'),
    [Input('app-2-dropdown', 'value')])
def display_value(value):
    return 'You have selected "{}"'.format(value)
