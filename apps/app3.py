import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import pandas as pd
import plotly.graph_objs as go
from plotly import tools

from app import app
# insert graph
trace1_inset_graph = go.Scatter(
    x=[1, 2, 3],
    y=[4, 3, 2]
)
trace2_inset_graph = go.Scatter(
    x=[20, 30, 40],
    y=[30, 40, 50],
    xaxis='x2',
    yaxis='y2'
)
data_inset_graph = [trace1_inset_graph, trace2_inset_graph]
layout_inset_graph = go.Layout(
    xaxis2=dict(
        domain=[0.6, 0.95],
        anchor='y2'
    ),
    yaxis2=dict(
        domain=[0.6, 0.95],
        anchor='x2'
    )
)
fig_inset_graph = go.Figure(data=data_inset_graph, layout=layout_inset_graph)

# Subplots
trace1_sbplots = go.Scatter(
    x=[1, 2, 3],
    y=[4, 5, 6],
    mode='markers+text',
    text=['Text A', 'Text B', 'Text C'],
    textposition='bottom center'
)
trace2_sbplots = go.Scatter(
    x=[20, 30, 40],
    y=[50, 60, 70],
    mode='markers+text',
    text=['Text D', 'Text E', 'Text F'],
    textposition='bottom center'
)

fig_sbplots = tools.make_subplots(rows=1, cols=2)

fig_sbplots.append_trace(trace1_sbplots, 1, 1)
fig_sbplots.append_trace(trace2_sbplots, 1, 2)

# Multiple Axes
trace1_multiple_axes = go.Scatter(
    x=[1, 2, 3],
    y=[4, 5, 6],
    name='yaxis1 data'
)
trace2_multiple_axes = go.Scatter(
    x=[2, 3, 4],
    y=[40, 50, 60],
    name='yaxis2 data',
    yaxis='y2'
)
trace3_multiple_axes = go.Scatter(
    x=[4, 5, 6],
    y=[40000, 50000, 60000],
    name='yaxis3 data',
    yaxis='y3'
)
trace4_multiple_axes = go.Scatter(
    x=[5, 6, 7],
    y=[400000, 500000, 600000],
    name='yaxis4 data',
    yaxis='y4'
)
data_multiple_axes = [trace1_multiple_axes, trace2_multiple_axes,
                      trace3_multiple_axes, trace4_multiple_axes]
layout_multiple_axes = go.Layout(
    title='multiple y-axes example',
    width=300,
    xaxis=dict(
        domain=[0.3, 0.7]
    ),
    yaxis=dict(
        title='yaxis title',
        titlefont=dict(
            color='#1f77b4'
        ),
        tickfont=dict(
            color='#1f77b4'
        )
    ),
    yaxis2=dict(
        title='yaxis2 title',
        titlefont=dict(
            color='#ff7f0e'
        ),
        tickfont=dict(
            color='#ff7f0e'
        ),
        anchor='free',
        overlaying='y',
        side='left',
        position=0.15
    ),
    yaxis3=dict(
        title='yaxis4 title',
        titlefont=dict(
            color='#d62728'
        ),
        tickfont=dict(
            color='#d62728'
        ),
        anchor='x',
        overlaying='y',
        side='right'
    ),
    yaxis4=dict(
        title='yaxis5 title',
        titlefont=dict(
            color='#9467bd'
        ),
        tickfont=dict(
            color='#9467bd'
        ),
        anchor='free',
        overlaying='y',
        side='right',
        position=0.85
    )
)
fig_multiple_axes = go.Figure(
    data=data_multiple_axes, layout=layout_multiple_axes)

# range slider and selector

df_range_slider_selector = pd.read_csv(
    'https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv')
df_range_slider_selector.columns = [col.replace('AAPL.', '') for col in df_range_slider_selector.columns]

trace_range_slider_selector = go.Scatter(x=list(df_range_slider_selector.Date),
                   y=list(df_range_slider_selector.High))

data_range_slider_selector = [trace_range_slider_selector]
layout_range_slider_selector = dict(
    title='Time series with range slider and selectors',
    xaxis=dict(
        rangeselector=dict(
            buttons=list([
                dict(count=1,
                     label='1m',
                     step='month',
                     stepmode='backward'),
                dict(count=6,
                     label='6m',
                     step='month',
                     stepmode='backward'),
                dict(count=1,
                     label='YTD',
                     step='year',
                     stepmode='todate'),
                dict(count=1,
                     label='1y',
                     step='year',
                     stepmode='backward'),
                dict(step='all')
            ])
        ),
        rangeslider=dict(
            visible=True
        ),
        type='date'
    )
)

fig_range_slider_selector = dict(data=data_range_slider_selector, layout=layout_range_slider_selector)


layout = html.Div(
    id='app3',
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
                    figure=fig_inset_graph
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
                    figure=fig_sbplots,
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
                    figure=fig_multiple_axes
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
                    figure=fig_range_slider_selector,
                    style={'height': 300},
                    id='my-graph-4'
                )
            ]
        ),
    ]
)


@app.callback(
    Output('app-3-display-value', 'children'),
    [Input('app-3-dropdown', 'value')])
def display_value(value):
    return 'You have selected "{}"'.format(value)
